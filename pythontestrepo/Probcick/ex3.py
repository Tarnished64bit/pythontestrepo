from student import Student
from course_group import CourseGroup

student = Student("Иван", "Иванов", 18, "1")
classmate1 = Student("Александр", "Александров", 19, "1")
classmate2 = Student("Василий", "Васильев", 20, "1")
classmate3 = Student("Сергей", "Сергеев", 25, "1")

course_group = CourseGroup(student, [classmate1, classmate2, classmate3])

print(course_group)