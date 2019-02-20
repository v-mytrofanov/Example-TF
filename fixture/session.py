from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, email, password):
        wd = self.app.wd
        # confirm about cookies
        wd.find_element_by_xpath("//div/button[@class='_3xdnBCFHHzRwWBlQzQct_0']").click()
        # choose language
        wd.find_element_by_css_selector("._3LR9l_AGUolFfsacKd3ufC").click()
        wd.find_elements_by_xpath("//div[@class='VTP5OgAreoOzdPdab-tCo']")[0].click()
        # choose user's module
        wd.find_element_by_css_selector("._2iIOX6WePX46qGIoHvu3XZ").click()
        wd.find_element_by_xpath("//a[@class='_2wMcsWux_8cbwlk2YpQ8I-']").click()
        # specify user's credentials
        wd.find_element_by_xpath("//input[@name='email']").click()
        wd.find_element_by_xpath("//input[@name='email']").clear()
        wd.find_element_by_xpath("//input[@name='email']").send_keys(email)
        wd.find_element_by_xpath("//input[@name='password']").click()
        wd.find_element_by_xpath("//input[@name='password']").clear()
        wd.find_element_by_xpath("//input[@name='password']").send_keys(password)
        # press a btn Login
        wd.find_element_by_xpath("//button[@class='_1nP445ctxUrpwlYMqTfOMK']").click()

    def logout(self):
        wd = self.app.wd
        sleep(1)
        wait = WebDriverWait(wd, 5, poll_frequency=1)
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@id='menuMore']//div[@class='SC17R398FgDtAfys4nxWZ']"))).click()
        wd.find_element_by_xpath("//div[@id='menuMore']//a[@href='/login']"
                                 "/div[@class='_3yl0syVO4yO1x84l9OOO9_']").click()
