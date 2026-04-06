#  Leia idade e: Mostre: Menor de idade (<18); Adulto (18 a 59); Idoso (60+).

idade = int(input('Qual a sua idade? '))

if idade < 18:
    print('Menor de idade.')
elif idade >= 18 and idade < 60:
    print('Adulto.')
else:
    print('Idoso.')
