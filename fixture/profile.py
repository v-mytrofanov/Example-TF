from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from assertpy import assert_that
from data.profile import *
import random
import os


class ProfileHelper:

    def __init__(self, app):
        self.app = app

    def open_profile_page(self):
        wd = self.app.wd
        wd.get(self.app.base_url + "/profile/profile")

    def open_profile_page_via_menu(self):
        wd = self.app.wd
        wd.find_element_by_id("menuProfile").click()

    def press_button_edit_profile(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//button[@id='mainEditProfileButton']/div[text()='Edit profile']").click()

    def get_zip_code(self):
        wd = self.app.wd
        zip_code = wd.find_element_by_xpath("//input[@name='zip']").get_attribute("defaultValue")
        return int(zip_code)

    def change_zip_code(self):
        wd = self.app.wd
        # get current zip code
        zip = self.get_zip_code()
        self.press_button_edit_profile()
        # specify a new zip code
        wd.find_element_by_xpath("//input[@name='zip']").click()
        wd.find_element_by_xpath("//input[@name='zip']").clear()
        new_zips = list(filter(lambda x: x != zip, zip_codes))
        wd.find_element_by_xpath("//input[@name='zip']").send_keys(random.choice(new_zips))
        self.save_changes()

    def save_changes(self):
        wd = self.app.wd
        wd.find_element_by_id("saveChangesButton").click()
        # check alert about successful action
        wait = WebDriverWait(wd, 5, poll_frequency=1)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='_2uQIxJecv6XvVT7EVDWD-t']")))
        # close alert
        wd.find_element_by_xpath("//button[@class='rIgUOvFfzh2SY5rCpEJ3L']").click()

    def specify_password(self, *args):
        wd = self.app.wd
        self.press_button_edit_profile()
        # specify a new password
        wd.find_element_by_id("fpass-field").click()
        wd.find_element_by_id("fpass-field").send_keys(*args)
        # confirm a new password
        wd.find_element_by_id("spass-field").click()
        wd.find_element_by_id("spass-field").send_keys(*args)
        self.save_changes()

    def login_with_new_password(self, new_password, email):
        wd = self.app.wd
        # specify user's credentials
        wd.find_element_by_xpath("//input[@name='email']").click()
        wd.find_element_by_xpath("//input[@name='email']").clear()
        wd.find_element_by_xpath("//input[@name='email']").send_keys(email)
        wd.find_element_by_xpath("//input[@name='password']").click()
        wd.find_element_by_xpath("//input[@name='password']").clear()
        wd.find_element_by_xpath("//input[@name='password']").send_keys(new_password)
        # press a btn Login
        wd.find_element_by_xpath("//button[@class='_1nP445ctxUrpwlYMqTfOMK']").click()
        # check_login_and_get_username
        username = wd.find_element_by_css_selector(
            "div.WSdQr8GYS2Fte07PXAc-N ._17y1uFPtDxkf7wminv19nT").get_attribute("textContent")
        assert_that(username).is_equal_to("Auto_user Dont Touch")

    def upload_avatar(self):
        wd = self.app.wd
        self.press_button_edit_profile()
        # upload avatar
        avatar = wd.find_element_by_xpath("//input[@type='file'][@class='_3VIiPq3oFrFmFZ3hinAhAR']")
        avatar.send_keys(os.path.abspath(r'..\autotests_user_module\images\wolf.jpeg'))
        # save avatar
        self.save_changes()

    def upload_cv(self):
        wd = self.app.wd
        self.press_button_edit_profile()
        # upload cv
        cv = wd.find_element_by_xpath("//input[@type='file'][@class='_1wDUiZYkkDmDzNR8uyChrN']")
        cv.send_keys(os.path.abspath(r'..\autotests_user_module\images\Lebenslauf.pdf'))
        # check an alert about successful uploading cv
        self.save_changes()

    def delete_user(self):
        wd = self.app.wd
        self.open_profile_page_via_menu()
        self.press_button_edit_profile()
        # press the "here" for deleting
        wd.find_element_by_id("deleteProfileButton").click()
        # confirm deleting
        wd.find_elements_by_xpath("//button[@class='_1nY8UdCousA7_YTOfmB3p5']")[1].click()
        # check logout from user's account to main page
        wd.find_element_by_xpath("//img[@class='LrzocSTT8jbvYyeYcCGOD']").is_displayed()
