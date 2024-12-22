import re

from function.variables.ProjectDictionaryVariables import YONG_MING_TI_LIST, THIRTY_EIGHT_ALPHABET
from function.variables.ProjectPathVariables import YONG_MING_TI_DATA_JSON, RECONSTRUCTIONS_SQLITE, RECONSTRUCTIONS, \
    RECONSTRUCTIONS_LIST
from module.Kaom import GetThePage, PhoneticDatabaseProcessor, GuangYunDatabase, FileProcessor, HtmlToSqlite


class YongMingTi:
    def __init__(self,text_widget):
        self.text_widget = text_widget
        self.get_all = '\n'.join(line.strip() for line in text_widget.get("1.0", "end").splitlines())
        self.var_0 = YONG_MING_TI_LIST[0][YONG_MING_TI_DATA_JSON[0]]
        self.var_1 = YONG_MING_TI_LIST[1][YONG_MING_TI_DATA_JSON[1]]
        self.var_2 = YONG_MING_TI_LIST[2][YONG_MING_TI_DATA_JSON[2]]
        self.var_3 = YONG_MING_TI_LIST[3][YONG_MING_TI_DATA_JSON[3]]
        self.var_4 = YONG_MING_TI_LIST[4][YONG_MING_TI_DATA_JSON[4]]

    def fetch(self):

        get_all_list = list(re.sub(r'[^\u4e00-\u9fa5]', '', self.get_all))

        need_to_look_list = []
        qing_zhuo_list = []
        sheng_diao_list = []

        phonetic_processor = PhoneticDatabaseProcessor(db_path=RECONSTRUCTIONS_SQLITE)
        guang_yun_sqlite = GuangYunDatabase(RECONSTRUCTIONS_SQLITE)
        guang_yun_sqlite.connect()

        for word in get_all_list:
            result = phonetic_processor.get_phonetic(headword=word, era=self.var_0, nature=self.var_1, scholar=self.var_2)
            if self.matching(result):
                need_to_look_list.append(word)#未找到，需启动

        crawler = GetThePage(need_to_look_list)
        crawler.crawl_words()
        html_list = FileProcessor(RECONSTRUCTIONS, RECONSTRUCTIONS_LIST).save_content()

        processor = HtmlToSqlite(RECONSTRUCTIONS_SQLITE)
        processor.process_html_files(html_list)
        processor.close()

        for word in get_all_list:
            result = phonetic_processor.get_phonetic(headword=word, era=self.var_0, nature=self.var_1,
                                                     scholar=self.var_2)
            qing_zhuo_list.append(THIRTY_EIGHT_ALPHABET[guang_yun_sqlite.get_sheng_nu(word, "聲紐")])
            if self.var_4 == "平上去入":
                sheng_diao_list.append(guang_yun_sqlite.get_sheng_nu(word, "聲調"))
            else:
                sheng_diao = guang_yun_sqlite.get_sheng_nu(word, "聲調")
                if sheng_diao in ["上", "去", "入"]:
                    sheng_diao_list.append("仄")
                else:
                    sheng_diao_list.append(sheng_diao)


        guang_yun_sqlite.close()

        # 查询特定字头、时代、性质和学者的拟音
        #result = phonetic_processor.get_phonetic(headword="人", era=var_0, nature=var_1, scholar=var_2)

        # 输出结果
        #print(result)  # 输出对应的拟音或相关错误信息

        # 关闭连接
        #processor.close()

        #crawler = GetThePage(all_except_first_line)
        #crawler.crawl_words()

    @staticmethod
    def matching(string):
        return bool(re.search(r'.*未找到.*', string))





