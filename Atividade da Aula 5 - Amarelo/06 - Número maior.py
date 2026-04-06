# Leia dois números e exiba qual é o maior.

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

if n1 > n2:
    print('Entre {} e {} o maior valor é {}.'.format(n1, n2, n1))
else:
    print('Entre {} e {} o maior valor é {}.'.format(n1, n2, n2))
