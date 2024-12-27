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
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from function.variables.ProjectPathVariables import RECONSTRUCTIONS, RECONSTRUCTIONS_VOWEL, \
    RECONSTRUCTIONS_VOWEL_RECONSTRUCTIONS_LIST, RECONSTRUCTIONS_VOWEL_RECONSTRUCTIONS_LIST_PATH, RECONSTRUCTIONS_SQLITE

class GetThePage:
    def __init__(self,words,text_widget,
                 timeout=8,
                 cycle_wait_time=5,max_retries=300,
                 wait_before_typing_time=3,wait_time_before_submitting=3,wait_time_before_switching_windows=3):
        """
            :param cycle_wait_time: 在循环后等待的时间
            :param max_retries: 最大重试次数
            :param wait_before_typing_time and wait_time_before_submitting and wait_time_before_switching_windows: 顾名思义-{用于operator_interface方法中}
        """
        self.words = list(re.sub(r'[^\u4e00-\u9fa5]', '', words))
        self.text_widget = text_widget
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
        #['chrome'].add_argument("--headless")
        options['edge'].add_argument("--headless")
        options['firefox'].add_argument("--headless")

        # 禁用GPU加速
        options['chrome'].add_argument("--disable-gpu")
        options['edge'].add_argument("--disable-gpu")
        options['firefox'].add_argument("--disable-gpu")

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
                    self.text_widget.insert("end", "程序启动成功\n")
                    return self.driver

                elif browser == 1:  # Edge
                    self.driver = Edge(service=EdgeService(EdgeChromiumDriverManager().install()),
                                       options=options['edge'])
                    self.text_widget.insert("end","程序启动成功\n")
                    return self.driver

                elif browser == 2:  # Firefox
                    self.driver = Firefox(service=FirefoxService(GeckoDriverManager().install()),
                                          options=options['firefox'])
                    self.text_widget.insert("end","程序启动成功\n")
                    return self.driver

            except Exception as e:
                self.text_widget.insert("end",f"启动失败-建议检查网络设置: {e}\n")
                continue  # 如果当前浏览器启动失败，尝试下一个浏览器

        raise Exception("所有浏览器启动失败")

    def wait_for_element(self, locator):
        """等待元素出现"""
        try:
            element = WebDriverWait(self.driver, self.timeout).until(ec.presence_of_element_located(locator))
            return element
        except Exception as e:
            self.text_widget.insert("end", f"等待元素超时: {locator}, 错误: {e}\n")
            return None

    def handle_frequency_limit(self,wait_time):
        """处理频繁点击的限制提示"""
        page_source = self.driver.page_source
        if "Please click with an interval greater than 3 seconds" in page_source or "請點擊間隔大於3秒" in page_source:
            self.text_widget.insert("end", f"检测到频繁点击限制，等待{wait_time}秒后重试\n")
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
        self.text_widget.insert("end",f"输入文字: {word}\n")

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
        self.text_widget.insert("end","切换到新窗口\n")
        return main_window

    def crawl_word_data(self,word):

        try:
            attempts = 0

            # 访问第一个页面并处理频繁点击限制
            while attempts < self.max_retries:
                self.driver.get("http://www.kaom.net/ny_word.php")
                self.text_widget.insert("end",f"访问成功: {self.driver.current_url}\n")
                main_window = self.driver.current_window_handle

                self.wait_for_element((By.TAG_NAME, "div"))

                # 检查是否出现频繁点击限制提示
                if self.handle_frequency_limit(self.cycle_wait_time):
                    attempts += 1
                    self.text_widget.insert("end", f"频繁点击限制提示，重试第 {attempts} 次\n")
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
                        self.text_widget.insert("end", f"频繁点击限制提示，重试第 {attempts} 次\n")
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
                        self.text_widget.insert("end", f"页面HTML已保存为: {file_path}\n")

                    self.frequent_clicks(main_window)
                    self.text_widget.insert("end","关闭新窗口并切回主窗口\n")
                    return []  # 成功保存文件，返回空列表

                self.text_widget.insert("end", "超过最大重试次数，无法保存文件\n")
                return []  # 如果达到最大重试次数仍未成功，则返回空列表

        except Exception as e:
            self.text_widget.insert("end", f"发生异常: {e}\n")
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

class SyllableSplitting(GetThePage):
    def __init__(self,text_widget,timeout=8, cycle_wait_time=5, max_retries=300,
                 wait_before_typing_time=3, wait_time_before_submitting=3,
                 wait_time_before_switching_windows=3,
                 syllabic_splits=5, words=None):
        """
        初始化SyllableSplitting类，添加了新参数syllabic_splits
        """
        # 如果没有传入 words，给一个默认值，或者在这里处理
        if words is None:
            words = ""  # 或者其他适合的默认值

        # 调用父类的构造函数，确保父类的初始化
        super().__init__(words, timeout, cycle_wait_time, max_retries,
                         wait_before_typing_time, wait_time_before_submitting,
                         wait_time_before_switching_windows)

        self.syllab_splits = syllabic_splits
        self.text_widget = text_widget

    def operator_interface(self,word):
        """操作界面"""
        input_box = self.wait_for_element((By.NAME, "text"))
        if not input_box:
            return []
        input_box.clear()

        time.sleep(self.wait_before_typing_time)

        for idx, item in enumerate(word):
            input_box.send_keys(item)
            # 判断是否是最后一个元素，最后一个元素不添加换行符
            if idx < len(word) - 1:
                input_box.send_keys("\n")  # 添加换行符，使每个元素为一行

        # 定位到第一个下拉框
        dropdown = self.driver.find_element(By.NAME, "mode")

        # 创建 Select 对象
        select = Select(dropdown)

        # 选择选项（3、4、5、7）
        select.select_by_value(str(self.syllab_splits))

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
        self.text_widget.insert("end","切换到新窗口\n")
        return main_window

    def split_syllables(self,word):
        try:
            attempts = 0

            # 访问第一个页面并处理频繁点击限制
            while attempts < self.max_retries:
                self.driver.get("http://www.kaom.net/font_ipa_qiefen.php")
                self.text_widget.insert("end",f"访问成功: {self.driver.current_url}\n")
                main_window = self.driver.current_window_handle

                self.wait_for_element((By.TAG_NAME, "div"))

                # 检查是否出现频繁点击限制提示
                if self.handle_frequency_limit(self.cycle_wait_time):
                    attempts += 1
                    self.text_widget.insert("end", f"频繁点击限制提示，重试第 {attempts} 次\n")
                    if self.driver.current_url == "http://www.kaom.net/font_ipa_qiefen.php":
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
                        self.text_widget.insert("end", f"频繁点击限制提示，重试第 {attempts} 次\n")
                        time.sleep(self.cycle_wait_time)
                        self.frequent_clicks(main_window)
                        self.operator_interface(word)
                        continue

                    self.wait_for_element((By.TAG_NAME, "table"))

                    # 保存HTML
                    file_name = f"p_page.html"
                    file_path = os.path.join(RECONSTRUCTIONS_VOWEL, file_name)
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(str(self.driver.page_source))
                        self.text_widget.insert("end", f"页面HTML已保存为: {file_path}\n")

                    self.frequent_clicks(main_window)
                    self.text_widget.insert("end","关闭新窗口并切回主窗口\n")
                    return []  # 成功保存文件，返回空列表

                self.text_widget.insert("end", "超过最大重试次数，无法保存文件\n")
                return []  # 如果达到最大重试次数仍未成功，则返回空列表

        except Exception as e:
            self.text_widget.insert("end", f"发生异常: {e}\n")
            return []

    def crawl_words_initiate(self,word):
        """批量爬取多个词的数据，使用单线程方式"""
        # 初始化驱动
        self.init_chrome_driver([1,0,2])


        self.split_syllables(word)

        # 在所有词处理完成后关闭驱动
        self.driver.quit()

class FileProcessor:
    def __init__(self,text_widget,folder_on_path, output_path):
        self.folder_on_path = folder_on_path
        self.output_path = output_path
        self.text_widget = text_widget

    def get_files_content(self):
        reconstructions_list = []
        self.text_widget.insert("end",f"开始提取中\n")
        for file in os.listdir(self.folder_on_path):
            if file.endswith('.html'):
                with open(os.path.join(self.folder_on_path, file), 'r', encoding='utf-8') as f:
                    # 解析并提取所有 <table> 标签
                    reconstructions_list.extend(
                        str(table) for table in BeautifulSoup(f.read(), 'html.parser').find_all('table')
                    )
        self.text_widget.insert("end",f"提取结束\n")
        return reconstructions_list

    def save_content(self):
        self.text_widget.insert("end",f"所有文件内容正在保存到 {self.output_path}\n")
        reconstructions_list = self.get_files_content()
        with open(self.output_path, 'w', encoding='utf-8') as f:
            json.dump(reconstructions_list, f, ensure_ascii=False, indent=4)

        self.text_widget.insert("end",f"所有文件内容已保存到 {self.output_path}\n")
        return reconstructions_list

class HtmlToSqlite:
    def __init__(self,text_widget,sq_file='reconstructions_list.sqlite'):
        self.text_widget = text_widget
        self.sq_file = sq_file
        self.conn = sqlite3.connect(self.sq_file, check_same_thread=False)# 防止多线程时的锁定
        #self.conn.execute('PRAGMA busy_timeout=100000;')
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
            UNIQUE(headword_id, era_id, nature_id, scholar_id),
            FOREIGN KEY (headword_id) REFERENCES headwords(id),
            FOREIGN KEY (era_id) REFERENCES eras(id),
            FOREIGN KEY (nature_id) REFERENCES natures(id),
            FOREIGN KEY (scholar_id) REFERENCES scholars(id)
        )''')

    @staticmethod
    def _parse_html(html_code):
        """解析 HTML 表格"""
        soup = BeautifulSoup(html_code, 'html.parser')
        html_string = str(soup.find('table'))
        html_file = StringIO(html_string)
        return pd.read_html(html_file)[0]

    def _process_row(self, row):
        """处理每一行数据"""
        headword = row['字頭'] if pd.notna(row['字頭']) else None
        if headword is None:
            #self.text_widget.insert("end","字頭為 None，跳過此行\n")
            return

        era = row['時代'] if pd.notna(row['時代']) else None
        nature = row['性質'] if pd.notna(row['性質']) else None
        scholar = row['學者'] if pd.notna(row['學者']) else None
        phonetic = row['擬音[經整理]'] if pd.notna(row['擬音[經整理]']) else None
        rhyme = row['韻部'] if pd.notna(row['韻部']) else None

        # 如果擬音[經整理]是“無擬音”，使用韻部
        if phonetic == "無擬音":
            phonetic = rhyme

        self.cursor.execute("INSERT OR IGNORE INTO headwords (word) VALUES (?)", (headword,))
        self.cursor.execute("SELECT id FROM headwords WHERE word = ?", (headword,))
        headword_id = self.cursor.fetchone()[0]

        # 插入和查询 era
        self.cursor.execute("INSERT OR IGNORE INTO eras (era) VALUES (?)", (era,))
        self.cursor.execute("SELECT id FROM eras WHERE era = ?", (era,))
        era_id = self.cursor.fetchone()[0]

        # 插入和查询 nature
        self.cursor.execute("INSERT OR IGNORE INTO natures (nature) VALUES (?)", (nature,))
        self.cursor.execute("SELECT id FROM natures WHERE nature = ?", (nature,))
        nature_id = self.cursor.fetchone()[0]

        # 插入和查询 scholar
        self.cursor.execute("INSERT OR IGNORE INTO scholars (scholar) VALUES (?)", (scholar,))
        self.cursor.execute("SELECT id FROM scholars WHERE scholar = ?", (scholar,))
        scholar_id = self.cursor.fetchone()[0]

        # 检查是否已存在相同组合的记录
        self.cursor.execute(''' 
        SELECT phonetic FROM phonetics
        WHERE headword_id = ? AND era_id = ? AND nature_id = ? AND scholar_id = ?''',
                            (headword_id, era_id, nature_id, scholar_id))

        existing_phonetic = self.cursor.fetchone()

        if existing_phonetic:
            return

        self.cursor.execute(''' 
        INSERT INTO phonetics (headword_id, era_id, nature_id, scholar_id, phonetic)
        VALUES (?, ?, ?, ?, ?)''', (headword_id, era_id, nature_id, scholar_id, phonetic))

    def process_html(self, html_code):
        """处理单个 HTML 文件"""
        df = self._parse_html(html_code)
        for _, row in df.iterrows():
            self._process_row(row)

    def process_html_files(self, html_files):
        for html_code in html_files:
            self.process_html(html_code)
        self.conn.commit()  # 提交所有操作
        self.text_widget.insert("end","数据提交数据库成功\n")

    def close(self):
        """关闭数据库连接"""
        self.conn.commit()  # 确保所有数据已提交
        self.conn.close()
        self.text_widget.insert("end","关闭数据库\n")

class SyllableHtmlToSqlite:
    def __init__(self, html_contents, column_names, db_name='table_data.sqlite', table_name='my_table'):
        """初始化类，提供 HTML 内容列表、列名列表、SQLite 数据库名称和表名"""
        self.html_contents = html_contents  # html_contents 是一个 HTML 内容列表
        self.column_names = column_names  # 用户提供的列名列表
        self.db_name = db_name
        self.table_name = table_name
        self.rows = []

    def parse_html(self, html_content):
        """解析 HTML 内容，提取表格数据，跳过第一列"""
        soup = BeautifulSoup(html_content, 'html.parser')

        # 获取表格中的数据
        for row in soup.find_all('tr')[1:]:  # 跳过表头
            cells = row.find_all('td')[1:]  # 跳过第一列
            row_data = [cell.get_text().strip() for cell in cells]
            self.rows.append(row_data)

    def create_table(self):
        """创建 SQLite 表格，列名由用户提供"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # 根据用户提供的列名创建 CREATE TABLE 查询
        create_table_query = f"CREATE TABLE IF NOT EXISTS {self.table_name} ("
        create_table_query += ", ".join([f'"{col}" TEXT' for col in self.column_names])
        create_table_query += ")"

        cursor.execute(create_table_query)
        conn.commit()
        conn.close()

    def insert_data(self):
        """插入数据到 SQLite 表中，如果数据已经存在，则不插入"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # 动态生成插入语句
        insert_query = f"INSERT INTO {self.table_name} ({', '.join(self.column_names)}) VALUES ({', '.join(['?' for _ in self.column_names])})"

        # 遍历每一行数据，检查是否已经存在相同数据
        for row_data in self.rows:
            # 构建查询语句来检查是否已经存在
            check_query = f"SELECT 1 FROM {self.table_name} WHERE " + " AND ".join(
                [f'"{col}" = ?' for col in self.column_names])
            cursor.execute(check_query, row_data)

            # 如果没有找到相同的行，则插入该行
            if cursor.fetchone() is None:
                cursor.execute(insert_query, row_data)

        # 提交更改并关闭连接
        conn.commit()
        conn.close()

    def convert(self):
        """将多个 HTML 内容转换为 SQLite 数据库"""
        # 创建数据库表
        self.create_table()

        # 处理每个 HTML 内容
        for html_content in self.html_contents:
            self.rows = []  # 每个 HTML 文件对应一组数据
            self.parse_html(html_content)
            self.insert_data()

    def get_column_data(self, column_name):
        """根据列名提取该列的数据"""
        if column_name not in self.column_names:
            raise ValueError(f"列名 '{column_name}' 不在提供的列名列表中。")

        column_index = self.column_names.index(column_name)  # 获取该列的索引
        column_data = [row[column_index] for row in self.rows]  # 提取该列的数据
        return column_data

class PhoneticDatabaseProcessor:
    def __init__(self, db_path):
        # 连接到SQLite数据库
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
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
        phonetic = self.cursor.fetchall()

        # 用来存储唯一的元素
        unique_phonetic = []
        seen = set()

        # 遍历phonetic，保留不重复的元素
        for item in phonetic:
            # 提取元组中的第一个元素
            item_value = item[0] if isinstance(item, tuple) else item

            if item_value not in seen:
                unique_phonetic.append(item_value)
                seen.add(item_value)

        # 判断去重后的结果
        if not unique_phonetic:
            return "未找到匹配的擬音[經整理]"  # 如果为空，返回相应提示
        elif len(unique_phonetic) == 1:
            return unique_phonetic[0]  # 返回单个元素
        else:
            return unique_phonetic  # 返回列表

    def close(self):
        """关闭数据库连接"""
        self.cursor.close()
        self.conn.close()

class CsvImportDatabase:
    def __init__(self, csv_file,table_name, sq_file='reconstructions_list.sqlite'):
        print(f"数据从 {csv_file} 开始添加到 {sq_file} 数据库")
        df = pd.read_csv(csv_file, encoding='utf-8', low_memory=False)
        conn = sqlite3.connect(sq_file)
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        conn.close()
        print(f"数据从 {csv_file} 成功添加到 {sq_file} 数据库")

class TabularDatabaseExtraction:
    def __init__(self,text_widget,db_file):
        """
        初始化数据库连接。

        :param db_file: SQLite数据库文件路径
        """
        self.text_widget = text_widget
        self.db_file = db_file
        self.conn = None
        self.cursor = None

    def connect(self):
        """连接到SQLite数据库。"""
        try:
            self.conn = sqlite3.connect(self.db_file, check_same_thread=False)
            self.cursor = self.conn.cursor()
            self.text_widget.insert("end","数据库连接成功\n")
        except sqlite3.Error as e:
            self.text_widget.insert("end",f"数据库连接失败: {e}\n")

    def close(self):
        """关闭数据库连接。"""
        self.cursor.close()
        self.conn.close()
        self.text_widget.insert("end","数据库连接已关闭\n")

    def get_sheng_nu(self, word_input,table,query,column="廣韻字頭_覈校後"):
        """
        根据字头查询对应的声纽。

        :param column: 字头列
        :param table: 需要查询的表
        :param query: 需要查询的列名
        :param word_input: 传入的字头（如“這”）
        :return: 查询结果，若有匹配则返回，否则返回 None。
        """
        try:
            # 执行查询
            self.cursor.execute(f"SELECT {query} FROM {table} WHERE {column} = ?", (word_input,))
            # 获取单条结果
            result = self.cursor.fetchone()
            if result:
                return result[0]  # 返回第一列的值（声纽）
            else:
                return None  # 如果没有找到匹配的记录，返回 None
        except sqlite3.Error as e:
            self.text_widget.insert("end",f"查询失败: {e}-{word_input}")
            return None

def main():
    input_string = "这。"

    ## 使用正则表达式去除非汉字字符
    #filtered_string = re.sub(r'[^\u4e00-\u9fa5]', '', input_string)
    # 转换为字符列表
    #char_list = list(filtered_string)

    crawler = GetThePage(input_string)
    crawler.crawl_words()

if __name__ == "__main__":
    #extract_the_phenotype_sqlite = TabularDatabaseExtraction(RECONSTRUCTIONS_SQLITE)
    #extract_the_phenotype_sqlite.connect()
    phonetic_processor = PhoneticDatabaseProcessor(db_path=RECONSTRUCTIONS_SQLITE)
    a = []
    for word in ['舊', '時', '逐', '日', '子', '曾', '見', '會', '稽', '王', '屈', '身', '成', '忠', '客', '葵', '傾', '晚', '霞',
     '黃', '末', '路', '廢', '碧', '血', '徒', '聽', '寒', '聲', '長', '姑', '息', '秋', '瑩', '遠', '反', '側', '見',
     '流', '光', '可', '憐', '夜', '色', '晚', '厭', '厭', '向', '太', '陽']:
        result = phonetic_processor.get_phonetic(headword=word, era="中古音", nature="構擬",
                                                 scholar="王力")
        #self.text_widget.insert(extract_the_phenotype_sqlite.get_sheng_nu(word, "guang_yun", "韻部_調整後"))

    #extract_the_phenotype_sqlite = TabularDatabaseExtraction(RECONSTRUCTIONS_SQLITE)
    #extract_the_phenotype_sqlite.connect()

    #self.text_widget.insert(type(extract_the_phenotype_sqlite.get_sheng_nu("pə̯u①", "cut_the_voicing", "介音")))
    #self.text_widget.insert(extract_the_phenotype_sqlite.get_sheng_nu("pə̯u①", "cut_the_voicing", "介音"))
    '''
    crawler = SyllableSplitting()
    crawler.crawl_words_initiate([
        "pə̯u①",
        "kŋ̍②",
        "tɕiãŋ③",
        "fv̩④",
        "ka̠k⑤",
        "tɯə⑥",
        "pə̯u12",
        "kŋ̍33",
        "tɕiãŋ214",
        "fv̩45",
        "ka̠k2",
        "tɯə̯22"
    ])
    

    html_list = FileProcessor(RECONSTRUCTIONS_VOWEL, RECONSTRUCTIONS_VOWEL_RECONSTRUCTIONS_LIST_PATH).save_content()

    converter = SyllableHtmlToSqlite(html_list,["序號","字表","聲母","介音","元音","韻尾","聲調","韻母","聲韻"],RECONSTRUCTIONS_SQLITE,"cut_the_voicing")
    converter.convert()
    '''

    #self.text_widget.insert(HtmlSplitting("<table><caption>因電子內容常有差錯、不能忠實反映作者原成果、嚴謹研究請查閱原著</caption><tbody><tr><th class=\"red\" style=\"width: 80px\">時代</th><th style=\"width: 38px\">性質</th><th style=\"width: 160px\">學者</th><th style=\"width: 38px;\">字頭</th><th style=\"width: 100px\">擬音[經整理]</th><th style=\"width: 100px\">擬音[原材料]</th><th style=\"width: 68px\">韻部</th><th>原表其他信息</th><th style=\"width: 60px\">出處</th><th style=\"width: 20px\">序</th></tr><tr><td rowspan=\"16\"><b>上古音</b></td><td rowspan=\"16\">構擬</td><td rowspan=\"1\"><u><a href=\"http://www.kaom.net/ny_x.php?name=gaobenhan\">高本漢</a></u></td><td>人</td><td><b>ȵîĕn</b></td><td><i>ȵîĕn</i></td><td><u>07部 真</u> <b style=\"background: orangered;color: #fff;padding: 0px 1px\">?</b></td><td><i></i></td><td><i></i></td><td rowspan=\"1\"><i>1</i></td></tr><tr><td rowspan=\"1\" style=\"background: #f8f8f8\"><u><a href=\"http://www.kaom.net/ny_x.php?name=dongtonghe\">董同龢</a></u></td><td style=\"background: #f8f8f8\">人</td><td style=\"background: #f8f8f8\"><b>ȵîen</b></td><td style=\"background: #f8f8f8\"><i>ȵjen</i></td><td style=\"background: #f8f8f8\"><u>真</u></td><td style=\"background: #f8f8f8\"><i></i></td><td style=\"background: #f8f8f8\"><i></i></td><td rowspan=\"1\" style=\"background: #f8f8f8\"><i>2</i></td></tr><tr><td rowspan=\"1\"><u><a href=\"http://www.kaom.net/ny_x.php?name=wangli\">王力體系</a></u></td><td>人</td><td><b>ȵĭen</b></td><td><i>ȵĭen</i></td><td><u>真</u></td><td><i></i></td><td><i></i></td><td rowspan=\"1\"><i>3</i></td></tr><tr><td rowspan=\"1\" style=\"background: #f8f8f8\"><u><a href=\"http://www.kaom.net/ny_x.php?name=lifanggui\">李方桂</a></u></td><td style=\"background: #f8f8f8\">人</td><td style=\"background: #f8f8f8\"><b>njin</b></td><td style=\"background: #f8f8f8\"><i>njin</i></td><td style=\"background: #f8f8f8\"><u>真</u></td><td style=\"background: #f8f8f8\"><i></i></td><td style=\"background: #f8f8f8\"><i></i></td><td rowspan=\"1\" style=\"background: #f8f8f8\"><i>4</i></td></tr><tr><td rowspan=\"1\"><u><a href=\"http://www.kaom.net/ny_x.php?name=zhoufagao\">周法高</a></u></td><td>人</td><td><b>njien</b></td><td><i>njien</i></td><td><u>真</u></td><td><i></i></td><td><i></i></td><td rowspan=\"1\"><i>5</i></td></tr><tr><td rowspan=\"1\" style=\"background: #f8f8f8\"><u><a href=\"http://www.kaom.net/ny_x.php?name=sita_a\">斯塔羅斯金①·上古前期</a></u></td><td style=\"background: #f8f8f8\">人</td><td style=\"background: #f8f8f8\"><b>nin</b></td><td style=\"background: #f8f8f8\"><i>nin</i></td><td style=\"background: #f8f8f8\"><u>真1</u> <b style=\"background: orangered;color: #fff;padding: 0px 1px\">?</b></td><td style=\"background: #f8f8f8\"><i>human being, person, man; other persons, others; a person, someone</i></td><td style=\"background: #f8f8f8\"><i><a href=\"https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\china\\bigchina&amp;root=config&amp;morpho=0\">巴別塔</a></i></td><td rowspan=\"1\" style=\"background: #f8f8f8\"><i>6</i></td></tr><tr><td rowspan=\"1\"><u><a href=\"http://www.kaom.net/ny_x.php?name=sita_b\">斯塔羅斯金②·上古後期</a></u></td><td>人</td><td><b>nin</b></td><td><i>nin</i></td><td><u>真1</u> <b style=\"background: orangered;color: #fff;padding: 0px 1px\">?</b></td><td><i>human being, person, man; other persons, others; a person, someone</i></td><td><i><a href=\"https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\china\\bigchina&amp;root=config&amp;morpho=0\">巴別塔</a></i></td><td rowspan=\"1\"><i>7</i></td></tr><tr><td rowspan=\"1\" style=\"background: #f8f8f8\"><u><a href=\"http://www.kaom.net/ny_x.php?name=sita_s\">斯塔羅斯金③·詩經音</a></u></td><td style=\"background: #f8f8f8\">人</td><td style=\"background: #f8f8f8\"><b>nin</b></td><td style=\"background: #f8f8f8\"><i>nin</i></td><td style=\"background: #f8f8f8\"><u>真</u></td><td style=\"background: #f8f8f8\"><i></i></td><td style=\"background: #f8f8f8\"><i><a href=\"img.php?b=ny_sita_s&amp;p=319\">319頁</a></i></td><td rowspan=\"1\" style=\"background: #f8f8f8\"><i>8</i></td></tr><tr><td rowspan=\"1\"><u><a href=\"http://www.kaom.net/ny_x.php?name=baiyiping\">白一平</a></u></td><td>人</td><td><b>njin</b></td><td><i>*ｎｊｉｎ</i></td><td><u>真n</u></td><td><i></i></td><td><i><a href=\"img.php?b=ny_baiyiping&amp;p=903\">903頁</a></i></td><td rowspan=\"1\"><i>9</i></td></tr><tr><td rowspan=\"1\" style=\"background: #f8f8f8\"><u><a href=\"http://www.kaom.net/ny_x.php?name=zhengzhang\">鄭張尚芳</a></u></td><td style=\"background: #f8f8f8\">人</td><td style=\"background: #f8f8f8\"><b>njin</b></td><td style=\"background: #f8f8f8\"><i>njin</i></td><td style=\"background: #f8f8f8\"><u>真n</u></td><td style=\"background: #f8f8f8\"><i>日真開三平·如鄰[人] </i></td><td style=\"background: #f8f8f8\"><i><a href=\"img.php?b=ny_zhengzhang&amp;p=466\">466頁</a></i></td><td rowspan=\"1\" style=\"background: #f8f8f8\"><i>10</i></td></tr><tr><td rowspan=\"1\"><u><a href=\"http://www.kaom.net/ny_x.php?name=panwuyun\">潘悟雲</a></u></td><td>人</td><td><b>nʲiŋ</b></td><td><i>nʲiŋ</i></td><td><u>真ŋ</u></td><td><i>日真開三平·如鄰[人]</i></td><td><i></i></td><td rowspan=\"1\"><i>11</i></td></tr><tr><td rowspan=\"1\" style=\"background: #f8f8f8\"><u><a href=\"http://www.kaom.net/ny_x.php?name=xusilai\">許思萊</a></u></td><td style=\"background: #f8f8f8\">人</td><td style=\"background: #f8f8f8\"><b>nin</b></td><td style=\"background: #f8f8f8\"><i>nin</i></td><td style=\"background: #f8f8f8\"><u>真</u></td><td style=\"background: #f8f8f8\"><i>人</i></td><td style=\"background: #f8f8f8\"><i><a href=\"img.php?b=ny_xusilai&amp;p=321\">321頁</a></i></td><td rowspan=\"1\" style=\"background: #f8f8f8\"><i>12</i></td></tr><tr><td rowspan=\"1\"><u><a href=\"http://www.kaom.net/ny_x.php?name=jinlixin\">金理新</a></u></td><td>人</td><td><b>ni̠n</b></td><td><i>同左</i></td><td><u>真①</u></td><td><i></i></td><td><i></i></td><td rowspan=\"1\"><i>13</i></td></tr><tr><td rowspan=\"1\" style=\"background: #f8f8f8\"><u><a href=\"http://www.kaom.net/ny_x.php?name=baisha\">白一平-沙加爾</a></u></td><td style=\"background: #f8f8f8\">人</td><td style=\"background: #f8f8f8\"><b>niŋ</b></td><td style=\"background: #f8f8f8\"><i>*ni[ŋ] </i></td><td style=\"background: #f8f8f8\"><u>真ŋ</u></td><td style=\"background: #f8f8f8\"><i>(other) person</i></td><td style=\"background: #f8f8f8\"><i><a href=\"img.php?b=ny_baisha&amp;p=90\">90頁</a></i></td><td rowspan=\"1\" style=\"background: #f8f8f8\"><i>14</i></td></tr><tr><td rowspan=\"1\"><u><a href=\"http://www.kaom.net/ny_x.php?name=guoxiliang_biaogao\">郭錫良（表稿）</a></u></td><td>人</td><td><b>ȵĭen</b> <b style=\"background: orangered;color: #fff;padding: 0px 1px\">?</b></td><td><i>同左</i></td><td><u>真</u></td><td><i>19真部-2真部開三[ĭen]</i></td><td><i><a href=\"img.php?b=ny_guoxiliang_biaogao&amp;p=109\">109頁</a></i></td><td rowspan=\"1\"><i>15</i></td></tr><tr><td rowspan=\"1\" style=\"background: #f8f8f8\"><u>郭錫良（手冊）</u></td><td style=\"background: #f8f8f8\">人</td><td style=\"background: #f8f8f8\"><b></b></td><td style=\"background: #f8f8f8\"><i>同左</i></td><td style=\"background: #f8f8f8\"><u>真</u></td><td style=\"background: #f8f8f8\"><i></i></td><td style=\"background: #f8f8f8\"><i><a href=\"img.php?b=ny_guoxiliang_shouce&amp;p=368\">368頁</a></i></td><td rowspan=\"1\" style=\"background: #f8f8f8\"><i>16</i></td></tr><tr><td rowspan=\"12\"><b>兩漢六朝</b></td><td rowspan=\"5\">構擬</td><td rowspan=\"2\"><u>斯塔羅斯金·西漢</u></td><td>人</td><td><b>njǝn</b></td><td><i>同左</i></td><td><u></u></td><td><i>human being, person, man; other persons, others; a person, someone</i></td><td><i></i></td><td rowspan=\"2\"><i>17</i></td></tr><tr><td>[人耎]</td><td><b>nwānh</b></td><td><i>同左</i></td><td><u></u></td><td><i>weak [LZ]</i></td><td><i></i></td></tr><tr><td rowspan=\"2\" style=\"background: #f8f8f8\"><u>斯塔羅斯金·東漢</u></td><td style=\"background: #f8f8f8\">人</td><td style=\"background: #f8f8f8\"><b>ń́ǝn</b></td><td style=\"background: #f8f8f8\"><i>同左</i></td><td style=\"background: #f8f8f8\"><u></u></td><td style=\"background: #f8f8f8\"><i>human being, person, man; other persons, others; a person, someone</i></td><td style=\"background: #f8f8f8\"><i></i></td><td rowspan=\"2\" style=\"background: #f8f8f8\"><i>18</i></td></tr><tr><td style=\"background: #f8f8f8\">[人耎]</td><td style=\"background: #f8f8f8\"><b>nwānh</b></td><td style=\"background: #f8f8f8\"><i>同左</i></td><td style=\"background: #f8f8f8\"><u></u></td><td style=\"background: #f8f8f8\"><i>weak [LZ]</i></td><td style=\"background: #f8f8f8\"><i></i></td></tr><tr><td rowspan=\"1\"><u>許思萊·東漢</u></td><td>人</td><td><b>nin</b></td><td><i>同左</i></td><td><u></u></td><td><i></i></td><td><i></i></td><td rowspan=\"1\"><i>19</i></td></tr><tr><td rowspan=\"7\">韻部</td><td rowspan=\"1\" style=\"background: #f8f8f8\"><u>西漢</u></td><td style=\"background: #f8f8f8\">人</td><td style=\"background: #f8f8f8\"><i>無擬音</i></td><td style=\"background: #f8f8f8\"><i>同左</i></td><td style=\"background: #f8f8f8\"><u>真</u></td><td style=\"background: #f8f8f8\"><i></i></td><td style=\"background: #f8f8f8\"><i></i></td><td rowspan=\"1\" style=\"background: #f8f8f8\"><i>20</i></td></tr><tr><td rowspan=\"1\"><u>東漢</u></td><td>人</td><td><i>無擬音</i></td><td><i>同左</i></td><td><u>真</u></td><td><i></i></td><td><i></i></td><td rowspan=\"1\"><i>21</i></td></tr><tr><td rowspan=\"1\" style=\"background: #f8f8f8\"><u>魏</u></td><td style=\"background: #f8f8f8\">人</td><td style=\"background: #f8f8f8\"><i>無擬音</i></td><td style=\"background: #f8f8f8\"><i>同左</i></td><td style=\"background: #f8f8f8\"><u>真</u></td><td style=\"background: #f8f8f8\"><i></i></td><td style=\"background: #f8f8f8\"><i></i></td><td rowspan=\"1\" style=\"background: #f8f8f8\"><i>22</i></td></tr><tr><td rowspan=\"1\"><u>晉</u></td><td>人</td><td><i>無擬音</i></td><td><i>同左</i></td><td><u>真</u></td><td><i></i></td><td><i></i></td><td rowspan=\"1\"><i>23</i></td></tr><tr><td rowspan=\"1\" style=\"background: #f8f8f8\"><u>宋北魏後期</u></td><td style=\"background: #f8f8f8\">人</td><td style=\"background: #f8f8f8\"><i>無擬音</i></td><td style=\"background: #f8f8f8\"><i>同左</i></td><td style=\"background: #f8f8f8\"><u>真諄臻</u></td><td style=\"background: #f8f8f8\"><i></i></td><td style=\"background: #f8f8f8\"><i></i></td><td rowspan=\"1\" style=\"background: #f8f8f8\"><i>24</i></td></tr><tr><td rowspan=\"1\"><u>北魏後期北齊</u></td><td>人</td><td><i>無擬音</i></td><td><i>同左</i></td><td><u>真諄臻</u></td><td><i></i></td><td><i></i></td><td rowspan=\"1\"><i>25</i></td></tr><tr><td rowspan=\"1\" style=\"background: #f8f8f8\"><u>齊梁陳北周隋</u></td><td style=\"background: #f8f8f8\">人</td><td style=\"background: #f8f8f8\"><i>無擬音</i></td><td style=\"background: #f8f8f8\"><i>同左</i></td><td style=\"background: #f8f8f8\"><u>真諄臻欣</u></td><td style=\"background: #f8f8f8\"><i></i></td><td style=\"background: #f8f8f8\"><i></i></td><td rowspan=\"1\" style=\"background: #f8f8f8\"><i>26</i></td></tr><tr><td rowspan=\"32\"><b>中古音</b></td><td rowspan=\"17\">構擬</td><td rowspan=\"1\"><u>高本漢</u></td><td>人</td><td><b>ȵʑi̯ĕn</b></td><td><i>同左</i></td><td><u></u></td><td><i></i></td><td><i></i></td><td rowspan=\"1\"><i>27</i></td></tr><tr><td rowspan=\"1\" style=\"background: #f8f8f8\"><u>王力</u></td><td style=\"background: #f8f8f8\">人</td><td style=\"background: #f8f8f8\"><b>ɽǐěn</b></td><td style=\"background: #f8f8f8\"><i>同左</i></td><td style=\"background: #f8f8f8\"><u></u></td><td style=\"background: #f8f8f8\"><i></i></td><td style=\"background: #f8f8f8\"><i></i></td><td rowspan=\"1\" style=\"background: #f8f8f8\"><i>28</i></td></tr><tr><td rowspan=\"1\"><u>董同龢</u></td><td>人</td><td><b>ȵjen</b></td><td><i>同左</i></td><td><u></u></td><td><i></i></td><td><i></i></td><td rowspan=\"1\"><i>29</i></td></tr><tr><td rowspan=\"1\" style=\"background: #f8f8f8\"><u>李方桂</u></td><td style=\"background: #f8f8f8\">人</td><td style=\"background: #f8f8f8\"><b>ńźjĕn</b></td><td style=\"background: #f8f8f8\"><i>同左</i></td><td style=\"background: #f8f8f8\"><u></u></td><td style=\"background: #f8f8f8\"><i></i></td><td style=\"background: #f8f8f8\"><i></i></td><td rowspan=\"1\" style=\"background: #f8f8f8\"><i>30</i></td></tr><tr><td rowspan=\"1\"><u>周法高</u></td><td>人</td><td><b>ȵiɪn</b></td><td><i>同左</i></td><td><u></u></td><td><i></i></td><td><i></i></td><td rowspan=\"1\"><i>31</i></td></tr><tr><td rowspan=\"1\" style=\"background: #f8f8f8\"><u>陳新雄</u></td><td style=\"background: #f8f8f8\">人</td><td style=\"background: #f8f8f8\"><b>nʑǐen</b></td><td style=\"background: #f8f8f8\"><i>同左</i></td><td style=\"background: #f8f8f8\"><u></u></td><td style=\"background: #f8f8f8\"><i></i></td><td style=\"background: #f8f8f8\"><i></i></td><td rowspan=\"1\" style=\"background: #f8f8f8\"><i>32</i></td></tr><tr><td rowspan=\"1\"><u>蒲立本·前期</u></td><td>人</td><td><b>ɲin</b></td><td><i>同左</i></td><td><u></u></td><td><i>man,person,human being</i></td><td><i></i></td><td rowspan=\"1\"><i>33</i></td></tr><tr><td rowspan=\"1\" style=\"background: #f8f8f8\"><u>蒲立本·後期</u></td><td style=\"background: #f8f8f8\">人</td><td style=\"background: #f8f8f8\"><b>rin</b></td><td style=\"background: #f8f8f8\"><i>同左</i></td><td style=\"background: #f8f8f8\"><u></u></td><td style=\"background: #f8f8f8\"><i>man,person,human being</i></td><td style=\"background: #f8f8f8\"><i></i></td><td rowspan=\"1\" style=\"background: #f8f8f8\"><i>34</i></td></tr><tr><td rowspan=\"2\"><u>斯塔羅斯金·中古</u></td><td>人</td><td><b>ńin</b></td><td><i>同左</i></td><td><u></u></td><td><i>human being, person, man; other persons, others; a person, someone</i></td><td><i></i></td><td rowspan=\"2\"><i>35</i></td></tr><tr><td>[人耎]</td><td><b>nwần</b></td><td><i>同左</i></td><td><u></u></td><td><i>weak [LZ]</i></td><td><i></i></td></tr><tr><td rowspan=\"2\" style=\"background: #f8f8f8\"><u>斯塔羅斯金·前期</u></td><td style=\"background: #f8f8f8\">人</td><td style=\"background: #f8f8f8\"><b>ńin</b></td><td style=\"background: #f8f8f8\"><i>同左</i></td><td style=\"background: #f8f8f8\"><u></u></td><td style=\"background: #f8f8f8\"><i>human being, person, man; other persons, others; a person, someone</i></td><td style=\"background: #f8f8f8\"><i></i></td><td rowspan=\"2\" style=\"background: #f8f8f8\"><i>36</i></td></tr><tr><td style=\"background: #f8f8f8\">[人耎]</td><td style=\"background: #f8f8f8\"><b>nwā̀n</b></td><td style=\"background: #f8f8f8\"><i>同左</i></td><td style=\"background: #f8f8f8\"><u></u></td><td style=\"background: #f8f8f8\"><i>weak [LZ]</i></td><td style=\"background: #f8f8f8\"><i></i></td></tr><tr><td rowspan=\"2\"><u>斯塔羅斯金·中期</u></td><td>人</td><td><b>ńin</b></td><td><i>同左</i></td><td><u></u></td><td><i>human being, person, man; other persons, others; a person, someone</i></td><td><i></i></td><td rowspan=\"2\"><i>37</i></td></tr><tr><td>[人耎]</td><td><b>nwā̀n</b></td><td><i>同左</i></td><td><u></u></td><td><i>weak [LZ]</i></td><td><i></i></td></tr><tr><td rowspan=\"2\" style=\"background: #f8f8f8\"><u>斯塔羅斯金·後期</u></td><td style=\"background: #f8f8f8\">人</td><td style=\"background: #f8f8f8\"><b>ńin</b></td><td style=\"background: #f8f8f8\"><i>同左</i></td><td style=\"background: #f8f8f8\"><u></u></td><td style=\"background: #f8f8f8\"><i>human being, person, man; other persons, others; a person, someone</i></td><td style=\"background: #f8f8f8\"><i></i></td><td rowspan=\"2\" style=\"background: #f8f8f8\"><i>38</i></td></tr><tr><td style=\"background: #f8f8f8\">[人耎]</td><td style=\"background: #f8f8f8\"><b>nwā̀n</b></td><td style=\"background: #f8f8f8\"><i>同左</i></td><td style=\"background: #f8f8f8\"><u></u></td><td style=\"background: #f8f8f8\"><i>weak [LZ]</i></td><td style=\"background: #f8f8f8\"><i></i></td></tr><tr><td rowspan=\"1\"><u>楊力</u></td><td>人</td><td><b>ɲɨ̃n</b></td><td><i>同左</i></td><td><u></u></td><td><i></i></td><td><i></i></td><td rowspan=\"1\"><i>39</i></td></tr><tr><td rowspan=\"3\">轉寫</td><td rowspan=\"1\" style=\"background: #f8f8f8\"><u>金理新</u></td><td style=\"background: #f8f8f8\">人</td><td style=\"background: #f8f8f8\"><b>ȵin①</b></td><td style=\"background: #f8f8f8\"><i>同左</i></td><td style=\"background: #f8f8f8\"><u></u></td><td style=\"background: #f8f8f8\"><i></i></td><td style=\"background: #f8f8f8\"><i></i></td><td rowspan=\"1\" style=\"background: #f8f8f8\"><i>40</i></td></tr><tr><td rowspan=\"1\"><u>許思萊</u></td><td>人</td><td><b>ńźjen</b></td><td><i>同左</i></td><td><u></u></td><td><i></i></td><td><i></i></td><td rowspan=\"1\"><i>41</i></td></tr><tr><td rowspan=\"1\" style=\"background: #f8f8f8\"><u>白一平-沙加爾</u></td><td style=\"background: #f8f8f8\">人</td><td style=\"background: #f8f8f8\"><b>nyin</b></td><td style=\"background: #f8f8f8\"><i>同左</i></td><td style=\"background: #f8f8f8\"><u></u></td><td style=\"background: #f8f8f8\"><i>(other) person</i></td><td style=\"background: #f8f8f8\"><i></i></td><td rowspan=\"1\" style=\"background: #f8f8f8\"><i>42</i></td></tr><tr><td rowspan=\"12\">推導</td><td rowspan=\"1\"><u>高本漢</u></td><td>人</td><td><b>ȵʑi̯ĕn</b> <b style=\"background: orangered;color: #fff;padding: 0px 1px\">?</b></td><td><i>同左</i></td><td><u></u></td><td><i>如鄰切[日真A開三]</i></td><td><i></i></td><td rowspan=\"1\"><i>43</i></td></tr><tr><td rowspan=\"1\" style=\"background: #f8f8f8\"><u>王力</u></td><td style=\"background: #f8f8f8\">人</td><td style=\"background: #f8f8f8\"><b>ȵʑĭĕn</b> <b style=\"background: orangered;color: #fff;padding: 0px 1px\">?</b></td><td style=\"background: #f8f8f8\"><i>同左</i></td><td style=\"background: #f8f8f8\"><u></u></td><td style=\"background: #f8f8f8\"><i>如鄰切[日真A開三]</i></td><td style=\"background: #f8f8f8\"><i></i></td><td rowspan=\"1\" style=\"background: #f8f8f8\"><i>44</i></td></tr><tr><td rowspan=\"1\"><u>張世祿</u></td><td>人</td><td><b>ȵʑjen</b> <b style=\"background: orangered;color: #fff;padding: 0px 1px\">?</b></td><td><i>同左</i></td><td><u></u></td><td><i>如鄰切[日真A開三]</i></td><td><i></i></td><td rowspan=\"1\"><i>45</i></td></tr><tr><td rowspan=\"1\" style=\"background: #f8f8f8\"><u>嚴學宭</u></td><td style=\"background: #f8f8f8\">人</td><td style=\"background: #f8f8f8\"><b>ȵʑjɛn</b> <b style=\"background: orangered;color: #fff;padding: 0px 1px\">?</b></td><td style=\"background: #f8f8f8\"><i>同左</i></td><td style=\"background: #f8f8f8\"><u></u></td><td style=\"background: #f8f8f8\"><i>如鄰切[日真A開三]</i></td><td style=\"background: #f8f8f8\"><i></i></td><td rowspan=\"1\" style=\"background: #f8f8f8\"><i>46</i></td></tr><tr><td rowspan=\"1\"><u>董同龢</u></td><td>人</td><td><b>ȵjen</b> <b style=\"background: orangered;color: #fff;padding: 0px 1px\">?</b></td><td><i>同左</i></td><td><u></u></td><td><i>如鄰切[日真A開三]</i></td><td><i></i></td><td rowspan=\"1\"><i>47</i></td></tr><tr><td rowspan=\"1\" style=\"background: #f8f8f8\"><u>李榮</u></td><td style=\"background: #f8f8f8\">人</td><td style=\"background: #f8f8f8\"><b>ȵiĕn</b> <b style=\"background: orangered;color: #fff;padding: 0px 1px\">?</b></td><td style=\"background: #f8f8f8\"><i>同左</i></td><td style=\"background: #f8f8f8\"><u></u></td><td style=\"background: #f8f8f8\"><i>如鄰切[日真A開三]</i></td><td style=\"background: #f8f8f8\"><i></i></td><td rowspan=\"1\" style=\"background: #f8f8f8\"><i>48</i></td></tr><tr><td rowspan=\"1\"><u>蒲立本</u></td><td>人</td><td><b>ȵin</b> <b style=\"background: orangered;color: #fff;padding: 0px 1px\">?</b></td><td><i>同左</i></td><td><u></u></td><td><i>如鄰切[日真A開三]</i></td><td><i></i></td><td rowspan=\"1\"><i>49</i></td></tr><tr><td rowspan=\"1\" style=\"background: #f8f8f8\"><u>邵榮芬</u></td><td style=\"background: #f8f8f8\">人</td><td style=\"background: #f8f8f8\"><b>ȵʑjen</b> <b style=\"background: orangered;color: #fff;padding: 0px 1px\">?</b></td><td style=\"background: #f8f8f8\"><i>同左</i></td><td style=\"background: #f8f8f8\"><u></u></td><td style=\"background: #f8f8f8\"><i>如鄰切[日真A開三]</i></td><td style=\"background: #f8f8f8\"><i></i></td><td rowspan=\"1\" style=\"background: #f8f8f8\"><i>50</i></td></tr><tr><td rowspan=\"1\"><u>鄭張尚芳</u></td><td>人</td><td><b>ȵʑiɪn</b> <b style=\"background: orangered;color: #fff;padding: 0px 1px\">?</b></td><td><i>同左</i></td><td><u></u></td><td><i>如鄰切[日真A開三]</i></td><td><i></i></td><td rowspan=\"1\"><i>51</i></td></tr><tr><td rowspan=\"1\" style=\"background: #f8f8f8\"><u>潘悟雲</u></td><td style=\"background: #f8f8f8\">人</td><td style=\"background: #f8f8f8\"><b>ȵin</b> <b style=\"background: orangered;color: #fff;padding: 0px 1px\">?</b></td><td style=\"background: #f8f8f8\"><i>同左</i></td><td style=\"background: #f8f8f8\"><u></u></td><td style=\"background: #f8f8f8\"><i>如鄰切[日真A開三]</i></td><td style=\"background: #f8f8f8\"><i></i></td><td rowspan=\"1\" style=\"background: #f8f8f8\"><i>52</i></td></tr><tr><td rowspan=\"1\"><u>楊劍橋</u></td><td>人</td><td><b>ȵʑjen</b> <b style=\"background: orangered;color: #fff;padding: 0px 1px\">?</b></td><td><i>同左</i></td><td><u></u></td><td><i>如鄰切[日真A開三]</i></td><td><i></i></td><td rowspan=\"1\"><i>53</i></td></tr><tr><td rowspan=\"1\" style=\"background: #f8f8f8\"><u>麥耘</u></td><td style=\"background: #f8f8f8\">人</td><td style=\"background: #f8f8f8\"><b>ȵin</b> <b style=\"background: orangered;color: #fff;padding: 0px 1px\">?</b></td><td style=\"background: #f8f8f8\"><i>同左</i></td><td style=\"background: #f8f8f8\"><u></u></td><td style=\"background: #f8f8f8\"><i>如鄰切[日真A開三]</i></td><td style=\"background: #f8f8f8\"><i></i></td><td rowspan=\"1\" style=\"background: #f8f8f8\"><i>54</i></td></tr><tr><td class=\"td_footer\" colspan=\"10\" style=\"padding: 10px 30px;text-align: left;font-size: 12px\"><b style=\"background: orangered;color: #fff;padding: 0px 2px;font-size: 14px\">?</b> 表示電子材料不太可靠，有以下三方面：\n            <br/>1：原電子材料無韻部名（現韻部名由古音小鏡依據一般原則添加，這不是作者本意，涉及內容：高本漢、斯塔羅斯金①/②）。\n            <br/>2：推導音（依據作者中古擬音框架配上字音，配音時有些位置可能考慮不周，比如合口是否判定為w介音，可能出錯，涉及內容：中古音12家）。\n            <br/>3：局部推導（郭錫良上古音電子表缺聲母（原書是有的），現聲母依據該書原則從《廣韻》批量推導，可能存在失誤，特別是多音字中）。\n            <br/></td></tr></tbody></table>").form_acquisition())

    #main()

    #self.text_widget.insert(RECONSTRUCTIONS_SQLITE)

    #CsvImportDatabase(r"D:\LightweightNotepad\lightweight_notepad_ttkbootstrap\pre\平水韻.csv","ping_shui_yun",RECONSTRUCTIONS_SQLITE)


    #html_list = FileProcessor(RECONSTRUCTIONS,RECONSTRUCTIONS_LIST).save_content()

    #processor = HTMLToSQLite(RECONSTRUCTIONS_SQLITE)

    #processor.process_html_files(html_list)

    #processor.close()
    '''
    # 创建数据库处理器实例
    processor = PhoneticDatabaseProcessor(db_path=RECONSTRUCTIONS_SQLITE)

    # 查询特定字头、时代、性质和学者的拟音
    result = processor.get_phonetic(headword="这", era="中古", nature="構擬", scholar="王力")

    # 输出结果
    self.text_widget.insert(result)  # 输出对应的拟音或相关错误信息

    # 关闭连接
    processor.close()
    '''
    '''
    # 数据库文件路径
    db_file = r"D:\LightweightNotepad\lightweight_notepad_ttkbootstrap\data\reconstructions_page\reconstructions\reconstructions_sqlite\reconstructions_list.sqlite"

    # 创建数据库对象
    guang_yun_db = GuangYunDatabase(db_file)

    # 连接数据库
    guang_yun_db.connect()

    # 输入字头
    word_input = "這"

    # 获取对应的声纽
    sheng_nu = guang_yun_db.get_sheng_nu(word_input,"聲紐")
    sheng_diao = guang_yun_db.get_sheng_nu(word_input, "聲調")
    # 输出结果
    if sheng_nu and sheng_diao:
        self.text_widget.insert(f"字头 '{word_input}' 对应的聲紐是: {sheng_nu}")
        self.text_widget.insert(f"字头 '{word_input}' 对应的聲調是: {sheng_diao}")
    else:
        self.text_widget.insert(f"字头 '{word_input}' 没有对应的声纽")

    # 关闭数据库连接
    guang_yun_db.close()
    '''
    '''
    for i in processor:
        get_scholars,get_zi_head_list,get_reconstructions,get_rhyme,get_type,get_era = HtmlSplitting(i).form_acquisition()
        self.text_widget.insert(get_scholars)
        self.text_widget.insert(get_zi_head_list)
        self.text_widget.insert(get_reconstructions)
        self.text_widget.insert(get_rhyme)
        self.text_widget.insert(get_type)
        self.text_widget.insert(get_era)
    '''


