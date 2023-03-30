print("\nNama  : Putri Robi'atul Adawiyah")
print("Nim    : 210511018")
print("Kelas  : TI21A(R1)\n\n")
class Kendaraan:
    def __init__(self, jenis, merk, warna):
        self.jenis = jenis
        self.merk = merk
        self.warna = warna
    def berkendara(self):
        print("Kendaraan ini sedang berjalan.")

class SepedaMotor(Kendaraan):
    def __init__(self, jenis, merk, warna, cc):
        super().__init__(jenis, merk, warna)
        self.cc = cc
    def belok(self):
        print("Sepeda Motor ini sedang belok.")

motorA = SepedaMotor("Sepeda Motor", "Honda", "Merah", 150)
motorA.berkendara() # Output: Kendaraan ini sedang berjalan.
motorA.belok() # Output: sepeda motor ini sedang belok.