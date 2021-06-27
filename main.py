class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lector(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_grades(self, course='all'):
        if course == 'all':
            summary_grades = 0
            grades_count = 0
            for course_name in self.grades:
                for grades in self.grades[course_name]:
                    summary_grades += grades
                    grades_count += 1
            res = summary_grades / grades_count
        else:
            summary_grades = 0
            for grades in self.grades[course]:
                summary_grades += grades
            res = summary_grades / len(self.grades[course])
        return res

    def __str__(self):
        average_grades = self.get_grades()
        res = f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {average_grades}
Курсы в процессе изучения: {self.courses_in_progress}
Завершенные курсы: {self.finished_courses}'''
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        self_grades = self.get_grades()
        other_grades = other.get_grades()
        return self_grades < other_grades


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        res = f'''Имя: {self.name}
Фамилия: {self.surname}'''
        return res


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def get_grades(self, course='all'):
        if course == 'all':
            summary_grades = 0
            grades_count = 0
            for course_name in self.grades:
                for grades in self.grades[course_name]:
                    summary_grades += grades
                    grades_count += 1
            res = summary_grades / grades_count
        else:
            summary_grades = 0
            for grades in self.grades[course]:
                summary_grades += grades
            res = summary_grades / len(self.grades[course])
        return res

    def __str__(self):
        average_grades = self.get_grades()
        res = f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {average_grades}'''
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        self_grades = self.get_grades()
        other_grades = other.get_grades()
        return self_grades < other_grades

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def average_grades_by_course(student_list, course_name):
    grades_sum = 0
    for student in student_list:
        grades_sum += student.get_grades(course_name)
    av_grade = grades_sum / len(student_list)
    return av_grade

def average_lecturers_grade(lecturers_list, course_name):
    grades_sum = 0
    for lecturer in lecturers_list:
        grades_sum += lecturer.get_grades(course_name)
    av_grade = grades_sum / len(lecturers_list)
    return av_grade

best_student = Student('Ruoy', 'Eman', 'parquet')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

other_student = Student('John', 'Doe', 'parquet')
other_student.courses_in_progress += ['Python', 'Git']
other_student.finished_courses += ['Введение в программирование']

cool_lector = Lecturer('Another', 'Buddy')
cool_lector.courses_attached += ['Python']
another_lector = Lecturer('Other', 'Buddy')
another_lector.courses_attached += ['Git']
third_buddy = Lecturer('Third', 'Buddy')
third_buddy.courses_attached += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(other_student, 'Python', 8)
cool_reviewer.rate_hw(other_student, 'Python', 10)
cool_reviewer.rate_hw(other_student, 'Python', 6)

another_reviewer = Reviewer('No', 'Buddy')
another_reviewer.courses_attached += ['Git']
another_reviewer.rate_hw(best_student, 'Git', 8)
another_reviewer.rate_hw(best_student, 'Git', 8)
another_reviewer.rate_hw(best_student, 'Git', 10)
another_reviewer.rate_hw(other_student, 'Git', 8)
another_reviewer.rate_hw(other_student, 'Git', 7)
another_reviewer.rate_hw(other_student, 'Git', 10)

best_student.rate_lector(cool_lector, 'Python', 10)
best_student.rate_lector(cool_lector, 'Python', 9)
best_student.rate_lector(third_buddy, 'Python', 6)
best_student.rate_lector(another_lector, 'Git', 8)
best_student.rate_lector(another_lector, 'Git', 7)
other_student.rate_lector(cool_lector, 'Python', 8)
other_student.rate_lector(cool_lector, 'Python', 9)
other_student.rate_lector(third_buddy, 'Python', 7)
other_student.rate_lector(another_lector, 'Git', 10)
other_student.rate_lector(another_lector, 'Git', 6)

print(best_student)
print()
print(other_student)
print()
print(cool_lector)
print()
print(another_lector)
print()
print(cool_reviewer)
print()
print(another_reviewer)
print()
print("Сравнение студентов:", best_student > other_student)
print()
print("Сравнение лекторов:", cool_lector > another_lector)
print()
print(average_grades_by_course([best_student, other_student], "Python"))
print()
print(average_lecturers_grade([cool_lector, third_buddy], "Python"))
