N = int(input('Digite um valor para ver sua tabuada '))
contador = 0
print('---------------- Forma 1 ----------------')
print(N,'X 1 = {:2}'.format(N))
print(N,'X 2 = {:2}'.format(N*2))
print(N,'X 3 = {:2}'.format(N*3))
print(N,'X 4 = {:2}'.format(N*4))
print(N,'X 5 = {:2}'.format(N*5))
print(N,'X 6 = {:2}'.format(N*6))
print(N,'X 7 = {:2}'.format(N*7))
print(N,'X 8 = {:2}'.format(N*8))
print(N,'X 9 = {:2}'.format(N*9))
print(N,'X 10 = {:2}'.format(N*10))
print('---------------- Forma 2 (While) ----------------')
while contador < 11:
    print(N,'X',contador,'= {:2}'.format(N*contador))
    contador = contador +1

