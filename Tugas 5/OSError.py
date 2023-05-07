print('Putri Robiatul Adawiyah\n210511018\nT121A(R1)\n')
import os

try:
    os.mkdir('/mydirectory')
except OSError as e:
    print("Failed to create directory: ", e)