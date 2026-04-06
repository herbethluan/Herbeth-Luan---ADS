#  Leia dois números e: Verifique se são iguais ou diferentes. Sendo diferentes mostre a diferença entre eles.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 == n2:
    print('Os números são iguais')
elif n1 > n2:
    print('O número {} é o maior e está a {} número(s) de distância'.format(n1, n1-n2))
else:
    print('O número {} é o maior e está a {} número(s) de distância'.format(n2, n2-n1))
