# Leia três números inteiros informados pelo usuário. Exiba em ordem decrescente o 
# resto da divisão por 3.

n1 = int(input('Digite o 1º número inteiro: '))
n2 = int(input('Digite o 2º número inteiro: '))
n3 = int(input('Digite o 3º número inteiro: '))

n1_resto = n1 % 3
n2_resto = n2 % 3
n3_resto = n3 % 3

if n1_resto > n2_resto and n3_resto:
    if n2_resto > n3_resto:
        print('Ordem decrescente dos restos: {}, {}, {}.'.format(n1_resto, n2_resto, n3_resto))

