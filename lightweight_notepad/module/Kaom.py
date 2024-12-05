import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
import logging
import re

class GetThePage:
    def __init__(self):
        self.driver = None
        self.ua = UserAgent()
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    def init_chrome_driver(self):
        """初始化无头Chrome驱动，带随机User-Agent"""
        options = Options()
        options.add_argument("--headless")  # 无头模式
        options.add_argument("--disable-gpu")  # 禁用GPU加速
        options.add_argument("--no-sandbox")  # 解决Linux环境下权限问题
        options.add_argument("--disable-dev-shm-usage")  # 解决资源问题

        # 随机User-Agent
        user_agent = self.ua.random
        options.add_argument(f"user-agent={user_agent}")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def wait_for_element(self, locator, timeout=10):
        """等待元素出现"""
        try:
            element = WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))
            return element
        except Exception as e:
            logging.error(f"等待元素超时: {locator}, 错误: {e}")
            return None

    def handle_frequency_limit(self):
        """处理频繁点击的限制提示"""
        page_source = self.driver.page_source
        if "請點擊間隔大於3秒" in page_source:
            logging.warning("检测到频繁点击限制，等待60秒后重试")
            time.sleep(8)  # 等待8秒
            return True  # 返回True表示需要重试
        return False

    def crawl_word_data(self, word):
        """根据输入的字爬取数据并下载整个页面HTML"""
        try:
            self.init_chrome_driver()
            self.driver.get("https://www.kaom.net/ny_word.php")
            logging.info(f"访问页面成功: {self.driver.current_url}")

            # 输入文字
            input_box = self.wait_for_element((By.NAME, "word"))
            if not input_box:
                return []
            input_box.clear()
            input_box.send_keys(word)
            logging.info(f"输入文字: {word}")

            # 随机延迟，模拟人类行为
            #time.sleep(random.uniform(1, 2))  # 增加随机延迟

            # 选择下拉框选项
            dropdown = self.driver.find_element(By.NAME, "bianti")
            dropdown.send_keys("no")

            # 随机延迟，模拟人类行为
            time.sleep(random.uniform(1, 2))  # 增加随机延迟

            # 提交表单
            submit_button = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
            submit_button.click()

            # 随机延迟，模拟人类行为
            time.sleep(random.uniform(1, 2))  # 增加随机延迟

            # 切换到新窗口
            main_window = self.driver.current_window_handle
            WebDriverWait(self.driver, 10).until(ec.new_window_is_opened([main_window]))
            new_window = [window for window in self.driver.window_handles if window != main_window][0]
            self.driver.switch_to.window(new_window)
            logging.info("切换到新窗口")

            # 等待新窗口加载
            self.wait_for_element((By.TAG_NAME, "table"))

            # 检查是否出现频繁点击限制提示
            if self.handle_frequency_limit():
                return []  # 如果触发限制，返回空列表

            # 保存HTML到文件
            file_name = f"{word}_page.html"
            tables = re.findall(r'<table.*?>(.*?)</table>', self.driver.page_source, re.DOTALL)
            with open(file_name, "w", encoding="utf-8") as f:
                f.write(str(tables))
                logging.info(f"页面HTML已保存为: {file_name}")

        except Exception as e:
            logging.error(f"发生异常: {e}")
            return []
        finally:
            self.driver.quit()

    def crawl_words(self, words):
        """批量爬取多个词的数据"""
        for word in words:
            logging.info(f"开始处理: {word}")
            self.crawl_word_data(word)

class HtmlAnalysis:
    def __init__(self):


def main():
    words = ["江"]
    crawler = GetThePage()
    crawler.crawl_words(words)


if __name__ == "__main__":
    main()
