print("\nNama  : Putri Robi'atul Adawiyah")
print("Nim    : 210511018")
print("Kelas  : TI21A(R1)\n\n")
class Hewan:
    def __init__(self, nama):
        self.nama = nama
    def speak(self):
        print(f"{self.nama} speaks")

class Kelinci(Hewan):
    def __init__(self, nama, jenis):
        super().__init__(nama)
        self.jenis = jenis
    def fly(self):
        print(f"{self.nama} adalah seekor kelinci lucu dengan jenis {self.jenis}")
        print("="*54)

class HollandLop(Kelinci):
    def __init__(self, nama, jenis, color):
        super().__init__(nama, jenis)
        self.color = color
    def speak(self):
        print(f"{self.nama} adalah kelinci berwarna {self.color} yang sangat menggemaskan")
        print("="*54)

HollandLopA = HollandLop("Bubu", "Holland Lop", "Abu-Abu")
HollandLopA.speak() # Output: Bubu adalah kelinci berwarna Abu-Abu yang sangat menggemaskan
HollandLopA.fly() # Output: Bubu adalah seekor kelinci lucu dengan jenis Holland Lop