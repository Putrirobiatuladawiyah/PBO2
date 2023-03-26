print("\nNama  : Putri Robi'atul Adawiyah")
print("Nim    : 210511018")
print("Kelas  : TI21A(R1)\n\n")
class Orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def display_info(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur}")

class Pekerja:
    def __init__(self, pekerjaan, gaji):
        self.pekerjaan = pekerjaan
        self.gaji = gaji
    def display_info(self):
        print(f"Pekerjaan: {self.pekerjaan}")
        print(f"Gaji: {self.gaji}")

class Produser:
    def __init__(self, film, genre):
        self.film = film
        self.genre = genre
    def display_info(self):
        print(f"Film: {self.film}")
        print(f"Genre: {self.genre}")

class ProduserPekerja(Orang, Pekerja, Produser):
    def __init__(self, nama, umur, pekerjaan, gaji, film, genre):
        Orang.__init__(self, nama, umur)
        Pekerja.__init__(self, pekerjaan, gaji)
        Produser.__init__(self, film, genre)
        
    def display_info(self):
        super().display_info()
        print(f"Pekerjaan: {self.pekerjaan}")
        print(f"Gaji: {self.gaji}")
        print(f"Film: {self.film}")
        print(f"Genre: {self.genre}")
# contoh penggunaan
produser_pekerjaC = ProduserPekerja("Steven Spielberg", 76, "Produser Film", "$330.000", "Jaws", "Thriller")
produser_pekerjaC.display_info()