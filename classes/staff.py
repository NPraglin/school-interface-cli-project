#staff.py
from .creator_ultimate_v1 import creator_ultimate_v1
import os
my_path = os.path.abspath(os.path.dirname(__file__))
path_staff = os.path.join(my_path, "../data/staff.csv")


class Staff:
    def __init__(self, name, age, role, employee_id, password):
        self.name = name 
        self.age = age         
        self.password = password
        self.role = role
        self.employee_id = employee_id

    @staticmethod
    def all_staff():
        return creator_ultimate_v1(path_staff, Staff)
   

    def __str__(self):
        return f"Staff member: {self.name}"

