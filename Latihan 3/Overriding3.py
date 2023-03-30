print("\nNama  : Putri Robi'atul Adawiyah")
print("Nim    : 210511018")
print("Kelas  : TI21A(R1)\n\n")

class Animal:
    def make_sound(self):
        print("The animal makes a sound")

class Dog(Animal):
    def make_sound(self):
        print("The dog barks")

class Cat(Animal):
    def make_sound(self):
        print("The cat meows")

class Chihuahua(Dog):
    def make_sound(self):
        print("The chihuahua yaps")

class Siamese(Cat):
    def make_sound(self):
        print("The Siamese purrs")
    def animal_sound(animal):
        animal.make_sound()

# Instantiate objects of each class
animal = Animal()
dog = Dog()
cat = Cat()
chihuahua = Chihuahua()
siamese = Siamese()

# Call the animal_sound function for each object
animal.make_sound()        # Output: The animal makes a sound
dog.make_sound()           # Output: The dog barks
cat.make_sound()           # Output: The cat meows
chihuahua.make_sound()     # Output: The chihuahua yaps
siamese.make_sound()       # Output: The Siamese purrs
