from assertpy import assert_that
from selenium.webdriver import ActionChains
import random


class SkillsHelper:

    def __init__(self, app, skill_name=None):
        self.app = app
        self.skill_name = skill_name

    def open_skills_page(self):
        wd = self.app.wd
        wd.get(self.app.base_url + "/profile/skills")

    def open_skills_page_by_click(self):
        wd = self.app.wd
        # press Skills in top menu
        wd.find_element_by_id("menuSkills").click()
        # press Skills in menu's drop-down list
        wd.find_element_by_id("skillsLink").click()
        # check the page of skills
        wd.find_element_by_xpath("//div[@class='_37GWdoRAYti0UC3Ar8QIUs'][text() = 'Skills']").is_displayed()

    def get_list_of_skills(self):
        wd = self.app.wd
        skills_list = wd.find_elements_by_xpath\
            ("//div[@class='_3qB-OBMPTcrvQipTsGwxWa']/div[@class='_2Is2kdo58kBSIRmBJKYksF _28o4nkHDAFFEJnW11Y-itf']")
        assert_that(skills_list).is_not_empty()
        return len(skills_list)

    def transit_to_page_with_adding_skill(self):
        wd = self.app.wd
        # press Skills in top menu
        wd.find_element_by_id("menuSkills").click()
        # press Add skills in menu's drop-down list
        wd.find_element_by_id("addSkillsLink").click()

    def add_skill_from_search_field(self):
        wd = self.app.wd
        # click into the search field
        wd.find_element_by_id("searchFilter").click()
        # choose any skill
        list_of_skills = wd.find_elements_by_xpath("//div[@class='_2au7FFxsWwEnLyHOtC5m5b']")
        random.choice(list_of_skills).click()
        # press a btn Add
        wd.find_element_by_xpath("//button[@class='_2Ja8JzmgN34VNaodRkk3pV'][text()='Add']").click()
        self.press_btn_save_skill()

    def press_btn_save_skill(self):
        wd = self.app.wd
        wd.find_element_by_id("confirmAddingSkills").click()

    def add_skill_from_alphabet_list(self):
        wd = self.app.wd
        # press a btn Add skills
        wd.find_element_by_xpath("//a[@class='_199DF05Wt-p5s5RSprY0mA'][text()='Add skills']").click()
        # click into the alphabet header
        wd.find_element_by_id("alphabetHeader").click()
        # choose any letter
        alphabet = wd.find_elements_by_xpath\
            ("//div[@class='_1o9-5HBm9cajXWVLYLCMNe']/div[@class='_2xb4F3yxL88W8xw7PSRGPC ']")
        random.choice(alphabet).click()
        # choose any skill
        skills_list = wd.find_elements_by_xpath\
            ("//div[@class='_2VbarsD_JzygMNskWSKt_5']//div[@class='_32hIyRqGMs-ua2mlKW4Cy7']")
        random.choice(skills_list).click()
        self.press_btn_save_skill()

    def edit_current_skill(self):
        wd = self.app.wd
        actions = ActionChains(wd)
        current_toggle = wd.find_element_by_xpath(
            "//div[@class='SPNDph98Uf-BzTmoU0Xg5']//div[@class='_1bJdtAOoyoKtyr-dJu8cnV']")
        actions.move_to_element(current_toggle).click_and_hold().move_by_offset(-15, 0).release().perform()

    def edit_desired_skill(self):
        wd = self.app.wd
        actions = ActionChains(wd)
        desired_toggle = wd.find_element_by_xpath(
            "//div[@class='SPNDph98Uf-BzTmoU0Xg5']//div[@class='_2R_7RZCgXun541O73Q3o7x']")
        actions.move_to_element(desired_toggle).click_and_hold().move_by_offset(15, 0).release().perform()

    def get_current_percentage_value(self):
        wd = self.app.wd
        percent_value = wd.find_element_by_xpath(
            "//div[@class='_3y5fWYnxTZ0a6kZKrUaq8_']/div[@class='_111k8vADT50biqEBTnzD5a']").get_attribute("textContent")
        return percent_value

    def get_desired_percentage_value(self):
        wd = self.app.wd
        percent_value = wd.find_element_by_xpath(
            "//div[@class='_3y5fWYnxTZ0a6kZKrUaq8_']/div[@class='_66VkFlpdgyFBtP8jIZt2a']").get_attribute("textContent")
        return percent_value

    def delete_skill(self):
        wd = self.app.wd
        # press on a btn Delete
        wd.find_element_by_xpath("//div[@class='_2MG-_aiHDlEC2aHG2gnOsg']//div[text()='Delete']").click()
        # press on a btn Confirm
        wd.find_element_by_id("confirmRemovingButton").click()

    def hide_desired_skill(self):
        wd = self.app.wd
        self.get_name_of_skill()
        wd.find_elements_by_xpath("//i[@class='material-icons _2WQSTQwBQoaeQXUTVZud0_']")[0].click()

    def get_list_of_desired_skills(self):
        wd = self.app.wd
        number_of_skills = wd.find_elements_by_xpath("//div[@class='xGABAltOqGF9LujeOQ2DS']")
        return len(number_of_skills)

    def get_name_of_skill(self):
        wd = self.app.wd
        self.skill_name = wd.find_element_by_xpath(
            "//div[@class='_2ocMM6372GfB_C45UB9x8M']").get_attribute("textContent")
        return self.skill_name

    def find_hidden_skill(self):
        wd = self.app.wd
        self.open_skills_page()
        # get name of hidden skill
        name_hidden_skill = wd.find_elements_by_xpath(
            "//div[@class='_2b-grcrzJeyun6TJn70kGG']")[0].get_attribute("textContent")
        assert_that(self.skill_name).is_equal_to(name_hidden_skill.strip())
        # get current / desired values
        cur_value = self.get_current_percentage_value()
        des_value = self.get_desired_percentage_value()
        assert_that(cur_value).is_equal_to(des_value)
