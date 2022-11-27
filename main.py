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

    def hw_average_grade(self):
        if len(self.grades) == 0:
            return 'У студента нет оценок.'
        else:
            total = 0
            list_len_sum = 0
            for grade_list in self.grades.values():
                list_len_sum += len(grade_list)
                for grade in grade_list:
                    total += grade
            return round(total / list_len_sum, 1)

    def __str__(self):
        if not isinstance(self, Student):
            print('Not Student')
            return
        return f"\nИмя студента: {self.name}\nФамилия студента: {self.surname}\nСредняя оценка за домашние задания: {self.hw_average_grade()}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}\n"

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self.hw_average_grade() < other.hw_average_grade()
    
        
class Mentor:
    def __init__(self, name, surname, courses_attached = [] ):
        self.name = name
        self.surname = surname
        self.courses_attached = courses_attached

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname, courses_attached = [] )
        self.grades = {}

    def averagelec_calc(self):
        for k,v in self.grades.items():
            av = sum(v)/ float(len(v))
            return round(av, 1)    

    def __str__(self):
        if not isinstance(self, Lecturer):
            print('Not Lecturer')
            return
        return f"\nИмя лектора: {self.name}\nФамилия лектора: {self.surname}\nСредняя оценка за лекции: {self.averagelec_calc()}"

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return self.averagelec_calc() < other.averagelec_calc()
        

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        if not isinstance(self, Reviewer):
            print('Not Reviewer')
            return
        return f"\nИмя проверяющего: {self.name}\nФамилия: {self.surname}"

# calls

best_student = Student('Harry', 'Markovskiy', 'male')
best_student.courses_in_progress += ['Python', 'Django', 'Soft Skills']
best_student.finished_courses += ['Введение в программирование', 'Photoshop Basics']

some_student = Student('Ron', 'Weasley', 'male')
some_student.courses_in_progress += ['Python', 'Введение в программирование', 'Django']
some_student.finished_courses += ['Soft Skills']

cool_reviewer = Reviewer('Christopher', 'Robin')
cool_reviewer.courses_attached += ['Python', 'Django']

some_reviewer = Reviewer('Vladimir', 'Putin')
some_reviewer.courses_attached += ['Введение в программирование', 'Soft Skills']

cool_lecturer = Lecturer('Albus', 'Dumbledore')
cool_lecturer.courses_attached += ['Django', 'Python']

bad_lecturer = Lecturer('Fred', 'Krueger')
bad_lecturer.courses_attached += ['Soft Skills', 'Photoshop Basics']
 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 5)
cool_reviewer.rate_hw(best_student, 'Python', 7)

cool_reviewer.rate_hw(some_student, 'Django', 3)
cool_reviewer.rate_hw(some_student, 'Django', 4)
cool_reviewer.rate_hw(some_student, 'Django', 3)

some_reviewer.rate_hw(best_student, 'Soft Skills', 2)
some_reviewer.rate_hw(best_student, 'Soft Skills', 5)
some_reviewer.rate_hw(best_student, 'Soft Skills', 7)

some_reviewer.rate_hw(some_student, 'Введение в программирование', 10)
some_reviewer.rate_hw(some_student, 'Введение в программирование', 3)
some_reviewer.rate_hw(some_student, 'Введение в программирование', 4)

best_student.rate_lec(cool_lecturer, 'Django', 10)
best_student.rate_lec(cool_lecturer, 'Django', 7)

best_student.rate_lec(bad_lecturer, 'Soft Skills', 1)
best_student.rate_lec(bad_lecturer, 'Soft Skills', 3)

some_student.rate_lec(cool_lecturer, 'Django', 7)
some_student.rate_lec(cool_lecturer, 'Django', 5)

best_student.rate_lec(bad_lecturer, 'Soft Skills', 10)
best_student.rate_lec(bad_lecturer, 'Soft Skills', 8)

students_list = [best_student, some_student]
lecturers_list = [cool_lecturer, bad_lecturer]

# functions

def st_course_average(some_list, course):
    total_rate = []
    for person in some_list:
        if not isinstance(person, Student):
            return f'{person} не студент.'
        else:
            if course in person.grades:
                total_rate += person.grades[course]
    res = round(sum(total_rate) / len(total_rate), 2)
    print(f'Средняя оценка студентов по курсу {course} = {res}.')
    return

def lecturer_course_average(some_list, course):
    total_rate = []
    for person in some_list:
        if not isinstance(person, Lecturer):
            print(f'{person} не лектор.')
            return
        else:
            if course in person.grades:
                total_rate += person.grades[course]
    res = round(sum(total_rate) / len(total_rate), 2)
    print(f'Средняя оценка лекторов по курсу {course} = {res}.')
    return

# tests

print(cool_reviewer)

print(some_reviewer)

print(cool_lecturer)

print(bad_lecturer)

print(best_student)

print(some_student)

print(best_student > some_student)
print(best_student < some_student)
print()
print(cool_lecturer > bad_lecturer)
print(bad_lecturer > cool_lecturer)
print()
lecturer_course_average(lecturers_list, 'Django')
st_course_average(students_list, 'Soft Skills')
print()