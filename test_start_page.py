"""Store tests related to start page"""

from conftest import BaseTest
from constants.login_page import LoginPageConstants
from constants.profile_page import ProfilePage


class TestLoginPage (BaseTest):

    def test_registration_empty_fields_error(self, start_page):
        """
        1 Open page;
        2 Click 'Доступ' button;
        3 Click 'Увійти' button;
        4 Login with empty fields
        5 Verify error message.
        """

        # Click 'Доступ' button, Click 'Увійти' button
        start_page.button_assess_and_enter ()
        self.log.info ("Click 'Увійти' button")

        # Login with empty fields
        start_page.new_registration (email="", username="", password="", double_password="")

        # Verify error message.
        start_page.error_message_empty_registration ()
        self.log.info ("Registration error message match to expected")

    def test_registration_invalid_fields_error(self, start_page):
        """
        1 Open page;
        2 Click 'Доступ' button;
        3 Click 'Увійти' button;
        4 Clear fields and add invalid fields;
        5 Press button 'Зареєструватися';
        6 Verify error message.
        """

        # Click 'Доступ' button, Click 'Увійти' button
        start_page.button_assess_and_enter ()
        self.log.info ("Click 'Увійти' button")

        # Press button checkbox 'Agree'
        agree_button=start_page.find_by_contains_text (ProfilePage.AGREE_BUTTON_XPATH)
        agree_button.click ()

        # Press radio button Female
        female_button=start_page.find_by_contains_text (ProfilePage.FEMALE_RADIO_BUTTON_XPATH)
        female_button.click ()

        # Clear fields and add invalid fields
        start_page.new_registration (email=f"email{self.variety}@gmail.com", username=f"Name{self.variety}",
                                     password="PassWord123",
                                     double_password="PassWord123")

        # Verify error message.
        start_page.error_message_invalid_registration ()
        self.log.info ("Registration error message match to expected")

    def test_login_empty_fields_error(self, start_page):
        """
        1 Open page;
        2 Click 'Доступ' button;
        3 Click 'Увійти' button;
        4 Clear login fields;
        5 Press button 'Увійти';
        6 Verify login error message.
        """

        # Click 'Доступ' button, Click 'Увійти' button
        start_page.button_assess_and_enter ()
        self.log.info ("Click 'Увійти' button")

        # Clear fields
        start_page.login (email="", password="")
        self.log.info ("Clear email and login fields")

        # Verify login error message
        start_page.login_error_message_empty_fields ()
        self.log.info ("Login error message match to expected")

    def test_login_invalid_fields_error(self, start_page):
        """
        1 Open page;
        2 Click 'Доступ' button;
        3 Click 'Увійти' button;
        4 Clear login fields and add invalid values;
        5 Press button 'Увійти';
        6 Verify login error message.
        """

        # Click 'Доступ' button, Click 'Увійти' button
        start_page.button_assess_and_enter ()
        self.log.info ("Click 'Увійти' button")

        # Clear fields and add login invalid fields
        start_page.login (email=f"user{self.variety}@gmail.com", password=f"PassWord{self.variety}")

        # Verify login error message
        start_page.login_error_message_invalid_fields ()
        self.log.info ("Login error message match to expected")

    def test_success_search_result(self, start_page):
        """
        1 Open start page;
        2 Click on All Sections button;
        3 Clear Search field and write word 'День Незалежності';
        4 Click on button Search
        5 Verify that search function working expectedly.
        """

        # Find button All Sections click on it, Clear Search field and write word 'День Незалежності', Click button Search
        start_page.search (search_field="День Незалежності")
        self.log.info ("Find results")

        # Verify that search function working expectedly
        start_page.find_search_result_message ()
        self.log.info ("Verify that search function working expectedly")

    def test_invalid_search_result(self, start_page):
        """
        1 Open start page;
        2 Click on All Sections button;
        3 Clear Search field and write word 'BLA';
        4 Click on button Search
        5 Verify error message.
        """

        # Find button All Sections click on it, Clear Search field and add invalid filed, Click on Search button
        start_page.search (search_field="BLA")

        # Verify error message
        start_page.find_error_message_invalid_search ()
        search_result=start_page.find_by_contains_text (LoginPageConstants.SEARCH_ERROR_MESSAGE_XPATH)
        assert search_result.text == LoginPageConstants.SEARCH_ERROR_MESSAGE_TEXT
        self.log.info ("Error message match to expected")

    def test_russian_language_menu(self, start_page):
        """
        1 Open start page;
        2 Find button RUS and click on it;
        3 Verify that page change menu language.
        """

        # Find button RUS and click on it, Verify that page change language.
        start_page.check_change_language_ru ()
        self.log.info ("Verify that page change menu language")

    def test_all_menu_points(self, start_page):
        """
        1 Open start page;
        2 Find button All Sections click on it;
        3 Verify that this section contain 8 menu points;
        4 Send click on All Sections button;
        5 Verify that after second click on user back to main menu.
        """

        # Find button All Sections click on it
        start_page.all_section_button ()
        self.log.info ("Find button All Sections click on it")

        # Verify that this section contain 8 menu points
        start_page.check_menu_in_ukr ()
        self.log.info ("Section contain 8 menu points on Ukrainian")

        # Send click on All Sections button
        start_page.all_section_button ()
        self.log.info ("Find button All Sections click on it")

        # Verify that after second click - user back to main menu
        main_menu_button=start_page.find_by_contains_text (LoginPageConstants.MAIN_BUTTON_RU_XPATH)
        assert main_menu_button.text == LoginPageConstants.MAIN_BUTTON_UKR_TEXT
        self.log.info ("Verify that after second click - user back to main menu")

    def test_tap(self, start_page):
        """
        1 Open page;
        2 Click Login in club button;
        3 Verify tap 'Толока УП' clickable and present text;
        """

        # Click login button
        club_button=start_page.find_by_contains_text (LoginPageConstants.CLUB_TAP_XPATH)
        club_button.click ()
        self.log.info ("Click Exit button")

        # Click tap
        tap_button=start_page.find_by_contains_text (LoginPageConstants.TAP_BUTTON_XPATH)
        tap_button.click ()

        # Find element tap
        start_page.find_tap_button ()
        self.log.info ("Verify tap 'Толока УП' clickable and present text")

    def test_club_tap(self, start_page):
        """
        1 Open page;
        2 Click Login in club button;
        3 Verify tap 'Клуб УП' clickable and present text;
        """

        # Click Login in button
        club_button=start_page.find_by_contains_text (LoginPageConstants.CLUB_TAP_XPATH)
        club_button.click ()
        self.log.info ("Click Exit button")

        # Click tap 'Club'
        tap_club_button=start_page.find_by_contains_text (LoginPageConstants.TAP_CLUB_XPATH)
        tap_club_button.click ()

        # Find tap 'Клуб УП'
        start_page.find_club_tap ()
        self.log.info ("Verify tap 'Клуб УП' clickable and present text")

    def test_social_media_icons(self, start_page):
        """
        1 Open start page;
        2 Verify that 6 icons present in Main page;
        """

        # Find and verify that 6 icons present in Main page displayed for user ;
        start_page.find_icons_on_start_page ()
        self.log.info ("Verify that 6 social media icons present in Main page and displayed for user")

    def test_footer_menu(self, start_page):
        """
        1 Open start page;
        2 Verify that present 5 Menu point in Footer;
        """

        # Find and verify that 5 Menu in Main page displayed for user;
        start_page.five_menu_points_mein_menu ()
        self.log.info ("Verify that 5 Menu point is present and shown for user in Footer")
