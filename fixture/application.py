
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.offers import OffersHelper
from fixture.skills import SkillsHelper
from fixture.profile import ProfileHelper
from testrail_config import TestRailHelper
from fixture.sign_up import SignUpHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "firefox":
            self.wd = webdriver.Firefox()  # for FF ESR52 use = webdriver.Firefox(capabilities={"marionette": False})
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        # self.wd.set_window_size(1024, 768)
        self.wd.maximize_window()
        self.base_url = base_url
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.offers = OffersHelper(self)
        self.skills = SkillsHelper(self, skill_name=None)
        self.profile = ProfileHelper(self)
        self.testrail_config = TestRailHelper(self)
        self.sign_up = SignUpHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
