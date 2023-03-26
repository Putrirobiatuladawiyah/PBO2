print("\nNama  : Putri Robi'atul Adawiyah")
print("Nim    : 210511018")
print("Kelas  : TI21A(R1)\n\n")
class Seseorang:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    def get_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Address:", self.address)
    
# Single Inheritance
class Mahasiswa(Seseorang):
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)
        self.student_id = student_id
    def get_info(self):
        super().get_info()
        print("Student ID:", self.student_id)

# Single Inheritance
class Employee(Seseorang):
    def __init__(self, name, age, address, employee_id, salary):
        super().__init__(name, age, address)
        self.employee_id = employee_id
        self.salary = salary
    def get_info(self):
        super().get_info()
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)

# Multiple Inheritance
class Penulis(Employee, Mahasiswa):
    def __init__(self, name, age, address, employee_id, salary, student_id, published_books):
        Mahasiswa.__init__(self, name, age, address, student_id)
        Employee.__init__(self, name, age, address, employee_id, salary)
        self.published_books = published_books
    def get_info(self):
        super().get_info()
        print("Student ID:", self.student_id)
        print("Published Books:", self.published_books)
    
SeseorangA = Penulis("putri robi'atul adawiyah", 19, "brebes", 12345, "penulis", 210511018, "cantik itu luka")
SeseorangA.get_info()