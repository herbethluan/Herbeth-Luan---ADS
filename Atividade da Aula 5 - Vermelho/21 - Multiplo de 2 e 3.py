# Leia um número inteiro informado pelo usuário.
# Verifique se o número é positivo.
# Caso seja, analise se ele é múltiplo de 2 e de 3 ao mesmo tempo.
# Se atender a ambas as condições, exiba: “Múltiplo de 2 e 3”.
# Caso contrário, exiba: “Não atende”.
# Se o número não for positivo, exiba: “Número inválido”.


num = int(input('Digite um número: '))

if num > 0: 
    print('O número é Positivo.')

    if num % 2 == 0 and num % 3 == 0:
        print('O número {} é múltiplo de 2 e 3 ao mesmo tempo.'.format(num))
    else:
          print('O número {} não é múltiplo de 2 e 3 ao mesmo tempo.'.format(num))
else:
      print('Número inválido.')
