print('Putri Robiatul Adawiyah\n210511018\nT121A(R1)\n')

class Kpop:
    def __init__(self,grup,year,fandom):
        self.grup = grup
        self.year = year
        self.fandom = fandom

class Agensi:
    def __init__(self,nama,kpop):
        self.nama = nama
        self.kpop = kpop

    def daftar_kpop(self):
        print(f'\nAgensi\t: {self.nama}\n')
        for kpop in self.kpop:
            print(f'Nama Grup\t: ',kpop.grup)
            print(f'Debut\t\t: {kpop.year}')
            print(f'Nama Fandom\t: {kpop.fandom}')

kpop1 = Kpop('Stray Kids', 2018, "Stay")
kpop2 = Kpop('Twice', 2015, "Once")
agensi1 = Agensi('JYP Entertaiment', [kpop1, kpop2])
kpop3 = Kpop('Black Pink', 2016, "Blink")
kpop4 = Kpop('Treasure', 2020, "Theume")
agensi2 = Agensi('YG Entertaiment', [kpop3, kpop4])
agensi1.daftar_kpop()
print('='*40)
agensi2.daftar_kpop()