print("\nNama  : Putri Robi'atul Adawiyah")
print("Nim    : 210511018")
print("Kelas  : TI21A(R1)\n\n")
from abc import ABC, abstractmethod

class Sport(ABC):
    @abstractmethod
    def start(self):
        pass

class Run(Sport):
    def start(self):
        print("Starting Run..one, two, three...")
        print("="*54)

class HighJump(Sport):
    def start(self):
        print("Starting HighJump..one, two, three...")
        print("="*54)

class Yoga(Sport):
    def start(self):
        print("Starting Yoga..one, two, three...")
        print("="*54)

sport = [Run(), HighJump(), Yoga()]

for sport in sport:
    sport.start()