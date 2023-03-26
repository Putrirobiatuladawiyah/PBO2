print("\nNama  : Putri Robi'atul Adawiyah")
print("Nim    : 210511018")
print("Kelas  : TI21A(R1)\n\n")
class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def get_name(self):
        return self.name
    def get_color(self):
        return self.color
    def data(self):
        print(f"{self.name} data")

class Mammal(Animal):
    def __init__(self, name, color, fur):
        super().__init__(name, color)
        self.fur = fur
    def get_fur(self):
        return self.fur
    
class Bird(Animal):
    def __init__(self, name, color, wingspan):
        super().__init__(name, color)
        self.wingspan = wingspan
    def get_wingspan(self):
        return self.wingspan
    
# Hierarchical Inheritance
class Reptile(Mammal):
    def __init__(self, name, color, fur, Weight):
        super().__init__(name, color, fur)
        self.Weight = Weight
    def get_Weight(self):
        return self.Weight
    def data(self):
        print(f"seekor {self.name} Berwarna {self.color} dengan tipe bulu {self.fur} dengan berat {self.Weight} ada di atap rumah")
        print("="*54)
    
Mammal = Reptile("Gagak", "Hitam", "Plumae", "5.9 kg")
Mammal.data()