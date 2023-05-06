print('Putri Robiatul Adawiyah\n210511018\nT121A(R1)\n')

dictionary = {"lima": 5, "enam": 6, "tujuh": 7}

try:
    value = dictionary["delapan"]
    
except KeyError:
    print("Key yang diminta tidak ditemukan pada dictionary!")
