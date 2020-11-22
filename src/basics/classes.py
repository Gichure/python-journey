from Student import Student

first_name = input("Enter firstname: ")
surname = input("Enter surname: ")
age = int(input("Enter ager: "))
gender = input("Enter gender: ")


student = Student(first_name,surname,age, gender)

print(student.full_name())

student.walk()
student.study()