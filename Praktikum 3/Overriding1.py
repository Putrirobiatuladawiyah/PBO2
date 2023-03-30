print("\nNama  : Putri Robi'atul Adawiyah")
print("Nim    : 210511018")
print("Kelas  : TI21A(R1)\n\n")
class Gitar:
    def bersuara(self):
        print("JRENGGG JENG JENGG")
    def cetak_suara(objek):
        objek.bersuara()

class Piano:
    def bersuara(self):
        print("DO RE MI FA SOL LA SI DOO")
    def cetak_suara(objek):
        objek.bersuara()

gitar = Gitar()
piano = Piano()

gitar.cetak_suara() # Output: JRENGGG JENG JENGG
print("="*54)

piano.cetak_suara() # Output: DO RE MI FA SOL LA SI DOO
print("="*54)