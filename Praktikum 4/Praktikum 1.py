print('Putri Robiatul Adawiyah\n210511018\nT121A(R1)\n')

class Jurnal:
    def __init__(self,title,date):
        self.title = title
        self.date = date

class Peneliti:
    def __init__(self,nama,jurnal):
        self.nama = nama
        self.jurnal = jurnal

    def daftar_jurnal(self):
        print(f'\nPeneliti\t: {self.nama}\n')
        for jurnal in self.jurnal:
            print(f'Judul\t\t: ',jurnal.title)
            print(f'Published\t: {jurnal.date}')

jurnal1 = Jurnal('The Paradox Of Digital Economy Development', 2020)
jurnal2 = Jurnal('Towards Data Sovereignty In Cyberspace', 2015)
peneliti1 = Peneliti('AS Sastrosobroto', [jurnal1, jurnal2])
jurnal3 = Jurnal('A Century Of Trends In Adult Human Height', 2016)
jurnal4 = Jurnal('Repositioning Of The Global Epicentre Of Non-Optimal Cholesterol', 2020)
peneliti2 = Peneliti('IS Widyahening', [jurnal3, jurnal4])
peneliti1.daftar_jurnal()
print('='*40)
peneliti2.daftar_jurnal()
