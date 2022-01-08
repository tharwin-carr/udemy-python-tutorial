'''
Object Oriented Programming
'''

class Student:

    school= 'Online School'
    number_of_students = 0

    def __init__(self, first_name, last_name, major):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major

        Student.number_of_students += 1

    def fullname_with_major(self):
        return f'{self.first_name} {self.last_name} is a {self.major} major.'

    def fullname_major_school(self):
        return f'{self.first_name} {self.last_name} is a {self.major} major going to {self.school}.'



print(f'Number of students = {Student.number_of_students}')
student_1 = Student('Eric', 'Roby', 'Computer Science')
student_2 = Student('John', 'Miller', 'Math')
print(f'Number of students = {Student.number_of_students}')