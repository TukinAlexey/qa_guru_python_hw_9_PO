import os

from selene import browser, have


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.user_email = browser.element('#userEmail')
        self.gender = browser.element('[for="gender-radio-1"]')
        self.user_number = browser.element('#userNumber')
        self.subjects = browser.element('#subjectsInput')
        self.hobbies = browser.element('[for="hobbies-checkbox-1"]')
        self.upload_pictures = browser.element('#uploadPicture')
        self.current_address = browser.element('#currentAddress')
        self.state = browser.element('#react-select-3-input')
        self.city = browser.element('#react-select-4-input')
        self.submit = browser.element('#submit')
        self.registered_user = browser.all('td')
        self.registered_user_2 = browser.element('.table').all('td')

    def fill_first_name(self, value):
        self.first_name.type(value)

    def fill_last_name(self, value):
        self.last_name.type(value)

    def fill_user_email(self, value):
        self.user_email.type(value)

    def fill_gender(self):
        self.gender.click()

    def fill_user_number(self, value):
        self.user_number.type(value)

    def fill_date_of_birth(self):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element('[value="0"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element('[value="1991"]').click()
        browser.element('[aria-label="Choose Tuesday, January 1st, 1991"]').click()

    def fill_subjects(self, value):
        self.subjects.type(value).press_enter()

    def fill_hobbies(self):
        self.hobbies.click()

    def fill_picture(self):
        my_picture = 'Picture.png'
        self.upload_pictures.send_keys(os.path.abspath(my_picture))

    def fill_current_address(self, value):
        self.current_address.type(value)

    def fill_state(self, value):
        self.state.type(value).press_enter()

    def fill_city(self, value):
        self.city.type(value).press_enter()

    def fill_submit(self):
        self.submit.click()

    def registered_user_with(self):
        self.registered_user.should(have.exact_texts(
            'Student Name', 'Иван Иванов', 'Student Email',
            'test@test.com', 'Gender', 'Male', 'Mobile', '9999999999',
            'Date of Birth', '01 January,1991', 'Subjects', 'English',
            'Hobbies', 'Sports', 'Picture', 'Picture.png', 'Address',
            'RF. Moscow, Arbat, 1', 'State and City', 'Haryana Karnal',
        )
        )

    def registered_user_with_2(self, student_name, student_email, gender, mobile, date_of_birth, subjects, hobbies,
                               picture, address, state_and_city):
        self.registered_user_2.even.should(have.exact_texts(
            student_name, student_email, gender, mobile,
            date_of_birth, subjects,
            hobbies, picture, address, state_and_city,
        )
        )
