from .school import School

class SchoolInterface:

    def __init__(self, school_name):
        self.school = School(school_name)
    
    def list_staff_func(self, x):
        for staff in x:
            print(staff)

    def list_student_func(self, x):
        for student in x:
          print(student)

    def student_by_id_func(self, x):
        id = input('Enter a student ID\n')
        for line in x:
            if id == line.get_id():
                return line

    def add_student(self):
        student_data = []
        student_data.append(input('Enter student name:\n'))
        student_data.append(input('Enter student age: \n'))
        student_data.append('Student')
        student_data.append(input('Enter student school id: \n'))
        student_data.append(input('Enter student password: \n'))
        self.school.enroll_student(student_data)
        print(f"{student_data[0]} added successfully")

    def remove_student(self, id):
        id = input('Enter a student ID\n')
        return self.school.erase_student(id)

    def run(self):
        while True: 
            res = input(("\nWhat would you like to do?\nOptions:\n1. List All Staff\n2. View All Students\n3. View Individual Student <student_id>\n4. Add a Student\n5. Remove a Student <student_id>\n6. Quit\n"))

            if res == '1':
                self.list_staff_func(self.school.staff)

            if res == '2':
                self.list_student_func(self.school.students)
                
            if res == '3':
                self.student_by_id_func((self.school.students))

            if res == '4':
                self.add_student()

            if res == '5':
                self.remove_student(self.school.students)

            elif res == '6':
                break
