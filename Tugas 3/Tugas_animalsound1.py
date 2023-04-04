print("\nNama  : Putri Robi'atul Adawiyah")
print("Nim    : 210511018")
print("Kelas  : TI21A(R1)\n\n")

from playsound import playsound 

class hewan:
    def __init__(self,hewan):
        self.hewan = hewan
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')

class anjing(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("C:\\Users\\HP\\Documents\\KULIAH\\SEMESTER4\\PBO2\\Coding\\Tugas3\\Sound\\anjing.mp3")

class ayam(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("C:\\Users\\HP\\Documents\\KULIAH\\SEMESTER4\\PBO2\\Coding\\Tugas3\\Sound\\ayam.mp3")

class bebek(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("C:\\Users\\HP\\Documents\\KULIAH\\SEMESTER4\\PBO2\\Coding\\Tugas3\\Sound\\bebek.mp3")

class burunghantu(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("C:\\Users\\HP\\Documents\\KULIAH\\SEMESTER4\\PBO2\\Coding\\Tugas3\\Sound\\burunghantu.mp3")

class gorilla(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("C:\\Users\\HP\\Documents\\KULIAH\\SEMESTER4\\PBO2\\Coding\\Tugas3\\Sound\\gorilla.mp3")

class kambing(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("C:\\Users\\HP\\Documents\\KULIAH\\SEMESTER4\\PBO2\\Coding\\Tugas3\\Sound\\kambing.mp3")

class kucing(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("C:\\Users\\HP\\Documents\\KULIAH\\SEMESTER4\\PBO2\\Coding\\Tugas3\\Sound\\kucing.mp3")

class sapi(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("C:\\Users\\HP\\Documents\\KULIAH\\SEMESTER4\\PBO2\\Coding\\Tugas3\\Sound\\sapi.mp3")

class singa(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("C:\\Users\\HP\\Documents\\KULIAH\\SEMESTER4\\PBO2\\Coding\\Tugas3\\Sound\\singa.mp3")

class ular(hewan):
    def __init__(self,hewan):
        super().__init__(hewan)
    def bersuara(self):
        print(f'{self.hewan} bersuara ...')
        playsound("C:\\Users\\HP\\Documents\\KULIAH\\SEMESTER4\\PBO2\\Coding\\Tugas3\\Sound\\ular.mp3")

def hewan_bersuara(hewan):
    hewan.bersuara()

hewan0 = hewan('Hewan')
hewan1 = anjing('Anjing')
hewan2 = ayam('Ayam')
hewan3 = bebek('Bebek')
hewan4 = burunghantu('Burung Hantu')
hewan5 = gorilla('Gorilla')
hewan6 = kambing('Kambing')
hewan7 = kucing('Kucing')
hewan8 = sapi('Sapi')
hewan9 = singa('Singa')
hewan10 = ular('Ular')

hewan_bersuara(hewan0)
hewan_bersuara(hewan1)
hewan_bersuara(hewan2)
hewan_bersuara(hewan3)
hewan_bersuara(hewan4)
hewan_bersuara(hewan5)
hewan_bersuara(hewan6)
hewan_bersuara(hewan7)
hewan_bersuara(hewan8)
hewan_bersuara(hewan9)
hewan_bersuara(hewan10)
