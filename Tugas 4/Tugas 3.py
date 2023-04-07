print('Putri Robiatul Adawiyah\n210511018\nT121A(R1)\n')

class Nama_Member:
    def __init__(self,nama=None):
        if nama is None:
            self.nama = []
        else:
            self.nama = nama

    def add_nama(self,nama):
        self.nama.append(nama)

    def daftar_nama(self):
        for nama in self.nama:
            print(f'Nama\t\t: ',nama.nama)
            print(f'Umur\t\t: ',nama.genre)
            print(f'Posisi\t\t: ',nama.tgl_rilis)

class Nama:
    def __init__(self,nama,genre,tgl_rilis):
        self.nama = nama
        self.genre = genre
        self.tgl_rilis = tgl_rilis

    def get_tgl_rilis(self):
        return self.tgl_rilis

    def get_genre(self):
        return self.genre
    
    def get_tgl_rilis(self):
        return self.tgl_rilis

class Member:
    def __init__(self,name_member,nama_member):
        self.name_member = name_member
        self.nama_member = nama_member

    def tampil(self):
        print(f'\nNama Grup\t: {self.name_member}\n')

nama1 = Nama('Hwang Hyunjin', 23, "Main Dancer")
nama2 = Nama('Lee Know', 24, "Main Dancer")
nama3 = Nama('Kim Seung-min', 22, "Lead Vocal")
nama4 = Nama('Yang Jeong-in', 22, "Vocalist")
nama5 = Nama('Cristopher Bang', 25, "Leader,Produser")
nama6 = Nama('Felix Lee', 22, "Lead Dancer")
nama7 = Nama('Han Ji Sung', 22, "Rapper,Pencipta Lagu")
nama8 = Nama('Seo Chang Bin', 23, "Main Rapper,Produser")
nama_member = Nama_Member([nama1, nama2, nama3, nama4, nama5, nama6, nama7, nama8])
member = Member('Stray Kids', nama_member)
member.nama_member.nama
member.tampil()
print("="*40)
member.nama_member.daftar_nama()