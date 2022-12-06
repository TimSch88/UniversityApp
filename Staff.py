from UniversityApp.Account import Account


class Staff(Account):
    def __init__(self):
        super().__init__()
        self.department = None

    def register(self):
        self.account_register()
        self.department = input('department:')

        staff = dict(first_name=self.first_name, last_name=self.last_name, email=self.get_email(),
                            phone=self.get_phone(), department=self.department)
        print('Staff added succesfully')
        return staff

    def update_field(self, field, value):
        if field == 'first_name':
            self.first_name = value
        elif field == 'last_name':
            self.last_name = value
        elif field == 'email':
            self.set_email(value)
        elif field == 'phone':
            self.set_phone(value)
        elif field == 'department':
            self.department = value