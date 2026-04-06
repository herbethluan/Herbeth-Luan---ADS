# Leia um número e: Se estiver entre 10 e 20 → “Dentro”; Caso contrário → “Fora”.

num = int(input('Digite um número inteiro: '))

if num < 20 and num > 10:
    print('Dentro')
else:
    print('Fora')