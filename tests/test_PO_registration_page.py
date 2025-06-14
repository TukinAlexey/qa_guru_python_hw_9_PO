from demoqa_tests.pages.registration_page import RegistrationPage


def test_google_chrome_open(open_browser_chrome):

    registration_page = RegistrationPage()

    registration_page.fill_first_name('Иван')
    registration_page.fill_last_name('Иванов')
    registration_page.fill_user_email('test@test.com')
    registration_page.fill_gender()
    registration_page.fill_user_number('9999999999')
    registration_page.fill_date_of_birth()
    registration_page.fill_hobbies()
    registration_page.fill_picture()
    registration_page.fill_current_address('RF. Moscow, Arbat, 1')
    registration_page.fill_subjects('English')
    registration_page.fill_state('Haryana')
    registration_page.fill_city('Karnal')
    registration_page.fill_submit()

    # Проверка данных в таблице

    registration_page.registered_user_with_2('Иван Иванов', 'test@test.com', 'Male', '9999999999', '01 January,1991',
                                             'English', 'Sports', 'Picture.png', 'RF. Moscow, Arbat, 1',
                                             'Haryana Karnal')
