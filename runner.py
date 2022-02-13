from classes.school import *;
from classes.staff import *;
from classes.student import *;
from classes.creator_ultimate_v1 import creator_ultimate_v1
import sys


# Initialize our student instances
creator_ultimate_v1(path_student, Student)

# Initialize our staff instances
creator_ultimate_v1(path_staff, Staff)

# Initialize our school instances
school_1 = School('RidgeMont High')

# Option 1 on input menu: View all staff
def list_staff_func(x):
    for staff in x:
        print(staff)

# Option 2 on input menu: View all students
def list_student_func(x):
    for student in x:
        print(student)

# Option 3 on input menu: View student by ID
def student_by_id_func(x):
    id = input('Enter a student ID\n')
    for line in x:
        if id == line.get_id():
            print(line)
        

# Input / Output menu
res = input(("\nWhat would you like to do?\nOptions:\n1. List All Staff\n2. View All Students\n3. View Individual Student <student_id>\n4. Add a Student\n5. Remove a Student <student_id>\n6. Quit\n"))

while res != 6:

    if res == '1':
        print(list_staff_func(school_1.staff))

    if res == '2':
        print(list_student_func(school_1.students))

    if res == '3':
        print(student_by_id_func((school_1.students)))
