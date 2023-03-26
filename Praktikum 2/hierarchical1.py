print("\nNama  : Putri Robi'atul Adawiyah")
print("Nim    : 210511018")
print("Kelas  : TI21A(R1)\n\n")
class AlasKaki:
    def __init__(self, nama):
        self.nama = nama
    def get_nama(self):
        return self.nama
    def data(self):
        print(f"{self.nama} data")
    
class Sepatu(AlasKaki):
    def __init__(self, nama, merek):
        super().__init__(nama)
        self.merek = merek
    def get_merek(self):
        return self.merek
    
class Sandal(AlasKaki):
    def __init__(self, nama, merek):
        super().__init__(nama)
        self.merek = merek
    def get_merek(self):
        return self.merek
    
# turunan Hierarchical Inheritance
class Kets(Sepatu):
    def __init__(self, nama, merek, ukuran):
        super().__init__(nama, merek)
        self.ukuran = ukuran
    def get_ukuran(self):
        return self.ukuran
    def data(self):
        print(f"sebuah sepatu {self.nama} dengan merek {self.merek} dg ukuran {self.ukuran} terlihat sangat cantik")
        print("="*54)
    
# turunan Hierarchical Inheritance
class Jepit(Sandal):
    def __init__(self, nama, merek, harga):
        super().__init__(nama, merek)
        self.harga = harga
    def get_harga(self):
        return self.harga
    def data(self):
        print(f"sandal {self.nama} dengan merek {self.merek} dg harga {self.harga} sangat nyaman digunakan")
    
SepatuA = Kets("Nike", "Air Jordan", "37")
SepatuA.data()
SandalA = Jepit("Eiger", "Ugimba", "Rp. 142.000")
SandalA.data()