# Leia um valor e: Converta para inteiro; Se for múltiplo de 3 → “Múltiplo de 3”; Senão → “Não é múltiplo”.

num = int(input('Digite um número: '))

if num % 3 == 0:
    print('O número {} é múltiplo de 3.'.format(num))
else:
    print('Não é múltiplo.')