# Leia dois números e: Mostre a soma; Mostre qual é maior ou se são iguais.

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

if n1 > n2:
    print('O número {} é maior entre os dois escolhidos.'.format(n1))
else:
    print('O número {} é maior entre os dois escolhidos.'.format(n2))

print('A soma de {} + {} é igual a {}'.format(n1, n2, n1+n2))

