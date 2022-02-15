from .staff import *;
from .student import *;
import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
path_student = os.path.join(my_path, "../data/students.csv")


class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.all_staff()
        self.students = Student.all_students()

    def enroll_student(self, data):
        with open(path_student, 'a', newline='\n') as csvfile:
            csv_w = csv.writer(csvfile)

            csv_w.writerow(data)
            
    def erase_student(self, id):
        # with open(path_student, 'rb') as csvfile:
        #     csv_d = csv.writer(csvfile)

        #     for row in csvfile:
        #         if row[3] == id:
        #             print(f"{row[0]} deleted")
        print('**Student Deleted from CSV**')