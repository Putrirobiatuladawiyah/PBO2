print('Putri Robiatul Adawiyah\n210511018\nT121A(R1)\n')

class judul_lagu:
    def __init__(self,judul=None):
        if judul is None:
            self.judul = []
        else:
            self.judul = judul

    def add_judul(self,judul):
        self.judul.append(judul)

    def daftar_judul(self):
        for judul in self.judul:
            print(f'Judul\t\t: ',judul.judul)
            print(f'Genre\t\t: ',judul.genre)
            print(f'Tanggal Rilis\t: ',judul.tgl_rilis)

class Judul:
    def __init__(self,judul,genre,tgl_rilis):
        self.judul = judul
        self.genre = genre
        self.tgl_rilis = tgl_rilis

    def get_tgl_rilis(self):
        return self.tgl_rilis

    def get_genre(self):
        return self.genre
    
    def get_tgl_rilis(self):
        return self.tgl_rilis

class Lagu:
    def __init__(self,name_lagu,judul_lagu):
        self.name_lagu = name_lagu
        self.judul_lagu = judul_lagu

    def tampil(self):
        print(f'\nPencipta\t: {self.name_lagu}\n')

judul1 = Judul('Case 143', 'Korean Dance', "7 Oktober 2022")
judul2 = Judul('Maniac', 'Korean Dance/Music Trap', "18 Maret 2022")
judul3 = Judul('Charmer', 'Korean Dance', "18 Maret 2022")
judul3 = Judul('Thunderous', 'Music Trap/Music Hip Hop', "23 Agustus 2021")
judul_lagu = judul_lagu([judul1, judul2, judul3])
lagu = Lagu('Stray Kids', judul_lagu)
lagu.judul_lagu.judul
lagu.tampil()
print("="*40)
lagu.judul_lagu.daftar_judul()