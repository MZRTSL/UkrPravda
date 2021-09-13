class ProfilePage:
    """Store constants related to Profile page"""

    # Buttons
    ACCESS_BUTTON_XPATH='/html/body/nav[1]/ul/li[9]/a'
    ACCESS_BUTTON_TEXT='Доступ'
    ENTER_BUTTON_XPATH='//*[@id="banner-inner"]/div[2]/section[4]/a[2]/span'
    ENTER_BUTTON_TEXT='Увійти'

    # Registration form
    AGREE_BUTTON_XPATH='.//*[@id="signup_form"]/p[6]/label'
    FEMALE_RADIO_BUTTON_XPATH='.//*[@id="user_signup_gender_female"]'

    # Registration form - error message
    REGISTRATION_EMPTY_ERROR_MESSAGE_XPATH='.//*[@id="error"]'
    REGISTRATION_EMPTY_ERROR_MESSAGE_TEXT='Ви маєте погодитись на використання вашої персональної інформації. Поставте, будь ласка, відповідну галочку.'

    LOGIN_EMPTY_ERROR_MESSAGE_XPATH='//*[@id="errorExplanation"]/ul/li'
    LOGIN_EMPTY_ERROR_MESSAGE_TEXT='Адреса або пароль не були розпізнані, спробуйте ще раз. Або створіть новий обліковий запис.'

    REGISTRATION_INVALID_LOGIN_XPATH='.//*[@id="signup_form"]/p[2]'
    REGISTRATION_INVALID_LOGIN_TEXT="Адреса вашої електронної пошти не повідомляється розпоряднику інформації та не оприлюднюється на сайті (розпорядник отримує електронний лист з адреси сайту"

    LOGIN_INVALID_ERROR_MESSAGE_XPATH='.//*[@id="errorExplanation"]/ul/li'
    LOGIN_INVALID_ERROR_MESSAGE_TEXT='Адреса або пароль не були розпізнані, спробуйте ще раз. Або створіть новий обліковий запис.'
