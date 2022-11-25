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

    def average_calc(self):
        for k,v in self.grades.items():
            av = sum(v)/ float(len(v))
            return round(av, 1)


    def __str__(self):
        if not isinstance(self, Student):
            print('Not Student')
            return
        return f"\nИмя студента: {self.name}\nФамилия студента: {self.surname}\nСредняя оценка за домашние задания: {self.average_calc()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}"

        
class Mentor:
    def __init__(self, name, surname, courses_attached = [] ):
        self.name = name
        self.surname = surname
        self.courses_attached = courses_attached

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname, courses_attached = [] )
        self.grades = {}

    def __str__(self):
        if not isinstance(self, Lecturer):
            print('Not Lecturer')
            return
        return f"\nИмя лектора: {self.name}\nФамилия лектора: {self.surname}\nСредняя оценка за лекции: делаю функцию"

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
 
best_student = Student('Harry', 'Markovskiy', 'male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Django', 'Soft Skills']

 
cool_reviewer = Reviewer('Christopher', 'Robin')
cool_reviewer.courses_attached += ['Python']

cool_lecturer = Lecturer('Albus', 'Dumbledore')
cool_lecturer.courses_attached += ['Django']

bad_lecturer = Lecturer('Fred', 'Krueger')
bad_lecturer.courses_attached += ['Soft Skills']
 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 5)
cool_reviewer.rate_hw(best_student, 'Python', 7)

best_student.rate_lec(cool_lecturer, 'Django', 10)
best_student.rate_lec(cool_lecturer, 'Django', 7)


best_student.rate_lec(bad_lecturer, 'Soft Skills', 1)
best_student.rate_lec(bad_lecturer, 'Soft Skills', 3)

# print(f"\nСтудент {best_student.name} {best_student.surname}, он учится на курсах {best_student.courses_in_progress}")

# print(f"\nДомашнюю работу {best_student.name} {best_student.surname} проверял {cool_reviewer.name} {cool_reviewer.surname}, оценки вот такие: {best_student.grades}")

# print(f"\nЛучший лектор {cool_lecturer.name} {cool_lecturer.surname} ведет курс(ы) {cool_lecturer.courses_attached} и его оценки {cool_lecturer.grades}")

# print(f"\nТак себе лектор {bad_lecturer.name} {bad_lecturer.surname} ведет курс(ы) {bad_lecturer.courses_attached} и его оценки {bad_lecturer.grades}")

print(cool_reviewer)

print(cool_lecturer)

print(bad_lecturer)

print(best_student)
