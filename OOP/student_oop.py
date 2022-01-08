'''
Object Oriented Programming
'''

class Student:
    def __init__(self, first_name, last_name, major):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major

    def fullname_with_major(self):
        return f'{self.first_name} {self.last_name} is a {self.major} major'

student_1 = Student('Eric', 'Roby', 'Computer Science')
student_2 = Student('John', 'Miller', 'Math')

print(student_1.fullname_with_major())
print(Student.fullname_with_major(student_2))