print("\nNama  : Putri Robi'atul Adawiyah")
print("Nim    : 210511018")
print("Kelas  : TI21A(R1)\n\n")
class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def berbicara(self):
        print(f"{self.nama} sedang bertugas.")

class Dokter(Manusia):
    def __init__(self, nama, umur, Spesialis):
        super().__init__(nama, umur)
        self.Spesialis = Spesialis
    def mengajar(self):
        print(f"{self.nama} dengan Spesialis {self.Spesialis} sedang memeriksa pasien.")
        
dokterA = Dokter("DR.Putrii", 19, "Gigi")
dokterA.berbicara() # Output: DR.Putrii sedang berbicara.
dokterA.mengajar() # Output: DR.Putrii dengan Spesialis Gigi sedang memeriksa pasien.