import logging

from selenium.webdriver.common.by import By
from constants.login_page import LoginPageConstants
from constants.profile_page import ProfilePage

from helpers.base import BaseHelper


class LoginPage (BaseHelper):
    """Store helpers for login"""

    def __init__(self, driver):
        super ().__init__ (driver)
        self.log=logging.getLogger (__name__)
        self.constants=LoginPageConstants

    def new_registration(self, email, username, password, double_password):
        """"Create new user"""
        # 4. Clear fields
        self.fill_input_fields (by=By.XPATH, locator=self.constants.EMAIL_REGISTRATION_XPATH, value=email)
        self.fill_input_fields (by=By.XPATH, locator=self.constants.USERNAME_REGISTRATION_XPATH, value=username)
        self.fill_input_fields (by=By.XPATH, locator=self.constants.PASSWORD_REGISTRATION_XPATH, value=password)
        self.fill_input_fields (by=By.XPATH, locator=self.constants.DOUBLE_PASSWORD_REGISTRATION_XPATH, value=double_password)
        self.log.debug ("Clear fields email, username, password")

        # Press button 'Зареєструватися'
        self.wait_and_click (By.XPATH, locator=self.constants.REGISTRATION_BUTTON_XPATH)
        self.log.debug ("Click button")

        return LoginPage (self.driver)

    def login(self, email, password):
        """Login by email and password"""

        # 4. Clear fields
        self.fill_input_fields (by=By.XPATH, locator=self.constants.EMAIL_LOGIN_XPATH, value=email)
        self.fill_input_fields (by=By.XPATH, locator=self.constants.PASSWORD_LOGIN_XPATH, value=password)
        self.log.debug ("Clear email and login fields")

        # 5. Press button 'Увійти'
        self.wait_and_click (By.XPATH, locator=self.constants.LOGIN_BUTTON_XPATH)
        self.log.info ("Press button 'Увійти' in login form")

        return LoginPage (self.driver)

    def search(self, search_field):
        """Testing search fields"""
        # Find button All Sections click on it
        self.wait_and_click (By.XPATH, locator=self.constants.ALL_POINTS_BUTTON_XPATH)
        self.log.info ("Find button All Sections click on it")

        # Clear Search field and write word 'День Незалежності'
        self.find_and_input_search_field (by=By.XPATH, locator=self.constants.SEARCH_FIELD_XPATH, value=search_field)
        self.log.info ("Clear Search field and write word")

        # Click button Search
        self.wait_and_click (By.XPATH, locator=self.constants.SEARCH_BUTTON_XPATH)
        self.log.info ("Click button Search")

    def button_assess_and_enter(self):
        # Click 'Доступ' button
        self.wait_and_click (By.XPATH, locator=ProfilePage.ACCESS_BUTTON_XPATH)
        self.log.info ("Click 'Доступ' button")

        # Click 'Увійти' button
        self.wait_and_click (By.XPATH, locator=ProfilePage.ENTER_BUTTON_XPATH)
        self.log.info ("Click 'Увійти' button")

    def check_menu_in_ukr(self):
        """Verified that Menu in Ukrainian language"""
        main_point=self.find_by_contains_text (self.constants.MAIN_BUTTON_XPATH)
        assert main_point.text == self.constants.MAIN_BUTTON_TEXT

        public_point=self.find_by_contains_text (self.constants.PUBLIC_BUTTON_XPATH)
        assert public_point.text == self.constants.PUBLIC_BUTTON_TEXT

        column_point=self.find_by_contains_text (self.constants.COLUMN_BUTTON_XPATH)
        assert column_point.text == self.constants.COLUMN_BUTTON_TEXT

        interview_point=self.find_by_contains_text (self.constants.INTERVIEW_BUTTON_XPATH)
        assert interview_point.text == self.constants.INTERVIEW_BUTTON_TEXT

        reportage_point=self.find_by_contains_text (self.constants.REPORTAGE_BUTTON_XPATH)
        assert reportage_point.text == self.constants.REPORTAGE_BUTTON_TEXT

        blog_point=self.find_by_contains_text (self.constants.BLOG_BUTTON_XPATH)
        assert blog_point.text == self.constants.BLOG_BUTTON_TEXT

        podcast_point=self.find_by_contains_text (self.constants.PODCAST_BUTTON_XPATH)
        assert podcast_point.text == self.constants.PODCAST_BUTTON_TEXT

        project_point=self.find_by_contains_text (self.constants.PROJECTS_BUTTON_XPATH)
        assert project_point.text == self.constants.PROJECTS_BUTTON_TEXT

    def check_change_language_ru(self):
        # 2. Find button RUS and click on it
        self.wait_and_click (By.XPATH, locator=self.constants.BUTTON_CHANGE_LANGUAGE_RUS_XPATH)
        self.log.info ("Find button RUS and click on it")

        # 3 Verify that page change language
        main_point_rus=self.find_by_contains_text (self.constants.MAIN_BUTTON_RU_XPATH)
        assert main_point_rus.text == self.constants.MAIN_BUTTON_RU_TEXT

        news_point_rus=self.find_by_contains_text (self.constants.NEWS_BUTTON_RU_XPATH)
        assert news_point_rus.text == self.constants.NEWS_BUTTON_RU_TEXT

        public_point_rus=self.find_by_contains_text (self.constants.PUBLIC_BUTTON_RU_XPATH)
        assert public_point_rus.text == self.constants.PUBLIC_BUTTON_RU_TEXT

        column_point_rus=self.find_by_contains_text (self.constants.COLUMN_BUTTON_RU_XPATH)
        assert column_point_rus.text == self.constants.COLUMN_BUTTON_RU_TEXT

        interview_point_rus=self.find_by_contains_text (self.constants.INTERVIEW_BUTTON_RU_XPATH)
        assert interview_point_rus.text == self.constants.INTERVIEW_BUTTON_RU_TEXT

        reportage_point_rus=self.find_by_contains_text (self.constants.REPORTAGE_BUTTON_RU_XPATH)
        assert reportage_point_rus.text == self.constants.REPORTAGE_BUTTON_RU_TEXT

        blog_point_rus=self.find_by_contains_text (self.constants.BLOG_BUTTON_RU_XPATH)
        assert blog_point_rus.text == self.constants.BLOG_BUTTON_RU_TEXT

        podcast_point_rus=self.find_by_contains_text (self.constants.PODCAST_BUTTON_RU_XPATH)
        assert podcast_point_rus.text == self.constants.PODCAST_BUTTON_RU_TEXT

        project_point_rus=self.find_by_contains_text (self.constants.PROJECTS_BUTTON_RU_XPATH)
        assert project_point_rus.text == self.constants.PROJECTS_BUTTON_RU_TEXT

        archive_point_rus=self.find_by_contains_text (self.constants.ARCHIVE_BUTTON_RU_XPATH)
        assert archive_point_rus.text == self.constants.ARCHIVE_BUTTON_RU_TEXT

    def all_section_button(self):
        """Click on All Section button"""
        self.wait_and_click (By.XPATH, locator=self.constants.ALL_POINTS_BUTTON_XPATH)

    def error_message_empty_registration(self):
        """Error message information about empty fields in registration form"""
        self.find_by_contains_text (ProfilePage.REGISTRATION_EMPTY_ERROR_MESSAGE_XPATH)
        error_message=self.find_by_contains_text (ProfilePage.REGISTRATION_EMPTY_ERROR_MESSAGE_XPATH)
        assert error_message.text == ProfilePage.REGISTRATION_EMPTY_ERROR_MESSAGE_TEXT

    def error_message_invalid_registration(self):
        """Error message information about invalid fields in registration form"""
        error_message=self.find_by_contains_text (ProfilePage.REGISTRATION_INVALID_LOGIN_XPATH)
        assert error_message.text == ProfilePage.REGISTRATION_INVALID_LOGIN_TEXT

    def login_error_message_empty_fields(self):
        """Error message information about empty fields in login form"""
        login_error_message=self.find_by_contains_text (ProfilePage.LOGIN_EMPTY_ERROR_MESSAGE_XPATH)
        assert login_error_message.text == ProfilePage.LOGIN_EMPTY_ERROR_MESSAGE_TEXT

    def login_error_message_invalid_fields(self):
        login_error_message=self.find_by_contains_text (ProfilePage.LOGIN_INVALID_ERROR_MESSAGE_XPATH)
        assert login_error_message.text == ProfilePage.LOGIN_INVALID_ERROR_MESSAGE_TEXT

    def find_icons_on_start_page(self):
        facebook_icon=self.find_by_contains_text (self.constants.FACEBOOK_ICON_XPATH)
        facebook_icon.is_displayed ()

        twitter_icon=self.find_by_contains_text (self.constants.TWITTER_ICON_XPATH)
        twitter_icon.is_displayed ()

        telegram_icon=self.find_by_contains_text (self.constants.TELEGRAM_ICON_XPATH)
        telegram_icon.is_displayed ()

        youtube_icon=self.find_by_contains_text (self.constants.YOUTUBE_ICON_XPATH)
        youtube_icon.is_displayed ()

        instagram_icon=self.find_by_contains_text (self.constants.INSTAGRAM_ICON_XPATH)
        instagram_icon.is_displayed ()

        rss_icon=self.find_by_contains_text (self.constants.RSS_ICON_XPATH)
        rss_icon.is_displayed ()

    def five_menu_points_mein_menu(self):
        advertising_button=self.find_by_contains_text (self.constants.ADVERTISING_BUTTON_XPATH)
        assert advertising_button.text == self.constants.ADVERTISING_BUTTON_TEXT
        advertising_button.is_displayed ()

        privacy_policy_button=self.find_by_contains_text (self.constants.PRIVACY_BUTTON_XPATH)
        assert privacy_policy_button.text == self.constants.PRIVACY_BUTTON_TEXT
        privacy_policy_button.is_displayed ()

        rules_button=self.find_by_contains_text (self.constants.RULES_BUTTON_XPATH)
        assert rules_button.text == self.constants.RULES_BUTTON_TEXT
        rules_button.is_displayed ()

        principles_button=self.find_by_contains_text (self.constants.PRINCIPLES_BUTTON_XPATH)
        assert principles_button.text == self.constants.PRINCIPLES_BUTTON_TEXT
        principles_button.is_displayed ()

        write_button=self.find_by_contains_text (self.constants.WRITE_BUTTON_XPATH)
        assert write_button.text == self.constants.WRITE_BUTTON_TEXT
        write_button.is_displayed ()

    def find_tap_button(self):
        element=self.find_by_contains_text (self.constants.TAP_BUTTON_XPATH).text
        assert element == self.constants.ELEMENT_TAP_TEXT

    def find_club_tap(self):
        element_club=self.find_by_contains_text (self.constants.TAP_CLUB_XPATH).text
        assert element_club == self.constants.TAP_CLUB_TEXT

    def find_search_result_message(self):
        search_result=self.find_by_contains_text (self.constants.FIND_RESULT_XPATH)
        assert search_result.text == self.constants.FIND_RESULT_TEXT

    def find_error_message_invalid_search(self):
        search_result=self.find_by_contains_text (self.constants.SEARCH_ERROR_MESSAGE_XPATH)
        assert search_result.text == self.constants.SEARCH_ERROR_MESSAGE_TEXT
