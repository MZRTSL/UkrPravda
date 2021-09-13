class LoginPageConstants:
    """Store constants related to Login Page"""

    # Registration form (https://dostup.pravda.com.ua/profile/sign_in?r=%2F)
    EMAIL_REGISTRATION_XPATH='//*[@id="user_signup_email"]'
    USERNAME_REGISTRATION_XPATH='//*[@id="user_signup_name"]'
    PASSWORD_REGISTRATION_XPATH='//*[@id="user_signup_password"]'
    DOUBLE_PASSWORD_REGISTRATION_XPATH='//*[@id="user_signup_password_confirmation"]'

    # Login form (https://dostup.pravda.com.ua/profile/sign_in?r=%2F)
    EMAIL_LOGIN_XPATH='//*[@id="user_signin_email"]'
    PASSWORD_LOGIN_XPATH='//*[@id="user_signin_password"]'

    # Buttons
    REGISTRATION_BUTTON_XPATH='.//*[@id="signup_form"]/div[2]/input[3]'
    REGISTRATION_BUTTON_TEXT='Зареєструватися'

    LOGIN_BUTTON_XPATH='//*[@id="signin_form"]/div/input[3]'
    LOGIN_BUTTON_TEXT='Увійти'

    BUTTON_CHANGE_LANGUAGE_RUS_XPATH='.//html/body/header/div/div/div[1]/div[2]/a[1]/span/span'
    ALL_POINTS_BUTTON_XPATH='.//html/body/header/div/div/div[1]/div[1]/a/span[2]'

    # Menu points
    MAIN_BUTTON_XPATH='.//html/body/header/div/div/div[2]/div/div/div[3]/div[2]/nav[1]/ul/li[1]/a'
    MAIN_BUTTON_TEXT="НОВИНИ"
    PUBLIC_BUTTON_XPATH='.//html/body/header/div/div/div[2]/div/div/div[3]/div[2]/nav[1]/ul/li[2]/a'
    PUBLIC_BUTTON_TEXT="ПУБЛІКАЦІЇ"
    COLUMN_BUTTON_XPATH='.//html/body/header/div/div/div[2]/div/div/div[3]/div[2]/nav[1]/ul/li[3]/a'
    COLUMN_BUTTON_TEXT="КОЛОНКИ"
    INTERVIEW_BUTTON_XPATH='.//html/body/header/div/div/div[2]/div/div/div[3]/div[2]/nav[1]/ul/li[4]/a'
    INTERVIEW_BUTTON_TEXT="ІНТЕРВ'Ю"
    REPORTAGE_BUTTON_XPATH='.//html/body/header/div/div/div[2]/div/div/div[3]/div[2]/nav[1]/ul/li[5]/a'
    REPORTAGE_BUTTON_TEXT="РЕПОРТАЖ"
    BLOG_BUTTON_XPATH='.//html/body/header/div/div/div[2]/div/div/div[3]/div[2]/nav[1]/ul/li[6]/a'
    BLOG_BUTTON_TEXT="БЛОГИ"
    PODCAST_BUTTON_XPATH='.//html/body/header/div/div/div[2]/div/div/div[3]/div[2]/nav[1]/ul/li[7]/a'
    PODCAST_BUTTON_TEXT="ПОДКАСТИ"
    PROJECTS_BUTTON_XPATH='.//html/body/header/div/div/div[2]/div/div/div[3]/div[2]/nav[1]/ul/li[8]/a'
    PROJECTS_BUTTON_TEXT="СПЕЦПРОЄКТИ"

    CLUB_TAP_XPATH='/html/body/header/div/div/div[1]/div[2]/a[2]/span'
    TAP_BUTTON_XPATH='//*[@id="join_to_us"]/div[1]/div[1]/div[1]'
    ELEMENT_TAP_TEXT='Толока УП'
    TAP_CLUB_XPATH='//*[@id="join_to_us"]/div[1]/div[1]/div[2]'
    TAP_CLUB_TEXT='Клуб УП'
    MAIN_BUTTON_UKR_TEXT="ГОЛОВНА"

    # Menu points in Russian language
    MAIN_BUTTON_RU_XPATH='.//html/body/nav[2]/ul/li[1]/a'
    MAIN_BUTTON_RU_TEXT="ГЛАВНАЯ"
    NEWS_BUTTON_RU_XPATH='.//html/body/nav[2]/ul/li[2]/a'
    NEWS_BUTTON_RU_TEXT="НОВОСТИ"
    PUBLIC_BUTTON_RU_XPATH='.//html/body/nav[2]/ul/li[3]/a'
    PUBLIC_BUTTON_RU_TEXT="ПУБЛИКАЦИИ"
    COLUMN_BUTTON_RU_XPATH='.//html/body/nav[2]/ul/li[4]/a'
    COLUMN_BUTTON_RU_TEXT="КОЛОНКИ"
    INTERVIEW_BUTTON_RU_XPATH='.//html/body/nav[2]/ul/li[5]/a'
    INTERVIEW_BUTTON_RU_TEXT="ИНТЕРВЬЮ"
    REPORTAGE_BUTTON_RU_XPATH='.//html/body/nav[2]/ul/li[6]/a'
    REPORTAGE_BUTTON_RU_TEXT="РЕПОРТАЖ"
    BLOG_BUTTON_RU_XPATH='.//html/body/nav[2]/ul/li[7]/a'
    BLOG_BUTTON_RU_TEXT="БЛОГИ"
    PODCAST_BUTTON_RU_XPATH='.//html/body/nav[2]/ul/li[8]/a'
    PODCAST_BUTTON_RU_TEXT="ПОДКАСТЫ"
    PROJECTS_BUTTON_RU_XPATH='.//html/body/nav[2]/ul/li[9]/a'
    PROJECTS_BUTTON_RU_TEXT="СПЕЦПРОЕКТЫ"
    ARCHIVE_BUTTON_RU_XPATH='.//html/body/nav[2]/ul/li[10]/a'
    ARCHIVE_BUTTON_RU_TEXT="АРХИВ"

    # Search
    SEARCH_BUTTON_XPATH='.//html/body/header/div/div/div[2]/div/div/div[2]/div/form/input[2]'
    SEARCH_BUTTON_TEXT='Знайти'
    SEARCH_FIELD_XPATH='.//html/body/header/div/div/div[2]/div/div/div[2]/div/form/input[1]'

    FIND_RESULT_XPATH='.//html/body/div[3]/div/div[1]/div[4]/div[3]/div/div[2]/div[1]/h4/a'
    FIND_RESULT_TEXT='Патріарх Варфоломій приїде до України на День Незалежності – нардеп'

    SEARCH_ERROR_MESSAGE_XPATH='.//html/body/div[3]/div/div[1]/div[2]'
    SEARCH_ERROR_MESSAGE_TEXT="За вашим запитом нічого не знайдено"

    # Social Media
    FACEBOOK_ICON_XPATH='.//html/body/footer/div/div[1]/div[2]/a[1]/img'
    TWITTER_ICON_XPATH='.//html/body/footer/div/div[1]/div[2]/a[2]/img'
    TELEGRAM_ICON_XPATH='.//html/body/footer/div/div[1]/div[2]/a[3]/img'
    YOUTUBE_ICON_XPATH='.//html/body/footer/div/div[1]/div[2]/a[4]/img'
    INSTAGRAM_ICON_XPATH='.//html/body/footer/div/div[1]/div[2]/a[5]/img'
    RSS_ICON_XPATH='.//html/body/footer/div/div[1]/div[2]/a[6]/img'

    # 5 Menu point in Footer
    ADVERTISING_BUTTON_XPATH='.//html/body/footer/div/nav/ul/li[1]/a'
    ADVERTISING_BUTTON_TEXT="РЕКЛАМА НА САЙТІ"

    PRIVACY_BUTTON_XPATH='.//html/body/footer/div/nav/ul/li[2]/a'
    PRIVACY_BUTTON_TEXT="ПОЛІТИКА КОНФІДЕНЦІЙНОСТІ"

    RULES_BUTTON_XPATH='.//html/body/footer/div/nav/ul/li[4]/a'
    RULES_BUTTON_TEXT="ПРАВИЛА ВИКОРИСТАННЯ МАТЕРІАЛІВ УП"

    PRINCIPLES_BUTTON_XPATH='.//html/body/footer/div/nav/ul/li[5]/a'
    PRINCIPLES_BUTTON_TEXT="ПРИНЦИПИ І ПРАВИЛА РОБОТИ УП"

    WRITE_BUTTON_XPATH='.//html/body/footer/div/nav/ul/li[6]/a'
    WRITE_BUTTON_TEXT="ЯК ПИСАТИ ДЛЯ УП"
