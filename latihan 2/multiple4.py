print("\nNama  : Putri Robi'atul Adawiyah")
print("Nim    : 210511018")
print("Kelas  : TI21A(R1)\n\n")
class Hewan:
    def __init__(self, jenis):
        self.jenis = jenis
    def display_info(self):
        print(f"Jenis hewan: {self.jenis}")

class Mamalia(Hewan):
    def __init__(self, jenis, nama):
        super().__init__(jenis)
        self.nama = nama
    def display_info(self):
        super().display_info()
        print(f"Nama mamalia: {self.nama}")

class Karnivora(Hewan):
    def __init__(self, jenis, makanan):
        super().__init__(jenis)
        self.makanan = makanan
    def display_info(self):
        super().display_info()
        print(f"Jenis makanan: {self.makanan}")

class Harimau(Mamalia, Karnivora):
    def __init__(self, jenis, nama, makanan):
        Mamalia.__init__(self, jenis, nama)
        Karnivora.__init__(self,jenis, nama, makanan)
    def display_info(self):
        super().display_info()
        print(f"Jenis hewan: {self.jenis}")
        
# contoh penggunaan
HarimauA = Harimau("Mamalia", "Harimau Sumatera", "Daging")
HarimauA.display_info()