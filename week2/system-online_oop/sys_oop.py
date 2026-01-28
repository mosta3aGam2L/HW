#ء(Parent Class)
class User:
    def __init__(self, name, email, password):
        self.name = name       # Public attribute
        self.email = email     # Public attribute
        self._password = password  # Private attribute (Encapsulation) 
    def show_info(self):
        return f"User: {self.name}, Email: {self.email}"

    # (Encapsulation)
    def set_password(self, new_password):
        self._password = new_password

    def check_password(self, password):
        return self._password == password

# 2.  (Student Subclass)
class Student(User):
    def __init__(self, name, email, password, level):
        super().__init__(name, email, password)
        self.level = level

    # Override  show_info (Polymorphism)
    def show_info(self):
        return f"Student: {self.name} | Level: {self.level}"

# 3.     (Instructor Subclass)
class Instructor(User):
    def __init__(self, name, email, password, specialty):
        super().__init__(name, email, password)
        self.specialty = specialty

    # Override  show_info (Polymorphism)
    def show_info(self):
        return f"Instructor: {self.name} | Specialty: {self.specialty}"

# --- (Main Execution) ---

s = Student("Ali", "ali@email.com", "1234", "Beginner") 

i = Instructor("Mona", "mona@email.com", "abcd", "Machine Learning")

print(s.show_info())  # : Student: Ali | Level: Beginner 
print(i.show_info())  # : Instructor: Mona | Specialty: Machine Learning]

#ckeck password
print(s.check_password("1234"))  #true