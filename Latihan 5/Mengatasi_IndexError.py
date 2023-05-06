print('Putri Robiatul Adawiyah\n210511018\nT121A(R1)\n')

list_angka = [1, 2, 3]

try:
    value = list_angka[4]
    
except IndexError:
    print("Index yang diminta melebihi jumlah elemen dalam list!")
