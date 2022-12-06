from UniversityApp.Staff import Staff
from UniversityApp.Student import Student
from UniversityApp.Teacher import Teacher
import prettytable as pt
import csv
# from DatabaseConfig import university_db
from UtilitiesFunction import *

# mycursor = university_db.cursor()
# mycursor.execute('CREATE DATABASE University')


class UniversityAdmin:
    def __init__(self):
        self.registrations = []
        self.students = []
        self.teachers = []
        self.staff = []
        self.data_files = {'Student': 'Students.csv', 'Teacher': 'Teachers.csv', 'Staff': 'Staff.csv'}
        self.read_csv()
        self.stats = {'student': len(self.students), 'teacher': len(self.teachers), 'staff': len(self.staff)}
        self.data_table = {1: self.students, 2: self.teachers, 3: self.staff}


    def read_csv(self):

        self.students = read_csv_main(self.data_files['Student'], 'student', self.students)
        self.teachers = read_csv_main(self.data_files['Teacher'], 'teacher', self.teachers)
        self.staff = read_csv_main(self.data_files['Staff'], 'staff', self.staff)


    def dashboard(self):
        dash = '''
        Please press :
        1. to register as student
        2. to register as teacher
        3. to register as staff
        4. Display University Admin Data
        :>>'''
        choice = int(input(dash))
        return choice

    def run(self):
        choice = self.dashboard()
        while 0 < choice < 5:
            if choice == 1:
                student = Student()
                register_save(student, self.students, self.data_files['Student'], self.stats, 'student')
                # student.register()
                # self.students.append(student)
                # write_to_csv(self.data_files['Student'], student, self.stats, 'Student')

            elif choice == 2:
                teacher = Teacher()
                register_save(teacher, self.teachers, self.data_files['Teacher'], self.stats, 'teacher')

            elif choice == 3:
                staff = Staff()
                register_save(staff, self.staff, self.data_files['Staff'], self.stats, 'staff')

            elif choice == 4:
                self.display_data()

            else:
                print('Incorrect input.')

            choice = self.dashboard()

    def display_data(self):
        print('University DataBase')
        print(f'Number of students enrolled: {len(self.students)}')
        print(f'Number of teachers enrolled: {len(self.teachers)}')
        print(f'Number of staff enrolled: {len(self.staff)}')
        choice = int(input('''
        1. Students records
        2. Teachers records
        3. Staff records
        4. Back to registration
        :>>'''))
        data_list = None
        file_name = None
        file_object = None

        while 0 < choice < 8:
            if choice == 1:
                print_data('student', self.students, 'Student data', ['First Name', 'Last name', 'Email', 'Phone', 'Major', 'Semester'])
                file_name = self.data_files['Student']
                file_object = Student

            elif choice == 2:
                print_data('teacher', self.teachers, 'Teacher data', ['First Name', 'Last name', 'Email', 'Phone', 'Department'])
                file_name = self.data_files['Teacher']
                file_object = Teacher

            elif choice == 3:
                print_data('staff', self.staff, 'Staff data', ['First Name', 'Last name', 'Email', 'Phone', 'Department'])
                file_name = self.data_files['Staff']
                file_object = Staff

            elif choice == 4:
                break

            elif choice == 5:
                name, email = input('Name and email of account to be updated:> ').split(', ')
                update_account(name, email, data_list)
                update_csv(data_list, file_name, file_object)
                self.run()

            elif choice == 6:
                name, email = input('Name and email of account to be deleted:> ').split(', ')
                delete_record(name, email, data_list)
                update_csv(data_list, file_name, file_object)
                self.run()
            elif choice == 7:
                print('''
                Filter by:
                (Major, Semester)
                ''')
                data_list = search_by_value(self.students, input('enter the value you are searching for:> '))
                print_data('student', data_list, 'Student data', ['First Name', 'Last name', 'Email', 'Phone', 'Major', 'Semester'])
                self.run()

            else:
                print('Incorrect input.')
            try:
                data_list = self.data_table[choice]
            except:
                pass
            choice = int(input('''
                    1. Students records
                    2. Teachers records
                    3. Staff records
                    4. Back to registration
                    5. Update account
                    6. Delete from current table
                    7. Filter by
                    :>>'''))
