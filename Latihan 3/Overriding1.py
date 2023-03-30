print("\nNama  : Putri Robi'atul Adawiyah")
print("Nim    : 210511018")
print("Kelas  : TI21A(R1)\n\n")

class Matematika:
    def add(self, a, b):
        return a + b
    def add(self, a, b, c=0):
        return a + b + c
    
mat = Matematika()
B = mat.add(5, 3, 4)
print(B)

mut = Matematika()
C = mut.add(7,3)
print(C)