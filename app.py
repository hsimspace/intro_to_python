# From student file, import Student class
from student import Student

# Create a student object
student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.5, True)
student3 = student("Harold", "Jazz Workshop", 3.8, True)

# Output the student
print(student1.name)
print(student2.gpa)
print(student3.gpa)

# Testing for honor roll
print(student1.on_honor_roll())
print(student1.on_honor_roll())















