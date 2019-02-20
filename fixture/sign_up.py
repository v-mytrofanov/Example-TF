from assertpy import assert_that
from data.profile import zip_codes
import random
import os


class SignUpHelper:

    def __init__(self, signup):
        self.signup = signup

    def start_signup(self):
        wd = self.signup.wd
        wd.get(self.signup.base_url)
        # confirm about cookies
        wd.find_element_by_xpath("//div/button[@class='_3xdnBCFHHzRwWBlQzQct_0']")
        wd.find_element_by_xpath("//div/button[@class='_3xdnBCFHHzRwWBlQzQct_0']").click()
        # choose language
        wd.find_element_by_css_selector("._3LR9l_AGUolFfsacKd3ufC").click()
        wd.find_elements_by_xpath("//div[@class='VTP5OgAreoOzdPdab-tCo']")[0].click()
        # press a btn "Yes, start now!"
        wd.find_element_by_id("startButton").click()

    def fill_out_form(self, name, email):
        wd = self.signup.wd
        # specify firstname
        wd.find_element_by_id("firstName-field").click()
        wd.find_element_by_id("firstName-field").send_keys(name.name)
        # specify lastname
        wd.find_element_by_id("lastName-field").click()
        wd.find_element_by_id("lastName-field").send_keys(name.name)
        # mark a checkbox
        wd.find_element_by_id("agreement-checkbox").click()
        # specify email
        wd.find_element_by_id("email-field").click()
        wd.find_element_by_id("email-field").send_keys(email.email)
        # press a btn sign up
        wd.find_element_by_id("signupButton").click()
        # check the successful sign up
        ava = wd.find_element_by_css_selector("div._17jJDYWfx7eDeRpZ-WzCE6").get_attribute("textContent")
        assert_that(ava).is_equal_to("Choose your avatar")

    def transfer_to_mailbox(self, mailbox):
        wd = self.signup.wd
        wd.get(mailbox)

    def specify_login_password(self, mail_login, mail_password):
        wd = self.signup.wd
        # enter login
        wd.find_element_by_xpath("/html//input[@id='id-l']").click()
        wd.find_element_by_xpath("/html//input[@id='id-l']").clear()
        wd.find_element_by_xpath("/html//input[@id='id-l']").send_keys(mail_login)
        # enter password
        wd.find_element_by_xpath(
            "//label[@class='input-text__label input-text__label_size-regular input-text__label_inactive']").click()
        wd.find_element_by_xpath("/html//input[@id='id-p']").clear()
        wd.find_element_by_xpath("/html//input[@id='id-p']").send_keys(mail_password)
        # press a btn login
        wd.find_element_by_xpath("//button[@type='submit']").click()

    def confirm_email_and_transfer_to_account(self):
        wd = self.signup.wd
        # press on email
        wd.find_elements_by_xpath("//tbody//td//a[@class='msglist__row_href']")[0].click()
        # press a btn for confirming email
        wd.find_element_by_xpath("//tbody//td//a[@class='xfmc4']").click()
        # get windows_id and switch to necessary window
        main_id = wd.current_window_handle
        all_windows = wd.window_handles
        for _ in all_windows:
            if _ != main_id:
                wd.close()
                wd.switch_to.window(_)

    def check_users_account(self):
        wd = self.signup.wd
        # check displaying tooltip
        tooltip_title = wd.find_element_by_xpath("//div[@class='vGgSdyENewmzy4_SKu3NK']").get_attribute("textContent")
        assert_that(tooltip_title).is_equal_to("Welcome to CVCube!")
        # close tooltip
        wd.find_element_by_xpath("//div[@class='_2x1kbGwvUwJW-s3RZeRjJh']").click()
        # check username element
        wd.find_element_by_xpath("//div[@class='_17y1uFPtDxkf7wminv19nT']").is_displayed()
        # check top menu
        top_menu = len(wd.find_elements_by_xpath("//div[@class='_2n6UNBkDs-2HWGEKjbl0wj']"))
        assert_that(top_menu).is_equal_to(4)

    def choice_all_options(self):
        wd = self.signup.wd
        # choose a second role
        old_role = wd.find_element_by_xpath("//div[@class='_3JDmcm74E8JTYsAMIcdp9m']").get_attribute("textContent")
        wd.find_element_by_id("nextCharacterButton").click()
        new_role = wd.find_element_by_xpath("//div[@class='_3JDmcm74E8JTYsAMIcdp9m']").get_attribute("textContent")
        assert_that(new_role).is_not_equal_to(old_role)
        wd.find_element_by_id("selectCharacterButton").click()
        # choose field of studies
        old_field = wd.find_element_by_xpath("//div[@class='_16sZF-_oaraVFJbSF5wxWY']").get_attribute("textContent")
        wd.find_element_by_id("prevBranchButton").click()
        new_field = wd.find_element_by_xpath("//div[@class='_16sZF-_oaraVFJbSF5wxWY']").get_attribute("textContent")
        assert_that(new_field).is_not_equal_to(old_field)
        wd.find_element_by_id("selectBranchButton").click()
        # upload cv
        old_inactive_badges = len(wd.find_elements_by_xpath("//div[@class='_3CkrdaGQBcpqMiQaWrGMYC']"))
        cv = wd.find_element_by_xpath("//input[@type='file'][@class='_1wDUiZYkkDmDzNR8uyChrN']")
        cv.send_keys(os.path.abspath(r'..\autotests_user_module\images\Lebenslauf.pdf'))
        new_inactive_badges = len(wd.find_elements_by_xpath("//div[@class='_3CkrdaGQBcpqMiQaWrGMYC']"))
        assert_that(new_inactive_badges).is_less_than(old_inactive_badges)
        # choose middle payment
        wd.find_element_by_css_selector("#midMoneyButton [version]").click()
        wd.find_element_by_id("selectPrice").click()
        # choose certificate
        old_value = wd.find_element_by_xpath("//div[@class='_3bjTZQOxbPJk6BMGJI5dJV']").get_attribute("textContent")
        wd.find_element_by_id("firstCerficateButton").click()
        new_value = wd.find_element_by_xpath("//div[@class='_3bjTZQOxbPJk6BMGJI5dJV']").get_attribute("textContent")
        assert_that(old_value).is_not_equal_to(new_value)
        wd.find_element_by_id("selectSertificateButton").click()
        # specify zip-code
        wd.find_element_by_id("zip-field").click()
        wd.find_element_by_id("zip-field").send_keys(random.choice(zip_codes))
        wd.find_element_by_id("selectZipButton").click()
        # choose traveling time
        old_time = wd.find_element_by_xpath("//div[@class='_3ufTL5JruTeZyIBjeNIHC4']").get_attribute("textContent")
        wd.find_element_by_id("forthTime").click()
        new_time = wd.find_element_by_xpath("//div[@class='_3ufTL5JruTeZyIBjeNIHC4']").get_attribute("textContent")
        assert_that(old_time).is_not_equal_to(new_time)
        wd.find_element_by_id("selectTimeButton").click()

    def get_confirmation_message(self):
        wd = self.signup.wd
        wd.find_element_by_xpath("//div[@class='cHff37q2MftX2hDXkcdlI']").is_displayed()

    def choose_zero_character(self):
        wd = self.signup.wd
        arrow = wd.find_element_by_id("nextCharacterButton")
        for _ in range(5):
            arrow.click()
        wd.find_element_by_xpath("//div[@class='_3OHQelLtPfur8EUB-qgcXv']").is_displayed()
        # press a btn next
        wd.find_element_by_id("selectCharacterButton").click()
        # check confirmation message
        question_mark = wd.find_element_by_xpath("//div[@class='_3oXgKFFIaC3NrwPFwIDe8A']").get_attribute("textContent")
        assert_that(question_mark).is_equal_to("?")
