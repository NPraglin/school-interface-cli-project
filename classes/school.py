from .staff import *;
from .student import *;


class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.all_staff()
        self.students = Student.all_students()
