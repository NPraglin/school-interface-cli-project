# student.py
from .creator_ultimate_v1 import creator_ultimate_v1
import os
my_path = os.path.abspath(os.path.dirname(__file__))
path_student = os.path.join(my_path, "../data/students.csv")


class Student:
    def __init__(self, **kwargs):
        self.info = {
            'name': kwargs['name'],
            'age': kwargs['age'],     
            'password': kwargs['password'],
            'role': kwargs['role'],
            'school_id': kwargs['school_id']
        }

    def __repr__(self):
        return str(self.info)

    @staticmethod
    def all_students():
        return creator_ultimate_v1(path_student, Student)

    def __str__(self):
        return f"\n{self.__getitem__('name')}\n----------\nAge: {self.__getitem__('age')}\nID: {self.__getitem__('school_id')}\n"

    def __getitem__(self, key):
        return self.info[key]

    def get_id(self):
        return self.__getitem__('school_id')