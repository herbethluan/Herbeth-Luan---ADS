# Leia um valor e verifique: Se é maior que 10 → “Maior que 10”; Caso contrário → “Menor ou igual a 10”

num = float(input('Digite um número: '))

if num > 10:
    print('O número {} é maior que 10.'.format(num))
else:
    print('O número {} é menor que 10.'.format(num))