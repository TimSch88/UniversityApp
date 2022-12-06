import csv
from UniversityApp.Student import Student
from UniversityApp.Teacher import Teacher
from UniversityApp.Staff import Staff
import prettytable as pt

def csv_to_object(csv_file_obj, target_obj):
    item_list = []
    for item in list(csv_file_obj)[1:]:
        obj_dict = target_obj.__dict__
        for i, x in enumerate(list(obj_dict.keys())):
            obj_dict[x] = item[i]

        item_list.append(obj_dict)
    return item_list

def read_csv_main(file_name, role, data_list):
    try:
        obj_csv = open(file_name, 'r')
        obj_list = csv.reader(obj_csv)

        for obj in list(obj_list)[1:]:
            object = None
            if role == 'student':
                object = Student()
                object.first_name, object.last_name, object_email, object_phone, object.major, object.semester = obj

            elif role == 'teacher':
                object = Teacher()
                object.first_name, object.last_name, object_email, object_phone, object.department = obj

            elif role == 'staff':
                object = Staff()
                object.first_name, object.last_name, object_email, object_phone, object.department = obj

            object.set_email(object_email)
            object.set_phone(object_phone)
            data_list.append(object)

    except:
        pass
    return data_list




def write_to_csv(file_name, object, stats, type):
    field_names = list(object.__dict__.keys())
    with open(file_name, 'a', newline='') as file_writer:
        csv_writer = csv.writer(file_writer)
        if stats[type] == 0:
            csv_writer.writerow(field_names)
        if type == 'student':
            csv_writer.writerow([object.first_name, object.last_name, object.get_email(), object.get_phone(), object.major, object.semester])
        if type == 'teacher':
            csv_writer.writerow([object.first_name, object.last_name, object.get_email(), object.get_phone(), object.department])
        if type == 'staff':
            csv_writer.writerow([object.first_name, object.last_name, object.get_email(), object.get_phone(), object.department])
        stats[type] += 1

def print_data(type, data_list, title, field_names):
    table = pt.PrettyTable()
    table.title = title
    table.field_names = field_names
    for obj in data_list:
        if type == 'student':
            table.add_row([obj.first_name, obj.last_name, obj.get_email(), obj.get_phone(), obj.major, obj.semester])
        elif type == 'teacher':
            table.add_row([obj.first_name, obj.last_name, obj.get_email(), obj.get_phone(), obj.department])
        elif type == 'staff':
            table.add_row([obj.first_name, obj.last_name, obj.get_email(), obj.get_phone(), obj.department])
    print(table)


def register_save(object, data_list, file_name, stats, type):
    object.register()
    data_list.append(object)
    write_to_csv(file_name, object, stats, type)


def delete_record(name, email, data_list):
    for record in data_list:
        if record.first_name == name and record.get_email() == email:
            data_list.remove(record)
            print(f'Account {record.first_name} and {record.get_email()}  has been deleted successfully.')

def update_csv(data_list, file_name, object):
    field_names = list(object().__dict__.keys())
    with open(file_name, 'w', newline='') as file_writer:
        csv_writer = csv.writer(file_writer)
        csv_writer.writerow(field_names)
        if object == Student:
            for obj in data_list:
                csv_writer.writerow([obj.first_name, obj.last_name, obj.get_email(), obj.get_phone(), obj.major, obj.semester])
        if object == Teacher:
            for obj in data_list:
                csv_writer.writerow([obj.first_name, obj.last_name, obj.get_email(), obj.get_phone(), obj.department])
        if object == Staff:
            for obj in data_list:
                csv_writer.writerow([obj.first_name, obj.last_name, obj.get_email(), obj.get_phone(), obj.department])

def update_account(name, email, data_list):
    for record in data_list:
        if record.first_name == name and record.get_email() == email:
            choice = input('''
            Enter name of field to update.
            press x key to exit.
            >>:
            ''')
            while choice != 'x':
                value = input(f'Enter name of new data for {choice}: >>')
                record.update_field(choice, value)

                print('Account updated succesfully.')
                choice = input('''
                        Enter name of field to update.
                        press x key to exit.
                        >>:
                        ''')

def search_by_value(data_list, lookup_value):
    value_list = []
    for obj in data_list:
        if lookup_value == 'Major':
            if obj.major == lookup_value:
                value_list.append(obj)
        elif lookup_value == 'Semester':
            if obj.semester == lookup_value:
                value_list.append(obj)
    return value_list
