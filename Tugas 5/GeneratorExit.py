print('Putri Robiatul Adawiyah\n210511018\nT121A(R1)\n')
def my_generator():
    try:
        yield 1
        yield 2
        yield 3
    except GeneratorExit:
        print("Generator closed")

g = my_generator()

print(next(g))
print(next(g))

g.close()

print(next(g))