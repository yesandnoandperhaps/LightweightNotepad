import re

from function.variables.ProjectDictionaryVariables import YONG_MING_TI_LIST, THIRTY_EIGHT_ALPHABET
from function.variables.ProjectPathVariables import YONG_MING_TI_DATA_JSON, RECONSTRUCTIONS_SQLITE, RECONSTRUCTIONS, \
    RECONSTRUCTIONS_LIST, RECONSTRUCTIONS_VOWEL, RECONSTRUCTIONS_VOWEL_RECONSTRUCTIONS_LIST_PATH
from module.Kaom import GetThePage, PhoneticDatabaseProcessor, TabularDatabaseExtraction, FileProcessor, HtmlToSqlite, \
    SyllableSplitting, SyllableHtmlToSqlite


class YongMingTi:
    def __init__(self,text_widget):
        self.text_widget = text_widget
        self.get_all = '\n'.join(line.strip() for line in text_widget.get("1.0", "end").splitlines())
        self.var_0 = YONG_MING_TI_LIST[0][YONG_MING_TI_DATA_JSON[0]]
        self.var_1 = YONG_MING_TI_LIST[1][YONG_MING_TI_DATA_JSON[1]]
        self.var_2 = YONG_MING_TI_LIST[2][YONG_MING_TI_DATA_JSON[2]]
        self.var_3 = YONG_MING_TI_LIST[3][YONG_MING_TI_DATA_JSON[3]]
        self.var_4 = YONG_MING_TI_LIST[4][YONG_MING_TI_DATA_JSON[4]]
        self.var_5 = YONG_MING_TI_LIST[5][YONG_MING_TI_DATA_JSON[5]]
        self.var_6 = YONG_MING_TI_LIST[6][YONG_MING_TI_DATA_JSON[6]]
        self.var_7 = YONG_MING_TI_LIST[7][YONG_MING_TI_DATA_JSON[7]]
        self.var_8 = YONG_MING_TI_LIST[8][YONG_MING_TI_DATA_JSON[8]]

    def fetch(self):

        get_all_list = list(re.sub(r'[^\u4e00-\u9fa5]', '', self.get_all))

        need_to_look_list = []
        qing_zhuo_list = []
        sheng_diao_list = []
        reconstructions_list = []
        yun_list = []
        main_vowel_rhyme_tail_list = []
        shengmu_yuanyin_yunwei_list = []

        phonetic_processor = PhoneticDatabaseProcessor(db_path=RECONSTRUCTIONS_SQLITE)
        extract_the_phenotype_sqlite = TabularDatabaseExtraction(RECONSTRUCTIONS_SQLITE)
        extract_the_phenotype_sqlite.connect()

        for word in get_all_list:
            result = phonetic_processor.get_phonetic(headword=word, era=self.var_0, nature=self.var_1, scholar=self.var_2)
            if self.matching(result):
                need_to_look_list.append(word)#未找到，需启动

        crawler = GetThePage(''.join(need_to_look_list))
        crawler.crawl_words()
        html_list = FileProcessor(RECONSTRUCTIONS, RECONSTRUCTIONS_LIST).save_content()

        processor = HtmlToSqlite(RECONSTRUCTIONS_SQLITE)
        processor.process_html_files(html_list)
        processor.close()

        qing_zhuo_table_dict = {
            "廣韻-基於poem": "guang_yun",
            "玉篇-基於poem": "yu_pian"
        }

        valid_scholars = [
            '西漢', '東漢', '魏', '晉', '宋北魏後期',
            '北魏後期北齊', '齊梁陳北周隋'
        ]

        table_dict = {
            "廣韻-基於poem": "guang_yun",
            "玉篇-基於poem": "yu_pian",
            "平水韻": "ping_shui_yun"
        }

        for word in get_all_list:
            result = phonetic_processor.get_phonetic(headword=word, era=self.var_0, nature=self.var_1,
                                                     scholar=self.var_2)

            '''擬音'''
            reconstructions_list.append(result)

            '''清濁'''
            qing_zhuo_list.append(THIRTY_EIGHT_ALPHABET[extract_the_phenotype_sqlite.get_sheng_nu(word,qing_zhuo_table_dict.get(self.var_3, "guang_yun"),"聲紐")])#清濁问题

            '''韻部'''
            if self.var_3 in valid_scholars:
                yun_list.append(phonetic_processor.get_phonetic(
                    headword=word, era="兩漢六朝", nature="韻部", scholar=self.var_3
                ))
            elif self.var_3 == "廣韻-基於poem":
                yun_list.append(extract_the_phenotype_sqlite.get_sheng_nu(word,"guang_yun","韻部_調整後"))
            elif self.var_3 == "玉篇-基於poem":
                yun_list.append(extract_the_phenotype_sqlite.get_sheng_nu(word,"yu_pian","韻部"))
            elif self.var_3 == "平水韻":
                yun_list.append(extract_the_phenotype_sqlite.get_sheng_nu(word,"ping_shui_yun","韻部"))

            '''聲調'''
            if self.var_4 == "平上去入":
                sheng_diao_list.append(extract_the_phenotype_sqlite.get_sheng_nu(word,table_dict.get(self.var_3, "guang_yun"),"聲調"))
            else:
                sheng_diao = extract_the_phenotype_sqlite.get_sheng_nu(word,table_dict.get(self.var_3, "guang_yun"),"聲調")
                if sheng_diao in ["上", "去", "入"]:
                    sheng_diao_list.append("仄")
                else:
                    sheng_diao_list.append(sheng_diao)



        crawler = SyllableSplitting()
        crawler.crawl_words_initiate(reconstructions_list)

        html_list = FileProcessor(RECONSTRUCTIONS_VOWEL, RECONSTRUCTIONS_VOWEL_RECONSTRUCTIONS_LIST_PATH).save_content()

        '''音节拆分，写入韵母'''
        converter = SyllableHtmlToSqlite(html_list,["序號", "字表", "聲母", "介音", "元音", "韻尾", "聲調", "韻母", "聲韻"],
                                         RECONSTRUCTIONS_SQLITE, "cut_the_voicing")
        converter.convert()

        if self.var_8 == "主元音韻尾檢查-半聯" or "主元音韻尾檢查-全聯":
            for word in get_all_list:
                a = extract_the_phenotype_sqlite.get_sheng_nu(word, "cut_the_voicing", "元音") or ""
                b = extract_the_phenotype_sqlite.get_sheng_nu(word, "cut_the_voicing", "韻尾") or ""
                main_vowel_rhyme_tail_list.append(a + b)
        elif self.var_8 == "韻母檢查-半聯" or "韻母檢查-全聯":
            for word in get_all_list:
                main_vowel_rhyme_tail_list.append(extract_the_phenotype_sqlite.get_sheng_nu(word, "cut_the_voicing", "韻母") or "")

        '''写入正紐-声母-主元音-韵尾'''
        for word in get_all_list:
            a = extract_the_phenotype_sqlite.get_sheng_nu(word, "cut_the_voicing", "聲母") or ""
            b = extract_the_phenotype_sqlite.get_sheng_nu(word, "cut_the_voicing", "元音") or ""
            c = extract_the_phenotype_sqlite.get_sheng_nu(word, "cut_the_voicing", "韻尾") or ""
            main_vowel_rhyme_tail_list.append(a + b + c)

        extract_the_phenotype_sqlite.close()
        phonetic_processor.close()

        s = self.sickness_detect(sheng_diao_list,qing_zhuo_list,yun_list,main_vowel_rhyme_tail_list,shengmu_yuanyin_yunwei_list,get_all_list)

        print(s)

        return s

    @staticmethod
    def matching(string):
        return bool(re.search(r'.*未找到.*', string))

    def sickness_detect(self,sheng_diao_list,qing_zhuo_list,yun_list,main_vowel_rhyme_tail_list,shengmu_yuanyin_yunwei_list,get_all_list):
        """
        :param shengmu_yuanyin_yunwei_list: 聲母與主元音與韻尾列表
        :param main_vowel_rhyme_tail_list: 主元音與韻尾列表或韻母列表
        :param yun_list: 韻部列表
        :param qing_zhuo_list: 清濁列表
        :param sheng_diao_list: 聲調列表
        :param get_all_list: 字符列表
        :return:
        """

        '''押韻'''

        tenth_elements = [yun_list[i] for i in range(9, len(sheng_diao_list), 10)]

        get_all_list = self.rhyme_or_shang_wei(tenth_elements,get_all_list,10,9,"出韻")

        '''平頭'''

        if sheng_diao_list[0] == sheng_diao_list[5]:
            _0 = get_all_list[0]
            _5 = get_all_list[5]
            get_all_list[0]=f"{_0}-平頭"
            get_all_list[5]=f"{_5}-平頭"

        if sheng_diao_list[1] == sheng_diao_list[6]:
            _1 = get_all_list[1]
            _6 = get_all_list[6]
            get_all_list[1] = f"{_1}-平頭"
            get_all_list[6] = f"{_6}-平頭"

        '''上尾'''

        # 提取每五个元素的第五个元素
        fifth_elements = [sheng_diao_list[i] for i in range(4, len(sheng_diao_list), 5)]

        get_all_list = self.rhyme_or_shang_wei(fifth_elements,get_all_list,5,4,"上尾")

        """
        # 遍历每两个相邻元素，检查是否相等
        for i in range(0, len(fifth_elements) - 1, 2):
            if fifth_elements[i] == fifth_elements[i + 1]:
                # 找到所有相等元素在 fifth_elements 中的位置
                value = fifth_elements[i]  # 当前相等的值
                for j in range(i, len(fifth_elements)):
                    if fifth_elements[j] == value:
                        # 每次都使用不同的索引进行处理，即使值相同
                        idx = j * 5 + 4  # 每个结果对应 get_all_list 中的索引 (按 5 个间隔计算)
                        _item = get_all_list[idx]
                        get_all_list[idx] = f"{_item}-上尾"  # 修改 get_all_list 中的元素
        """

        '''蜂腰'''

        '''聲調'''

        # 提取每五个元素的第二个元素，并保留索引
        first_elements = [(sheng_diao_list[i], i) for i in range(1, len(sheng_diao_list), 5)]

        # 获取每五个元素的第四个元素，并保留索引
        fourth_elements = [(sheng_diao_list[i], i) for i in range(3, len(sheng_diao_list), 5)]

        # 提取每五个元素的第五个元素，并保留索引
        fifth_elements_new = [(sheng_diao_list[i], i) for i in range(4, len(sheng_diao_list), 5)]

        '''清濁'''
        # 提取每五个元素的第二个元素，并保留索引
        first_elements_qing_zhuo = [(qing_zhuo_list[i], i) for i in range(1, len(qing_zhuo_list), 5)]

        # 获取每五个元素的第四个元素，并保留索引
        fourth_elements_qing_zhuo = [(qing_zhuo_list[i], i) for i in range(3, len(qing_zhuo_list), 5)]

        if self.var_5 == "二五同調":
            get_all_list = self.rhyme_or_feng_yao(get_all_list, first_elements, fifth_elements_new, sickness="蜂腰")
        elif self.var_5 == "二四同調":
            get_all_list = self.rhyme_or_feng_yao(get_all_list, first_elements, fourth_elements, sickness="蜂腰")
        elif self.var_5 == "二四同濁":
            get_all_list = self.rhyme_or_feng_yao(get_all_list, first_elements_qing_zhuo, fourth_elements_qing_zhuo, True, False, False,"濁", "蜂腰")
        elif self.var_5 == "二四同濁調":
            get_all_list = self.rhyme_or_feng_yao(get_all_list, first_elements, fourth_elements, sickness="蜂腰")
            get_all_list = self.rhyme_or_feng_yao(get_all_list, first_elements_qing_zhuo, fourth_elements_qing_zhuo, True, False, False, "濁", "蜂腰")
        elif self.var_5 == "中濁四清":
            get_all_list = self.feng_yao_compare_and_update(qing_zhuo_list, get_all_list,"濁","蜂腰")
        else:
            get_all_list = self.feng_yao_compare_and_update(qing_zhuo_list, get_all_list,"濁","蜂腰")

        '''鶴膝'''

        if self.var_6 == "五與十五同調":
            if sheng_diao_list[4] == sheng_diao_list[14]:
                _0 = get_all_list[4]
                _5 = get_all_list[14]
                get_all_list[4] = f"{_0}-鶴膝"
                get_all_list[14] = f"{_5}-鶴膝"
        elif self.var_6 == "二四同清":
            get_all_list = self.rhyme_or_feng_yao(get_all_list, first_elements_qing_zhuo, fourth_elements_qing_zhuo, True,False,False, "清", "鶴膝")
        elif self.var_6 == "中清四濁":
            get_all_list = self.feng_yao_compare_and_update(qing_zhuo_list, get_all_list, "清","鶴膝")
        else:
            get_all_list = self.feng_yao_compare_and_update(qing_zhuo_list, get_all_list, "清", "鶴膝")

        '''大韻'''

        # 提取每十个元素的第一个元素，并保留索引
        first_elements_yun = [(yun_list[i], i) for i in range(0, len(yun_list), 10)]

        # 获取每十个元素的第十个元素，并保留索引
        tenth_elements_yun = [(yun_list[i], i) for i in range(9, len(yun_list), 10)]

        get_all_list = self.rhyme_or_feng_yao(get_all_list, first_elements_yun, tenth_elements_yun, False, True, sickness="大韻")

        '''小韻'''

        if self.var_7 == "字韻部不同":
            get_all_list = self.xiao_yun_compare_and_update(yun_list,get_all_list)
        elif self.var_7 == "上下字韻部不同":
            start_with_0_extract_5_skip_5 = self.extract_5_skip_5(yun_list)
            start_with_5_extract_5_skip_5 = self.extract_5_skip_5(yun_list, 5)
            get_all_list = self.rhyme_or_feng_yao(get_all_list,start_with_0_extract_5_skip_5,start_with_5_extract_5_skip_5,xiao_yun=True,sickness="小韻")
        else:
            # 提取每十个元素的第四个元素，并保留索引
            fourth_elements_yun = [(yun_list[i], i) for i in range(3, len(yun_list), 10)]

            # 提取每十个元素的第六个元素，并保留索引
            sixth_elements_yun = [(yun_list[i], i) for i in range(5, len(yun_list), 10)]

            get_all_list = self.rhyme_or_feng_yao(get_all_list,fourth_elements_yun,sixth_elements_yun,xiao_yun=True,sickness="小韻")


        '''旁紐'''

        if self.var_8 == "韻部檢查-全聯":
            start_with_0_extract_5_skip_5 = self.extract_5_skip_5(yun_list)
            start_with_5_extract_5_skip_5 = self.extract_5_skip_5(yun_list, 5)
            get_all_list = self.rhyme_or_feng_yao(get_all_list, start_with_0_extract_5_skip_5,
                                                  start_with_5_extract_5_skip_5, xiao_yun=True, sickness="旁紐")
        elif self.var_8 == "韻部檢查-半聯":
            get_all_list = self.xiao_yun_compare_and_update(yun_list, get_all_list,'旁紐',5)
        elif self.var_8 == "主元音韻尾檢查-半聯" or "韻母檢查-半聯":
            get_all_list = self.xiao_yun_compare_and_update(main_vowel_rhyme_tail_list, get_all_list, '旁紐', 5)
        elif self.var_8 == "主元音韻尾檢查-全聯" or "韻母檢查-全聯":
            start_with_0_extract_5_skip_5 = self.extract_5_skip_5(main_vowel_rhyme_tail_list)
            start_with_5_extract_5_skip_5 = self.extract_5_skip_5(main_vowel_rhyme_tail_list, 5)
            get_all_list = self.rhyme_or_feng_yao(get_all_list, start_with_0_extract_5_skip_5,
                                                  start_with_5_extract_5_skip_5, xiao_yun=True, sickness="旁紐")

        '''正紐'''
        start_with_0_extract_5_skip_5 = self.extract_5_skip_5(shengmu_yuanyin_yunwei_list)
        start_with_5_extract_5_skip_5 = self.extract_5_skip_5(shengmu_yuanyin_yunwei_list, 5)
        get_all_list = self.rhyme_or_feng_yao(get_all_list, start_with_0_extract_5_skip_5,
                                              start_with_5_extract_5_skip_5, xiao_yun=True, sickness="正紐")

        return get_all_list
    @staticmethod
    def rhyme_or_shang_wei(elements,get_all_list,group_elements_num,segmentation_num,sickness="上尾"):
        for i in range(0, len(elements) - 1, 2):
            if elements[i] == elements[i + 1]:
                # 找到所有相等元素在 elements 中的位置
                value = elements[i]  # 当前相等的值
                for j in range(i, len(elements)):
                    if elements[j] == value:
                        idx = j * group_elements_num + segmentation_num
                        _item = get_all_list[idx]
                        get_all_list[idx] = f"{_item}-{sickness}"
        return get_all_list

    @staticmethod
    def rhyme_or_feng_yao(get_all_list, elements_0, elements_1, qing_zhuo=False,rhyme=False,xiao_yun=False, qing_zhuo_word="濁", sickness="蜂腰"):
        for i in range(min(len(elements_0), len(elements_1))):
            first_value, first_index = elements_0[i]
            fourth_value, fourth_index = elements_1[i]

            if qing_zhuo:#清濁匹配
                if first_value == qing_zhuo_word and fourth_value == qing_zhuo_word:
                    print(f"匹配: {first_value} 和 {fourth_value}")

                    # 修改 get_all_list 对应位置
                    get_all_list[first_index] = f"{get_all_list[first_index]}-{sickness}"
                    get_all_list[fourth_index] = f"{get_all_list[fourth_index]}-{sickness}"
            else:#聲調匹配或押韻匹配
                if rhyme:
                    if first_value != fourth_value:
                        print(f"不匹配: {first_value} 和 {fourth_value}")

                        # 修改 get_all_list 对应位置
                        get_all_list[first_index] = f"{get_all_list[first_index]}-{sickness}"
                        get_all_list[fourth_index] = f"{get_all_list[fourth_index]}-{sickness}"
                else:
                    if first_value == fourth_value:
                        print(f"匹配: {first_value} 和 {fourth_value}")
                        if xiao_yun:
                            # 修改 get_all_list 对应位置
                            get_all_list[first_index] = f"{get_all_list[first_index]}-{first_value}{sickness}"
                            get_all_list[fourth_index] = f"{get_all_list[fourth_index]}-{fourth_value}{sickness}"
                        else:
                            # 修改 get_all_list 对应位置
                            get_all_list[first_index] = f"{get_all_list[first_index]}-{sickness}"
                            get_all_list[fourth_index] = f"{get_all_list[fourth_index]}-{sickness}"
        return get_all_list

    @staticmethod
    def _1to5_(data):
        result = []
        for i in range(0, len(data), 5):
            # 提取每5个元素为一组
            group = data[i:i + 5]
            # 提取第1、2、3、4、5个元素
            extracted = [(group[j], i + j) for j in range(5) if j < len(group)]
            # 将每5个元素分成一个列表
            result.append(extracted)
        return result

    @staticmethod
    def extract_5_skip_5(data, start_index=0):
        """
        提取元素的函数，可从指定索引开始，每次提取5个元素，然后跳过5个元素。

        :param data: 输入的数据列表
        :param start_index: 开始提取的索引（默认从0开始）
        :return: 处理后的结果列表
        """
        result = []
        for i in range(start_index, len(data), 10):  # 从指定索引开始，每次跳过5个元素，再提取5个
            # 提取从i开始的5个元素
            group = data[i:i + 5]
            # 提取第1、2、3、4、5个元素
            extracted = [(group[j], i + j) for j in range(5) if j < len(group)]
            # 将每5个元素分成一个列表
            result.append(extracted)
        return result

    @staticmethod
    def _1to10_(data):
        result = []
        for i in range(0, len(data), 10):  # 每次取10个元素
            # 提取每10个元素为一组
            group = data[i:i + 10]
            # 提取第1到10个元素
            extracted = [(group[j], i + j) for j in range(10) if j < len(group)]
            # 将每10个元素分成一个列表
            result.append(extracted)
        return result

    @staticmethod
    def xiao_yun_compare_and_update(yun_list, get_all_list, sickness="小韻",_1towhat_=10):
        # 提取并分组
        if _1towhat_ == 10:
            grouped_yun = YongMingTi._1to10_(yun_list)
        elif _1towhat_ == 5:
            grouped_yun = YongMingTi._1to5_(yun_list)
        else:
            grouped_yun = YongMingTi._1to10_(yun_list)

        for group in grouped_yun:
            # 用于记录每组中元素的索引
            element_indices = {}
            for element, original_index in group:
                if element in element_indices:
                    # 如果该元素已出现过，检查并更新对应位置
                    previous_index = element_indices[element]
                    if f"-{element}{sickness}" not in get_all_list[previous_index]:
                        get_all_list[previous_index] += f"-{element}{sickness}"
                    if f"-{element}{sickness}" not in get_all_list[original_index]:
                        get_all_list[original_index] += f"-{element}{sickness}"
                else:
                    # 记录该元素及其索引
                    element_indices[element] = original_index

        return get_all_list
    @staticmethod
    def feng_yao_compare_and_update(qing_zhuo_list, get_all_list,qing_zhuo_word="濁",sickness="蜂腰"):
        grouped_sheng_diao = YongMingTi._1to5_(qing_zhuo_list)
        qing_zhuo_dict = {
            "清":"濁",
            "濁":"清"
        }

        for group_idx, group in enumerate(grouped_sheng_diao):
            # 检查1、2、4、5是否相等
            if len(group) >= 5 and group[0][0] == group[1][0] == group[3][0] == group[4][0] == qing_zhuo_dict[qing_zhuo_word]:
                # 检查第3个元素是否为"濁"
                if group[2][0] == qing_zhuo_word:
                    # 更新 get_all_list 对应位置
                    for idx in [0, 1, 3, 4]:  # 更新1、2、4、5元素
                        get_all_list[group[idx][1]] += f"-{sickness}{qing_zhuo_dict[qing_zhuo_word]}"
                    get_all_list[group[2][1]] += f"-{sickness}{qing_zhuo_word}"  # 更新第3个元素
        return get_all_list