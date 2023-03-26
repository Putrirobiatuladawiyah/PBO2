print("\nNama  : Putri Robi'atul Adawiyah")
print("Nim    : 210511018")
print("Kelas  : TI21A(R1)\n\n")
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_salary(self):
        return self.salary
    def data(self):
        print(f"{self.name} data")
    
class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department
    def get_department(self):
        return self.department
    
class Programmer(Employee):
    def __init__(self, name, age, salary, language):
        super().__init__(name, age, salary)
        self.language = language
    def get_language(self):
        return self.language
    
# Hierarchical Inheritance
class SeniorProgrammer(Programmer):
    def __init__(self, name, age, salary, language, level):
        super().__init__(name, age, salary, language)
        self.level = level
    def get_level(self):
        return self.level
    def data(self):
        print(f"{self.name} Berumur {self.age} th berpenghasilan Rp {self.salary} /Bulan, sebagai programmer dg menggunakan bahasa {self.language} Level {self.level}")
        print("="*54)

Programmer = SeniorProgrammer("Putri Robi'atul Adawiyah", 19, "14jt", "Python", 2)
Programmer.data()
