print('Putri Robiatul Adawiyah\n210511018\nT121A(R1)\n')
def get_data():
    with open('data.txt', 'r') as f:
        data = f.read()
    return data

print(get_data())