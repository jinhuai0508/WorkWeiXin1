import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class Testcookies():
    def setup_method(self):
        # chrome_args = webdriver.ChromeOptions()
        # chrome_args.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=chrome_args)
        # self.driver.implicitly_wait(5)

        self.driver = webdriver.Chrome()

        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()

    def test_cookie(self):
        #  cookies = self.driver.get_cookies()
        #  print(cookies)
        # # 将cookies信息存储到文件
        #  with open("cookie.json", "w") as f:
        #      json.dump(cookies, f)

        #注入cookie之前要先打开登录访问的前一个页面
        self.driver.get("https://work.weixin.qq.com/")

        #注入cookie信息
        with open("cookie.json", "r") as f:
            cookies = json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id='menu_customer']").click()
        sleep(3)