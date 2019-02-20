from assertpy import assert_that
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random


class OffersHelper:

    def __init__(self, app):
        self.app = app

    def open_offers_page(self):
        wd = self.app.wd
        wd.get(self.app.base_url + "/profile/offers/")
        matched_offers = wd.find_element_by_css_selector("div._1RBChRXvM6aeD-QRfta4h7").get_attribute("textContent")
        assert_that(matched_offers).contains("Matched Offers")

    def open_favorite_offers_page(self):
        wd = self.app.wd
        wd.get(self.app.base_url + "/profile/offers/favorite")
        favorite_offers = wd.find_element_by_css_selector("div._5QOvL0mrl6xQATVko9lhj").get_attribute("textContent")
        assert_that(favorite_offers).is_equal_to("Favorite Offers")

    def open_archived_offers_page(self):
        wd = self.app.wd
        wd.get(self.app.base_url + "/profile/offers/archived")
        matched_offers = wd.find_element_by_css_selector("div._5QOvL0mrl6xQATVko9lhj").get_attribute("textContent")
        assert_that(matched_offers).is_equal_to("Archived Offers")

    def open_booked_courses_page(self):
        wd = self.app.wd
        wd.get(self.app.base_url + "/profile/offers/booked")
        matched_offers = wd.find_element_by_css_selector("div._5QOvL0mrl6xQATVko9lhj").get_attribute("textContent")
        assert_that(matched_offers).is_equal_to("Booked Offers")

    def open_offers_page_by_click(self):
        wd = self.app.wd
        wait = WebDriverWait(wd, 5, poll_frequency=1)
        # press a button "Offers" in top menu
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@id='menuOffers']//div[text()='Offers']"))).click()
        # press a btn "Offers" in drop-down list
        wd.find_element_by_css_selector("._3U3Uzk0t6lfXxmV1yttB2t").click()
        # check the offers' page
        wait.until(EC.url_contains("/profile/offers"))
        matched_offers = wd.find_element_by_css_selector("div._1RBChRXvM6aeD-QRfta4h7").get_attribute("textContent")
        assert_that(matched_offers).contains("Matched Offers")

    def press_btn_load_more(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//button[@class='_2NzHovuWBjhP_h7R38tG86'][text()='Load more']").click()

    def get_list_of_courses(self):
        wd = self.app.wd
        courses_list = wd.find_elements_by_css_selector(".Rig9YiYm_739HABgrDfwA ._3RmyPRBhOiz3m9zws1JWu-")
        return len(courses_list)

    def review_all_courses(self):
        wd = self.app.wd
        wait = WebDriverWait(wd, 5, poll_frequency=1)
        btn_load_more = wd.find_element_by_xpath("//button[@class='_2NzHovuWBjhP_h7R38tG86'][text()='Load more']")
        list_1 = self.get_list_of_courses()
        self.press_btn_load_more()
        list_2 = self.get_list_of_courses()
        assert list_1 < list_2
        while btn_load_more.is_displayed():
            self.press_btn_load_more()
            if wait.until(EC.invisibility_of_element
                              ((By.XPATH, "//button[@class='_2NzHovuWBjhP_h7R38tG86'][text()='Load more']"))):
                return True

    def select_any_course_as_favorite(self):
        wd = self.app.wd
        list_hearts = wd.find_elements_by_xpath("//div[@class='_3RmyPRBhOiz3m9zws1JWu-']//i[text()=' favorite ']")
        random.choice(list_hearts).click()

    def get_list_of_favorite_courses(self):
        wd = self.app.wd
        favorite_list = wd.find_elements_by_css_selector("._3rtKTWKGofLT_PzMGKPTdQ ._2oywgY108C-IYCpD2dscFH")
        return len(favorite_list)

    def delete_favorite_course(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@class='_2m5-5kRJvaBFAmADWxzgAV']/i[text()=' delete ']").click()

    def select_first_course_as_archived(self):
        wd = self.app.wd
        wd.find_elements_by_xpath("//div[@class='_3RmyPRBhOiz3m9zws1JWu-']//i[text()=' delete ']")[2].click()

    def get_list_of_all_courses(self):
        wd = self.app.wd
        courses_list = wd.find_elements_by_css_selector("._3rtKTWKGofLT_PzMGKPTdQ ._2oywgY108C-IYCpD2dscFH")
        return len(courses_list)

    def get_title_archived_course_and_find_one_in_offers(self):
        wd = self.app.wd
        # get name of archived course
        title_of_course = wd.find_element_by_css_selector("#courseTitle").get_attribute("textContent")
        self.open_offers_page_by_click()
        # specify name of archived course into searching field
        wd.find_element_by_css_selector("input.wSfSBBZYq7YSanl9N-ZsZ").click()
        wd.find_element_by_css_selector("input.wSfSBBZYq7YSanl9N-ZsZ").send_keys(title_of_course)
        # press a btn Apply
        wd.find_element_by_xpath("//button[@class='_2NI0CUTIGdw3SHZ_2sc_BB']").click()
        # check the titles of remaining courses
        list_of_courses = wd.find_elements_by_css_selector("#courseTitle")
        for course in list_of_courses:
            if course.get_attribute("textContent") == title_of_course:
                return False

        return True

    def delete_archived_course(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(".w1TS1MOOHlAQODyXODAdX").click()

    def get_title_of_course(self):
        wd = self.app.wd
        title_of_course = wd.find_element_by_css_selector("#courseTitle").get_attribute("textContent")
        return title_of_course

    def find_ex_archived_course(self):
        wd = self.app.wd
        self.open_offers_page_by_click()
        # specify name of archived course into searching field
        wd.find_element_by_css_selector("input.wSfSBBZYq7YSanl9N-ZsZ").click()
        wd.find_element_by_css_selector("input.wSfSBBZYq7YSanl9N-ZsZ")\
            .send_keys(OffersHelper.get_title_of_course(self))
        # check the titles of courses
        return self.compare_title_of_course()

    def check_courses_skills(self):
        wd = self.app.wd
        # choose first course
        wd.find_elements_by_css_selector("#courseTitle")[0].click()
        # check for skills
        wd.find_element_by_xpath("//div[@class='_2SWy788nI7bBJAOfDbJEOe']/div[text()='Skills']")
        first_skill = wd.find_element_by_xpath\
            ("//div[@class='_2VvP0kStC62fybXHMC38g_']//div[@class='_1CjCvdeBMcl8iD0nn4XlfD']")
        first_skill.is_displayed()

    def choose_any_course(self):
        wd = self.app.wd
        list_courses = wd.find_elements_by_css_selector("#courseTitle")
        random.choice(list_courses).click()

    def mark_as_booked(self):
        wd = self.app.wd
        # get title of course
        wd.find_element_by_css_selector(".frxlxkEFosz6IN6p5X0Z-").get_attribute("textContent")
        # press link "mark as booked"
        wd.find_element_by_xpath("//div[@class='_2xcnQvZEqFRJUPlkWNdReU'][text()='mark as booked']").click()
        # click into the field "start date"
        wd.find_element_by_xpath("//div[@class='_3KJrf7Ov4SfLGjZnUOuvy3']/input[@name='startDate']").click()
        self.select_date_of_course()
        # click into the field "finish date"
        wd.find_element_by_xpath("//div[@class='_3KJrf7Ov4SfLGjZnUOuvy3']/input[@name='finishDate']").click()
        self.select_date_of_course()
        # press a btn save
        wd.find_element_by_xpath("//button[@class='_2MbZYrgl_gJRMseVZVn7bb'][text()='Save']").click()

    def select_date_of_course(self):
        wd = self.app.wd
        # move to the other month
        wd.find_element_by_xpath(
            "//div[@class='a1gGQaqXfU5vrrCu6Csry']//button[text()=' keyboard_arrow_right ']").click()
        # choose date
        list_dates = wd.find_elements_by_css_selector(".sn_yuFzJML2SE1CtqrQKI ._1KOZ9GIypElw5TRTAIqMRc")
        random.choice(list_dates[8:15]).click()

    def check_booked_course_on_page(self):
        self.open_booked_courses_page()
        self.get_title_of_course()
        return self.compare_title_of_course()

    def compare_title_of_course(self):
        wd = self.app.wd
        list_of_courses = wd.find_elements_by_css_selector("#courseTitle")
        for course in list_of_courses:
            if course.get_attribute("textContent") == OffersHelper.get_title_of_course(self):
                return True
            else:
                assert_that('list_of_courses').contains(OffersHelper.get_title_of_course(self))

    def cancel_booking_course(self):
        wd = self.app.wd
        # choose a course
        wd.find_element_by_css_selector("#courseTitle").click()
        # press a link "cancel booking"
        wd.find_element_by_xpath("//div[@class='_2xcnQvZEqFRJUPlkWNdReU'][text()='Cancel booking']").click()
        # press a btn "cancel"
        wd.find_element_by_xpath("//button[@class='_3-5sdH6NmH9j-aJPmbB7VS'][text()='Cancel']").click()
        wd.find_element_by_xpath("//div[@class='_2xcnQvZEqFRJUPlkWNdReU'][text()='mark as booked']").is_displayed()



















