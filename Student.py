from UniversityApp.Account import Account


class Student(Account):
    def __init__(self):
        super().__init__()
        self.major = None
        self.semester = None

    def register(self):
        self.account_register()
        self.major = input('major:')
        self.semester = input('semester:')
        student = dict(first_name=self.first_name, last_name=self.last_name, email=self.get_email(),
                            phone=self.get_phone(), major=self.major, semester=self.semester)
        print('Student added succesfully')
        return student


    def update_field(self, field, value):
        if field == 'first_name':
            self.first_name = value
        elif field == 'last_name':
            self.last_name = value
        elif field == 'email':
            self.set_email(value)
        elif field == 'phone':
            self.set_phone(value)
        elif field == 'major':
            self.major = value
        elif field == 'semester':
            self.semester = value
