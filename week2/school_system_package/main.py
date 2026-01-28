from student.student_model import Student
from teacher.teacher_model import Teacher
from courses.course_model import Course

# 2.(Objects)
t1 = Teacher(1, "Dr. Ahmed", "AI")           
s1 = Student(10, "mostafa")                     
c1 = Course(100, "Machine Learning", t1)     

# 3. enroll
s1.enroll(c1)                                # 

#  output
print(s1.name, "enrolled in:", s1.courses)   # 