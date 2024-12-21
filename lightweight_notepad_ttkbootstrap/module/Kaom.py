import json
import logging
import os
import re
import sqlite3
import time
from io import StringIO

import pandas as pd
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from selenium.webdriver import Chrome, Edge, Firefox
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from function.variables.ProjectPathVariables import RECONSTRUCTIONS, RECONSTRUCTIONS_LIST,RECONSTRUCTIONS_SQLITE


class GetThePage:
    def __init__(self,words,
                 timeout=8,
                 cycle_wait_time=5,max_retries=300,
                 wait_before_typing_time=3,wait_time_before_submitting=3,wait_time_before_switching_windows=3):
        """
            :param cycle_wait_time: 在循环后等待的时间
            :param max_retries: 最大重试次数
            :param wait_before_typing_time and wait_time_before_submitting and wait_time_before_switching_windows: 顾名思义-{用于operator_interface方法中}
        """
        self.words = list(re.sub(r'[^\u4e00-\u9fa5]', '', words))
        self.driver = None
        self.ua = UserAgent()
        self.cycle_wait_time = cycle_wait_time
        self.max_retries = max_retries
        self.wait_before_typing_time = wait_before_typing_time
        self.wait_time_before_submitting = wait_time_before_submitting
        self.wait_time_before_switching_windows = wait_time_before_switching_windows
        self.timeout = timeout


    def init_chrome_driver(self, browser_priority:list=None):
        """初始化浏览器驱动，按照优先顺序尝试启动"""
        if browser_priority is None:
            browser_priority = [0, 1, 2]

        options = {
            'chrome': ChromeOptions(),
            'edge': EdgeOptions(),
            'firefox': FirefoxOptions(),
        }

        # 随机User-Agent
        #user_agent = self.ua.random
        #options['chrome'].add_argument(f"user-agent={user_agent}")
        #options['edge'].add_argument(f"user-agent={user_agent}")
        #options['firefox'].add_argument(f"user-agent={user_agent}")

        # 启用无头模式
        #options['chrome'].add_argument("--headless")
        #options['edge'].add_argument("--headless")
        #options['firefox'].add_argument("--headless")

        # 禁用GPU加速
        #options['chrome'].add_argument("--disable-gpu")
        #options['edge'].add_argument("--disable-gpu")
        #options['firefox'].add_argument("--disable-gpu")

        # 禁用浏览器扩展
        options['chrome'].add_argument("--disable-extensions")
        options['edge'].add_argument("--disable-extensions")
        options['firefox'].add_argument("--disable-extensions")

        # 禁用日志输出
        #options['chrome'].add_argument("--log-level=3")
        #options['edge'].add_argument("--log-level=3")
        #options['firefox'].add_argument("--log-level=3")

        # 浏览器优先级列表
        # 0=Chrome, 1=Edge, 2=Firefox

        for browser in browser_priority:
            try:
                if browser == 0:  # Chrome
                    self.driver = Chrome(service=ChromeService(ChromeDriverManager().install()),
                                         options=options['chrome'])
                    logging.info("Chrome启动成功")
                    return self.driver

                elif browser == 1:  # Edge
                    self.driver = Edge(service=EdgeService(EdgeChromiumDriverManager().install()),
                                       options=options['edge'])
                    logging.info("Edge启动成功")
                    return self.driver

                elif browser == 2:  # Firefox
                    self.driver = Firefox(service=FirefoxService(GeckoDriverManager().install()),
                                          options=options['firefox'])
                    logging.info("Firefox启动成功")
                    return self.driver

            except Exception as e:
                logging.info(f"浏览器启动失败: {e}")
                continue  # 如果当前浏览器启动失败，尝试下一个浏览器

        raise Exception("所有浏览器启动失败")

    def wait_for_element(self, locator):
        """等待元素出现"""
        try:
            element = WebDriverWait(self.driver, self.timeout).until(ec.presence_of_element_located(locator))
            return element
        except Exception as e:
            logging.error(f"等待元素超时: {locator}, 错误: {e}")
            return None

    def handle_frequency_limit(self,wait_time):
        """处理频繁点击的限制提示"""
        page_source = self.driver.page_source
        if "Please click with an interval greater than 3 seconds" in page_source or "請點擊間隔大於3秒" in page_source:
            logging.warning(f"检测到频繁点击限制，等待{wait_time}秒后重试")
            time.sleep(wait_time)  # 等待3.8秒
            return True  # 返回True表示需要重试
        return False

    def frequent_clicks(self,main_window):
        self.driver.close()  # 关闭当前新窗口
        self.driver.switch_to.window(main_window)

    def refresh_url(self,wait_time):
        time.sleep(wait_time)
        self.driver.refresh()
        time.sleep(wait_time)

    def operator_interface(self,word):
        """操作界面"""
        input_box = self.wait_for_element((By.NAME, "word"))
        if not input_box:
            return []
        input_box.clear()

        time.sleep(self.wait_before_typing_time)

        input_box.send_keys(word)
        logging.info(f"输入文字: {word}")

        # 选择下拉框选项
        dropdown = self.driver.find_element(By.NAME, "bianti")
        dropdown.send_keys("no")

        time.sleep(self.wait_time_before_submitting)

        # 提交表单
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        submit_button.click()

        time.sleep(self.wait_time_before_switching_windows)

        # 切换到新窗口
        main_window = self.driver.current_window_handle
        WebDriverWait(self.driver, 10).until(ec.new_window_is_opened([main_window]))
        new_window = [window for window in self.driver.window_handles if window != main_window][0]
        self.driver.switch_to.window(new_window)
        logging.info("切换到新窗口")
        return main_window

    def crawl_word_data(self,word):

        try:
            attempts = 0

            # 访问第一个页面并处理频繁点击限制
            while attempts < self.max_retries:
                self.driver.get("http://www.kaom.net/ny_word.php")
                logging.info(f"访问页面成功: {self.driver.current_url}")
                main_window = self.driver.current_window_handle

                self.wait_for_element((By.TAG_NAME, "div"))

                # 检查是否出现频繁点击限制提示
                if self.handle_frequency_limit(self.cycle_wait_time):
                    attempts += 1
                    logging.warning(f"频繁点击限制提示，重试第 {attempts} 次")
                    if self.driver.current_url == "http://www.kaom.net/ny_word.php":
                        self.refresh_url(self.cycle_wait_time)
                    else:
                        time.sleep(self.cycle_wait_time)
                        self.frequent_clicks(main_window)
                        self.operator_interface(word)
                    continue

                # 输入文字
                main_window = self.operator_interface(word)

                # 检查新页面的频繁点击限制
                retry_count = 0
                while retry_count < self.max_retries:

                    if self.handle_frequency_limit(self.cycle_wait_time):
                        retry_count += 1
                        logging.warning(f"频繁点击限制提示，重试第 {retry_count} 次")
                        time.sleep(self.cycle_wait_time)
                        self.frequent_clicks(main_window)
                        self.operator_interface(word)
                        continue

                    self.wait_for_element((By.TAG_NAME, "table"))

                    # 保存HTML
                    file_name = f"{word}_page.html"
                    file_path = os.path.join(RECONSTRUCTIONS, file_name)
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(str(self.driver.page_source))
                        logging.info(f"页面HTML已保存为: {file_path}")

                    self.frequent_clicks(main_window)
                    logging.info("关闭新窗口并切回主窗口")
                    return []  # 成功保存文件，返回空列表

                logging.error("超过最大重试次数，无法保存文件")
                return []  # 如果达到最大重试次数仍未成功，则返回空列表

        except Exception as e:
            logging.error(f"发生异常: {e}")
            return []

    def crawl_words(self):
        """批量爬取多个词的数据，使用单线程方式"""
        # 初始化驱动
        self.init_chrome_driver([1,0,2])

        # 逐个爬取每个词的数据
        for word in self.words:
            self.crawl_word_data(word)

        # 在所有词处理完成后关闭驱动
        self.driver.quit()

class FileProcessor:
    def __init__(self, folder_on_path, output_path):
        self.folder_on_path = folder_on_path
        self.output_path = output_path

    def get_files_content(self):
        reconstructions_list = []

        for file in os.listdir(self.folder_on_path):
            if file.endswith('.html'):
                with open(os.path.join(self.folder_on_path, file), 'r', encoding='utf-8') as f:
                    # 解析并提取所有 <table> 标签
                    reconstructions_list.extend(
                        str(table) for table in BeautifulSoup(f.read(), 'html.parser').find_all('table')
                    )
        return reconstructions_list

    def save_content(self):
        reconstructions_list = self.get_files_content()
        with open(self.output_path, 'w', encoding='utf-8') as f:
            json.dump(reconstructions_list, f, ensure_ascii=False, indent=4)

        logging.info(f"所有文件内容已保存到 {self.output_path}")
        return reconstructions_list

'''repeal
class HtmlSplitting:
    def __init__(self, html):
        self.Html = html

    @staticmethod#提取学者
    def extract_scholars(text_list):
        return [(match.group(1), match.group(2))
                for item in text_list if (match := re.search(r"(\d+)-([^-\s]+(?:-[^-\s]+)*?)-學者", item))]

    @staticmethod#提取字头
    def extract_zi_heads(text_list):
        return [match.group(1) for item in text_list if (match := re.search(r"([a-zA-Z\u4e00-\u9fa5]+)-字頭", item))]

    @staticmethod#提取 reconstructions 并判断是否以 '?' 结尾
    def extract_reconstruction(text_list):
        return [(1 if match.group(1).endswith('?') else 0, match.group(1))
                for item in text_list if (match := re.search(r"值为：([^：]+)-擬音", item))]

    @staticmethod#提取韵部
    def extract_rhyme(text_list):
        return [
            (1, match.group(1)[:-1]) if match and match.group(1).endswith("？")
            else (0, match.group(1)) if match
            else (0, None)
            for text in text_list
            if (match := re.search(r"值为：([^\-]+)-韻部", text)) is not None
        ]

    @staticmethod#提取类型
    def extract_type(text_list):
        return [m for item in text_list for m in re.findall(r'rowspan属性，值为: (\d+)-([^-\s]+)-[^-\s]+-性質', item)]

    @staticmethod#提取时代
    def extract_era(text_list):
        return [m for item in text_list for m in re.findall(r'rowspan属性，值为: (\d+)-([^-\s]+)-[^-\s]+-時代', item)]

    @staticmethod#解决错误
    def replace_consecutive_zi_head(text_list):
        return [
            item.replace('字頭', '擬音') if '字頭' in item and '字頭' in (text_list[i - 1] if i > 0 else '') else item
            for i, item in enumerate(text_list)
        ]

    def form_acquisition(self):

        textual_information_list = []

        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(self.Html, "html.parser")

        # 查找所有<td>标签
        td_elements = soup.find_all('td')
        logging.info(td_elements)
        # 遍历每个<td>元素，检查是否满足条件
        for td in td_elements:

            text = td.get_text(strip=True)
            if text == "":
                text = 'None'

            # 检查<td>是否包含<u>标签
            u_tag = td.find('u')
            b_tag = td.find('b')
            i_tag = td.find('i')
            rowspan = td.get('rowspan')

            if i_tag and i_tag.get_text(strip=True) == "無擬音":
                textual_information = f"标签含有<i>，且是'無擬音'文本，值为：None-擬音"
                logging.info(textual_information)
                textual_information_list.append(textual_information)
                continue
            elif i_tag:
                continue

            if b_tag:
                if rowspan:
                    if b_tag:
                        textual_information = f"标签含有<b>，并有rowspan属性，值为: {rowspan}-{text}-其不符合要求-時代"
                        logging.info(textual_information)
                        textual_information_list.append(textual_information)
                else:
                    if u_tag:
                        textual_information = f"标签包含<b>，包含<u>，没有rowspan属性，值为：{text}-韻部-不太可靠"
                        logging.info(textual_information)
                        textual_information_list.append(textual_information)
                    else:
                        textual_information = f"标签包含<b>，非含<u>，没有rowspan属性，值为：{text}-擬音"
                        logging.info(textual_information)
                        textual_information_list.append(textual_information)
            else:
                if u_tag:
                    if rowspan:
                        textual_information = f"标签包含<u>，并有rowspan属性，值为: {rowspan}-{text}-學者"
                        logging.info(textual_information)
                        textual_information_list.append(textual_information)
                    else:
                        textual_information = f"标签包含<u>，没有rowspan属性，值为：{text}-韻部"
                        logging.info(textual_information)
                        textual_information_list.append(textual_information)
                else:
                    if rowspan:
                        textual_information = f"标签没有<u>，但有rowspan属性，值为: {rowspan}-{text}-其不符合要求-性質"
                        logging.info(textual_information)
                        textual_information_list.append(textual_information)
                    else:
                        textual_information = f"标签没有<u>，没有rowspan属性，值为：{text}-字頭"
                        logging.info(textual_information)
                        textual_information_list.append(textual_information)

        corrected_textual_information_list = self.replace_consecutive_zi_head(textual_information_list)

        scholars = self.extract_scholars(corrected_textual_information_list)
        zi_head_list = self.extract_zi_heads(corrected_textual_information_list)
        reconstructions = self.extract_reconstruction(corrected_textual_information_list)
        rhyme_list = self.extract_rhyme(corrected_textual_information_list)
        type_list = self.extract_type(corrected_textual_information_list)
        era_list = self.extract_era(corrected_textual_information_list)

        logging.info(f"Scholars:{scholars}")
        # logging.info("Scholars len:", len(scholars))
        logging.info(f"Zi Head List:{zi_head_list}")
        # logging.info("Zi Head List len", len(zi_head_list))
        logging.info(f"reconstructions List:{reconstructions}")
        # logging.info("reconstructions List len:", len(reconstructions))
        logging.info(f"Rhyme:{rhyme_list}")
        logging.info(f"Type:{type_list}")
        logging.info(f"Era:{era_list}")

        return scholars,[item for item in set(zi_head_list) if item != "None"],reconstructions,rhyme_list,type_list,era_list
'''

'''repeal
class StandardizeHtmlIntoDict:
    def __init__(self,htlm,scholars,zi_head_list,reconstructions,rhyme_list,type_list,era_list):
        """
        :param htlm: 网页
        :param scholars: 学者列表
        :param zi_head_list: 字头列表
        :param reconstructions: 拟音列表
        :param rhyme_list: 韵部；
        :param type_list: 类型列表
        :param era_list: 时期列表
        """
        self.html = htlm
        self.scholars = scholars
        self.zi_head_list = zi_head_list
        self.reconstructions = reconstructions
        self.rhyme_list = rhyme_list
        self.type_list = type_list
        self.era_list = era_list
        #self.era_dict = {int(num): name for num, name in era_list}
        self.scholar_reconstructions_dict = {}
        self.reconstructions_index = 0

    def return_dict(self,new_dict,zhitou):
        for era_num, era in self.era_list:
            era_num = int(era_num)
            for scholar_num, scholar in self.scholars:
                scholar_num = int(scholar_num)

                while self.reconstructions_index < era_num:

                    save_dict = new_dict[zhitou][era]["構擬"][scholar]["擬音"] = []

                    self.reconstructions_index += 1

    @staticmethod
    def replace_zhitou(new_zhitou):
        """
        替换字头为新的字
        :param new_zhitou: 新的字头
        :return: 更新后的字典
        """
        if "字頭" in ROOCHSCMC:
            # 获取原始的子字典
            original_data = ROOCHSCMC["字頭"]

            # 用新的字头替换字头
            ROOCHSCMC[new_zhitou] = original_data

            # 删除旧的字头
            del ROOCHSCMC["字頭"]

        return ROOCHSCMC

    # 示例：替换字头为"新字頭"
    ROOCHSCMC_updated = replace_zhitou("")

    # 查看更新后的字典
    print(ROOCHSCMC_updated)
'''

class HTMLToSQLite:
    def __init__(self, db_name='reconstructions_list.sqlite'):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self._initialize_database()

    def _initialize_database(self):
        """初始化数据库表"""
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS headwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT UNIQUE
        )''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS eras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            era TEXT UNIQUE
        )''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS natures (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nature TEXT UNIQUE
        )''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS scholars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            scholar TEXT UNIQUE
        )''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS phonetics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            headword_id INTEGER,
            era_id INTEGER,
            nature_id INTEGER,
            scholar_id INTEGER,
            phonetic TEXT,
            FOREIGN KEY (headword_id) REFERENCES headwords(id),
            FOREIGN KEY (era_id) REFERENCES eras(id),
            FOREIGN KEY (nature_id) REFERENCES natures(id),
            FOREIGN KEY (scholar_id) REFERENCES scholars(id)
        )''')

    def _parse_html(self, html_code):
        """解析 HTML 表格"""
        soup = BeautifulSoup(html_code, 'html.parser')
        html_string = str(soup.find('table'))
        html_file = StringIO(html_string)
        return pd.read_html(html_file)[0]

    def _process_row(self, row):
        """处理每一行数据"""
        headword = row['字頭'] if pd.notna(row['字頭']) else None
        if headword is None:
            print("字頭為 None，跳過此行")
            return  # 如果字頭為 None，跳過此行

        era = row['時代'] if pd.notna(row['時代']) else None
        nature = row['性質'] if pd.notna(row['性質']) else None
        scholar = row['學者'] if pd.notna(row['學者']) else None
        phonetic = row['擬音[經整理]'] if pd.notna(row['擬音[經整理]']) else None
        rhyme = row['韻部'] if pd.notna(row['韻部']) else None

        # 如果擬音[經整理]是“無擬音”，使用韻部
        if phonetic == "無擬音":
            phonetic = rhyme

        # 插入字頭，避免重复
        print(f"正在插入字頭: {headword}")
        self.cursor.execute("INSERT OR IGNORE INTO headwords (word) VALUES (?)", (headword,))
        print(f"插入字頭成功或已存在: {headword}")

        # 查询 headword_id
        print(f"正在查询字頭 ID: {headword}")
        self.cursor.execute("SELECT id FROM headwords WHERE word = ?", (headword,))
        headword_id = self.cursor.fetchone()
        if headword_id is None:
            print(f"字頭 '{headword}' 在数据库中未找到，正在插入...")
            self.cursor.execute("INSERT INTO headwords (word) VALUES (?)", (headword,))
            print(f"重新插入字頭: {headword}")
            self.cursor.execute("SELECT id FROM headwords WHERE word = ?", (headword,))
            headword_id = self.cursor.fetchone()

        if headword_id is None:
            raise ValueError(f"字頭 '{headword}' 未能找到其对应的 ID")

        headword_id = headword_id[0]
        print(f"字頭 ID: {headword_id}")

        # 插入和查询 era
        print(f"正在插入時代: {era}")
        self.cursor.execute("INSERT OR IGNORE INTO eras (era) VALUES (?)", (era,))
        self.cursor.execute("SELECT id FROM eras WHERE era = ?", (era,))
        era_id = self.cursor.fetchone()
        if era_id is None:
            print(f"時代 '{era}' 在数据库中未找到，正在插入...")
            self.cursor.execute("INSERT INTO eras (era) VALUES (?)", (era,))
            self.cursor.execute("SELECT id FROM eras WHERE era = ?", (era,))
            era_id = self.cursor.fetchone()
        era_id = era_id[0]
        print(f"時代 ID: {era_id}")

        # 插入和查询 nature
        print(f"正在插入性質: {nature}")
        self.cursor.execute("INSERT OR IGNORE INTO natures (nature) VALUES (?)", (nature,))
        self.cursor.execute("SELECT id FROM natures WHERE nature = ?", (nature,))
        nature_id = self.cursor.fetchone()
        if nature_id is None:
            print(f"性質 '{nature}' 在数据库中未找到，正在插入...")
            self.cursor.execute("INSERT INTO natures (nature) VALUES (?)", (nature,))
            self.cursor.execute("SELECT id FROM natures WHERE nature = ?", (nature,))
            nature_id = self.cursor.fetchone()
        nature_id = nature_id[0]
        print(f"性質 ID: {nature_id}")

        # 插入和查询 scholar
        print(f"正在插入學者: {scholar}")
        self.cursor.execute("INSERT OR IGNORE INTO scholars (scholar) VALUES (?)", (scholar,))
        self.cursor.execute("SELECT id FROM scholars WHERE scholar = ?", (scholar,))
        scholar_id = self.cursor.fetchone()
        if scholar_id is None:
            print(f"學者 '{scholar}' 在数据库中未找到，正在插入...")
            self.cursor.execute("INSERT INTO scholars (scholar) VALUES (?)", (scholar,))
            self.cursor.execute("SELECT id FROM scholars WHERE scholar = ?", (scholar,))
            scholar_id = self.cursor.fetchone()
        scholar_id = scholar_id[0]
        print(f"學者 ID: {scholar_id}")

        # 插入 phonetic
        print(f"正在插入擬音: {phonetic}")
        self.cursor.execute('''
        INSERT INTO phonetics (headword_id, era_id, nature_id, scholar_id, phonetic)
        VALUES (?, ?, ?, ?, ?)''', (headword_id, era_id, nature_id, scholar_id, phonetic))
        print(f"擬音插入成功: {phonetic}")

    def process_html(self, html_code):
        """处理单个 HTML 文件"""
        df = self._parse_html(html_code)
        for _, row in df.iterrows():
            self._process_row(row)
        self.conn.commit()

    def process_html_files(self, html_files):
        """处理多个 HTML 文件"""
        for html_code in html_files:
            self.process_html(html_code)

    def close(self):
        """关闭数据库连接"""
        self.conn.commit()
        self.conn.close()
        print(f"数据已成功保存到 {self.db_name} 数据库。")

class PhoneticDatabaseProcessor:
    def __init__(self, db_path):
        # 连接到SQLite数据库
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def get_phonetic(self, headword, era, nature, scholar):
        """根据输入的字頭、時代、性質和學者返回擬音[經整理]"""
        # 查询字頭的id
        self.cursor.execute("SELECT id FROM headwords WHERE word = ?", (headword,))
        headword_id = self.cursor.fetchone()
        if headword_id is None:
            return f"字頭 '{headword}' 未找到"
        headword_id = headword_id[0]

        # 查询時代的id
        self.cursor.execute("SELECT id FROM eras WHERE era = ?", (era,))
        era_id = self.cursor.fetchone()
        if era_id is None:
            return f"時代 '{era}' 未找到"
        era_id = era_id[0]

        # 查询性質的id
        self.cursor.execute("SELECT id FROM natures WHERE nature = ?", (nature,))
        nature_id = self.cursor.fetchone()
        if nature_id is None:
            return f"性質 '{nature}' 未找到"
        nature_id = nature_id[0]

        # 查询學者的id
        self.cursor.execute("SELECT id FROM scholars WHERE scholar = ?", (scholar,))
        scholar_id = self.cursor.fetchone()
        if scholar_id is None:
            return f"學者 '{scholar}' 未找到"
        scholar_id = scholar_id[0]

        # 使用已找到的id查询擬音[經整理]
        self.cursor.execute("""
        SELECT phonetic 
        FROM phonetics 
        WHERE headword_id = ? AND era_id = ? AND nature_id = ? AND scholar_id = ?""",
                            (headword_id, era_id, nature_id, scholar_id))
        phonetic = self.cursor.fetchone()

        if phonetic:
            return phonetic[0]
        else:
            return "未找到匹配的擬音[經整理]"

    def close(self):
        """关闭数据库连接"""
        self.conn.close()

def main():
    input_string = "四廂人寒噤，要眇如啼眼。"

    ## 使用正则表达式去除非汉字字符
    #filtered_string = re.sub(r'[^\u4e00-\u9fa5]', '', input_string)
    # 转换为字符列表
    #char_list = list(filtered_string)

    crawler = GetThePage(input_string)
    crawler.crawl_words()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    #main()

    #print(RECONSTRUCTIONS_SQLITE)

    html_list = FileProcessor(RECONSTRUCTIONS,RECONSTRUCTIONS_LIST).save_content()

    processor = HTMLToSQLite(RECONSTRUCTIONS_SQLITE)

    processor.process_html_files(html_list)

    processor.close()

    '''
    for i in processor:
        get_scholars,get_zi_head_list,get_reconstructions,get_rhyme,get_type,get_era = HtmlSplitting(i).form_acquisition()
        print(get_scholars)
        print(get_zi_head_list)
        print(get_reconstructions)
        print(get_rhyme)
        print(get_type)
        print(get_era)
    '''


