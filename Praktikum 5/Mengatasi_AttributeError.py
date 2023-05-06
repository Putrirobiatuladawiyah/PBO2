print('Putri Robiatul Adawiyah\n210511018\nT121A(R1)\n')

class Kucing:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

kucing = Kucing("puppy", "anggora")

try:
    print(kucing.pemilik)
except AttributeError:
    print("Objek tidak memiliki atribut yang diminta!")