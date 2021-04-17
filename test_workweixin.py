import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class Testweixin:
    def setup_method(self):
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_args)
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()

    def test_workweixin(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        sleep(5)
        self.driver.find_element(By.ID, "menu_customer").click()
        cookies = self.driver.get_cookies()
        print(cookies)
        # 将cookies信息存储到文件
        with open("cookie.json", "w") as f:
            json.dump(cookies, f)

    # def test_testdemo(self):
    #     self.driver.get("http://www.baidu.com")
    #
