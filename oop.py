class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)   

    def rate_lect(self, lecturer, course, grade):
            if isinstance(lecturer, Lecturer):
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
            res=f'Имя: {self.name} \n Фамилия: {self.surname}'
            return res
            
class Lecturer (Mentor):
    grades = {}
    
    def mean(grades):
        return float(sum(grades)) / max(len(grades), 1)

    def __str__(self):
        res=f'Имя: {self.name} \n Фамилия: {self.surname} \n Средняя оценка за лекции: {self.mean}'
        return res
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 9)
cool_mentor.rate_hw(best_student, 'Python', 8)

some_lecter = Lecturer('Hannibal', 'Body')
best_student.rate_lect(some_lecter, 'Whython',7)

print(cool_mentor)
print(some_lecter)
