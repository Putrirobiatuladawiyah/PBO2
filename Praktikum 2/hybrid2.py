print("\nNama  : Putri Robi'atul Adawiyah")
print("Nim    : 210511018")
print("Kelas  : TI21A(R1)\n\n")
class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def data(self):
        print(f"{self.x} {self.y}")

# Single Inheritance
class Drawable:
    def draw(self):
        print("Drawing object at: ", self.x, self.y)

# Single Inheritance
class Moveable:
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
# Multiple Inheritance
class Player(GameObject, Drawable, Moveable):
    def __init__(self, x, y):
        super().__init__(x, y)
    def update(self):
        self.move(1, 1)
        self.draw()
    def data(self):
        print(f"{self.x} {self.y}")

GameObjectA = Player("satu", "dua" )
GameObjectA.data()