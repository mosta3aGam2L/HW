class Student:
    def __init__(self, id, name, courses=None):
        self.id = id
        self.name = name
        self.courses = courses if courses is not None else []

    def enroll(self, course):
       #enroll a student in a course
        self.courses.append(course.title)