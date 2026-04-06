#  Leia um número e: Se for par e positivo → “Par positivo”; Se for par e negativo → “Par negativo”; Caso contrário → “Ímpar”

num = int(input('Digite um número inteiro: '))

if num % 2 == 0 and num >= 0:
    print('Seu número é um Par e Positivo')
elif num % 2 == 0 and num < 0:
    print('Seu número é um Par Negativo')
elif num % 2 != 0 and num > 0:
    print('Seu número é um Ímpar Positivo')
else:
    print('Seu número é um Ímpar Negativo')