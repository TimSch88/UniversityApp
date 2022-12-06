from UniversityApp.DataFile import university_data


class Account:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.__email = None
        self.__phone = None

    def account_register(self):
        self.first_name = input('fn:')
        self.last_name = input('ln:')

        self.set_email(input('email:'))
        while self.__email is None:
            self.set_email(input('email:'))

        self.set_phone(input('phone:'))
        while self.__phone is None:
            self.set_phone(input('phone:'))

        registration = dict(first_name = self.first_name, last_name = self.last_name, email = self.__email, phone = self.__phone)
        university_data['registrations'].append(registration)
        print('Acount registered succesfully')

    def set_phone(self, phone):
        if len(str(phone)) == 10:
            self.__phone = phone
        else:
            print('You have entered invalid number')

    def get_phone(self):
        return self.__phone

    def set_email(self, email):
        if '@' in (email):
            self.__email = email

        else:
            print('You have entered invalid email')


    def get_email(self):
        return self.__email
