print('Putri Robiatul Adawiyah\n210511018\nT121A(R1)\n')

try:
    with open("file_yang_tidak_terdeteksi.txt") as file:
        data = file.read()
        
except FileNotFoundError:
    print("File yang diminta tidak ditemukan!")
