# Leia um número e informe: “Dentro do intervalo” se estiver entre 0 e 10; “Fora do intervalo” caso contrário.

num = float(input('Digite um número: '))

if num < 11 and num >= 0:
    print('O número {} está dentro do intervalo.'.format(num))
else:
    print('O número {} está fora do intervalo.'.format(num))