# Leia um número e: Se for positivo, mostre a raiz aproximada (use **0.5); Caso contrário, informe “Número inválido”

num = int(input('Digite um número: '))

if num >= 0:
    print('A raiz de {} é {:.2f}'.format(num, num**0.5))
else:
    print('O número é inválido! Tente novamente.')