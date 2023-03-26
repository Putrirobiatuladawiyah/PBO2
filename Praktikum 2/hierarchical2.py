print("\nNama  : Putri Robi'atul Adawiyah")
print("Nim    : 210511018")
print("Kelas  : TI21A(R1)\n\n")
class Work:
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
    
class Manager(Work):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department
    def get_department(self):
        return self.department
    
class Aktor(Work):
    def __init__(self, name, age, salary, film):
        super().__init__(name, age, salary)
        self.film = film
    def get_film(self):
        return self.film
    
# Hierarchical Inheritance
class SeniorAktor(Aktor):
    def __init__(self, name, age, salary, film, genre):
        super().__init__(name, age, salary, film)
        self.genre = genre
    def get_genre(self):
        return self.genre
    def data(self):
        print(f"aktor tampan {self.name} Berumur {self.age} th berpenghasilan Rp {self.salary} memainkan drama berjudul {self.film} yg bergenre {self.genre}")
        print("="*54)

AktorA = SeniorAktor("Gong Yoo", 43, "17,2M", "Goblin", "Fantasi & Romance")
AktorA.data()
