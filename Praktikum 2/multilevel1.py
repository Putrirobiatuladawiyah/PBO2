print("\nNama  : Putri Robi'atul Adawiyah")
print("Nim    : 210511018")
print("Kelas  : TI21A(R1)\n\n")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Karyawan(Person):
    def __init__(self, name, age, gender, salary):
        super().__init__(name, age)
        self.gender = gender
        self.salary = salary
    def get_details(self):
        super().get_details()
        print(f"Gender: {self.gender}, Salary: {self.salary}")

class Designer(Karyawan):
    def __init__(self, name, age, gender, salary, fashion):
        super().__init__(name, age, gender, salary)
        self.fashion = fashion
    def get_details(self):
        super().get_details()
        print(f"Fashion: {self.fashion}")
        
DesignerA = Designer("Putri", 19, "Female", "14jt", "Dress")
DesignerA.get_details() 