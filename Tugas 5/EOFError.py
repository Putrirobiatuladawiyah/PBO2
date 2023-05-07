print('Putri Robiatul Adawiyah\n210511018\nT121A(R1)\n')
try:
    x = int(input("Enter a number: "))
except EOFError:
    print("End of file reached")
except ValueError:
    print("Invalid input")