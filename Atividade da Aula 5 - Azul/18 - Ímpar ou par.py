# Leia um número e: Mostre se ele é par positivo, par negativo, impar positivo, impar negativo ou neutro.

num = int(input('Digite um número: '))

if num % 2 == 0 and num > 0:
    print('Par Positivo')
elif num % 2 == 0 and num < 0:
    print('Par Negativo')
elif num % 2 != 0 and num > 0:
    print('Ímpar Positivo')
elif num % 2 != 0 and num < 0:
    print('ímpar Negativo')
else:
    print('Neutro')