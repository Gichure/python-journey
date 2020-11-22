#Open the file
employees_file = open("employees.txt", "r")
#Read values
if(employees_file.readable()):
    for employee in employees_file.readlines():
        print(employee)
employees_file.close()

#Appending to file
employees_file = open("employees.txt", "a")
employees_file.write("\nLeah - Human Resources")
employees_file.close()

#Writing file
employees_file = open("employees-new.txt", "w")
employees_file.write("Leah - Human Resources")
employees_file.close()