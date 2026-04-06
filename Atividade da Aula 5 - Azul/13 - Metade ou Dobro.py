# Leia um número e: Se for maior que 100 → mostre metade; Senão → mostre o dobro.

num = int(input('Digite um número inteiro: '))

if num > 100:
    print('A metade de {} é {}.'.format(num, num/2))
else:
    print('O dobro de {} é {}.'.format(num, num*2))