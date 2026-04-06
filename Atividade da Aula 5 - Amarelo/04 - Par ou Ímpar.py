# Leia um número e informe se ele é par ou ímpar.

num = float(input('Digite um número: '))

if num % 2 == 0:         # Se o resto da divisão por 2 for 0 sempre será par. 
    print('O número {} é par'.format(num))
else:
    print('O número {} é ímpar'.format(num))
