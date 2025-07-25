from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.__email = email
        
     
    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email  
    
    @abstractmethod
    def display_infor(self):
        pass
    
class Student(Person):
    def __init__(self, name, age, email, student_id, grades =0):
        super().__init__(name, age, email)
        self.student_id = student_id
        self.grades= grades if grades is not None else{}
    
    def calculate_gda(self):
       if not self.grades:
           return 0
       return sum(self.grades.values()) / len(self.grades)
    
    def display_infor(self):
        print(f'''---Information Student---
Student ID: {self.student_id}
Name: {self.name},
Age: {self.age},
Email: {self.get_email()},
GDA: {self.calculate_gda()}
''')
        
class Teacher(Person):
    def __init__(self, name, age, email, employee_id, student_list= 0):
        super().__init__(name, age, email)
        self.employee_id = employee_id
        self.student_list= student_list if student_list is not None else{}
        
    def calculate_students_gpa(self):
        if not self.student_list:
            return 0
        total_gpa = sum(student.calculate_gda() for student in self.student_list)
        return total_gpa / len(self.student_list) if self.student_list else 0
       
    def display_infor(self):
        print(f'''---Information Student---
Student ID: {self.employee_id}
Name: {self.name},
Age: {self.age},
Email: {self.get_email()},
GDA: {self.calculate_students_gpa():}
''')
student1= Student("Nguyen Van An", 12, "abc@gmail.com", 1, {"Toan" : 10, "Van": 9, "Anh": 8})
student2= Student("Nguyen Van Be", 12, "abcd@gmail.com", 2,{"Toan" : 10, "Van": 7, "Anh": 8})
student3= Student("Nguyen Van Ce", 12, "abcde@gmail.com", 3, {"Toan" : 9, "Van": 9, "Anh": 8})
student4= Student("Nguyen Van De", 12, "abcdef@gmail.com", 4,{"Toan" : 7, "Van": 9, "Anh": 8})

student1.display_infor()
student2.display_infor()
student3.display_infor()
student4.display_infor()


teacher1 = Teacher("Thay 1", 35, "thay1@gmail.com", 5, [student1, student2])
teacher2 = Teacher("Co 2", 40, "co2@gmail.com", 6, [student3, student4])

teacher1.display_infor()
teacher2.display_infor()