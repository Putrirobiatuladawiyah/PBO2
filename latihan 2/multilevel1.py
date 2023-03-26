print("\nNama  : Putri Robi'atul Adawiyah")
print("Nim    : 210511018")
print("Kelas  : TI21A(R1)\n\n")
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} The animal speaks")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def speak(self):
        print(f"{self.breed} The dog barks")
        
class Bulldog(Dog):
    def __init__(self, name, breed, origin):
        super().__init__(name, breed)
        self.origin = origin
    def speak(self):
        print(f"{self.origin} The bulldog growls")

Bulldog = Bulldog("Mikki", "French Bulldog", "Prancis")
Bulldog.speak() 
 

