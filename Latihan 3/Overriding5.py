print("\nNama  : Putri Robi'atul Adawiyah")
print("Nim    : 210511018")
print("Kelas  : TI21A(R1)\n\n")

class Kucing:
    def bersuara(self):
        print("Meow")
    def cetak_suara(objek):
        objek.bersuara()

class Anjing:
    def bersuara(self):
        print("Guk guk")
    def cetak_suara(objek):
        objek.bersuara()

kucing = Kucing()
anjing = Anjing()

kucing.cetak_suara() # Output: Meow
anjing.cetak_suara() # Output: Guk guk