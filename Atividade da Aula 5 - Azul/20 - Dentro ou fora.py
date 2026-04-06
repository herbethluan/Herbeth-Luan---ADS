# Leia um valor e: verifique se eles está entre 0 e 100, caso o número esteja fora do intervalo, mostre na tela o valor

num = int(input('Digite um número: '))

if num >= 0 and num <= 100:
    print('Dentro')
else:
    print('O número {} está Fora.'.format(num))
