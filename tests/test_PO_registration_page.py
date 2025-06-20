from demoqa_tests.data.users import User
from demoqa_tests.pages.registration_page import RegistrationPage


def test_google_chrome_open(open_browser_chrome):
    registration_page = RegistrationPage()
    user = User(
        first_name='Иван',
        last_name='Иванов',
        email='test@test.com',
        gender='Male',
        phone_number='9999999999',
        year='1991',
        month='January',
        day='01',
        subjects='English',
        hobbies='Sports',
        picture='Picture.png',
        address='RF. Moscow, Arbat, 1',
        state='Haryana',
        city='Karnal'
    )

    #Заполнение формы
    registration_page.fill_user_registration_form(user)

    # Проверка данных в таблице
    registration_page.check_registered_user(user)