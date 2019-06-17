nome = input('Qual o seu nome? ')
print('Centralizado')
print('Muito prazer {:=^15}!!'.format(nome))
print('A direita')
print('Muito prazer {:=>15}!!'.format(nome))
print('A Esquerda')
print('Muito prazer {:=<15}!!'.format(nome))
print('\n')
N1 = int(input('Digite um número '))
N2 = int(input('Digite um outro número '))
Som = N1+N2
Sub = N1-N2
Mul = N1*N2
Div = N1/N2
Pot = N1**N2
DivI = N1//N2
Res = N1%N2
print(' A soma dos dois números é {},\n A Subtração é {},\n A Multiplicação é {},\n A Divisão é {:.2f},\n A potencia do primeiro pelo segundo é {}'.format(Som, Sub, Mul, Div,Pot))
print(' A Divisão inteira é {},\n O resto dessa divisão é {}'.format(DivI, Res))




