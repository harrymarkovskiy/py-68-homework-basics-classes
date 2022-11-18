class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    grades = {}

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
 
best_student = Student('Harry', 'Markovskiy', 'male')
best_student.courses_in_progress += ['Python']
 
cool_reviewer = Reviewer('Christopher', 'Robin')
cool_reviewer.courses_attached += ['Python']

cool_lecturer = Lecturer('Albus', 'Dumbledore')
cool_lecturer.courses_attached += ['Django']

bad_lecturer = Lecturer('Fred', 'Krueger')
bad_lecturer.courses_attached += ['Soft Skills']
 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

print(f"\nСтудент {best_student.name} {best_student.surname}")
print(f"Домашнюю работу проверял {cool_reviewer.name} {cool_reviewer.surname}")
print(best_student.grades)

print(f"\nЛучший лектор {cool_lecturer.name} {cool_lecturer.surname}") 