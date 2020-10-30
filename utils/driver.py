from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import json
import time


class WebDriver(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_snapshot(self, filename):
        if self.driver:
            try:
                self.driver.save_screenshot(filename)
            except:
                alert = self.driver.switch_to.alert()
                alert.accept()

    def go_to_url(self, url):
        try:
            self.driver.get(url)
        except Exception as e:
            raise Exception(f'Desired URL: {url}, exception -  {e}')
        assert self.driver.title.find("404 Page Not Found") < 0, f"URL: {url} results in '404 Page Not Found'"
        assert self.driver.title.find(
            "Problem loading page") < 0, f"URL: {url} results in error 'The page isn't redirecting properly'"

    def quit(self):
        try:
            self.driver.close()
            self.driver.quit()
        except Exception as e:
            raise Exception(f'Problem with closing a browser: {e}')

    def copy_new_email(self):
        delay = 3
        try:
            el = WebDriverWait(self.driver, delay)\
                .until(EC.presence_of_element_located((By.CLASS_NAME, 'what_to_copy'))).text
            print("Page is ready!")
        except TimeoutException:
            raise TimeoutException
        return el

    def copy_picture(self, url):
        self.go_to_url(url)
        res = self.driver.find_element_by_xpath('/html/body/pre').text
        return json.loads(res)

    def chek_received_email(self):
        delay = 3
        time.sleep(5)
        try:
            self.driver.refresh()
            el = WebDriverWait(self.driver, delay)\
                .until(EC.presence_of_element_located((By.CLASS_NAME, 'msg_item'))).text

            print("Page is ready!")
        except TimeoutException:
            raise TimeoutException
        s = el.split('.com ')[1].split(' (')[0].replace("'", '"')
        return s
