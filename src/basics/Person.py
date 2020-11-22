class Person:
    def __init__(self,first_name, surname, age, gender):
        self.first_name = first_name
        self.surname = surname
        self.age = age
        self.gender = gender
        
    def full_name(self):
        return self.first_name + " "+self.surname
    
    def run(self):
        print("Person is running")
    def walk(self):
        print("Person is walking")
    def sleep(self):
        print("Person is sleeping")