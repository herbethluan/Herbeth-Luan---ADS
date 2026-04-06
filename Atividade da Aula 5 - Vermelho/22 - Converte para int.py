# Leia um valor informado pelo usuário.
# Tente convertê-lo para número inteiro.
# Caso não seja possível realizar a conversão, exiba: “Entrada inválida”.
# Caso a conversão seja bem-sucedida:
# Se o número for maior que 10, exiba: “Alto”.
# Caso contrário, exiba: “Baixo”.

num = input('Digite um número: ')

if num.isdigit():
    valor = int(num)
    if valor > 10:
        print('Alto!')
    else:
        print('Baixo!')
else:
    print('Entrada Inválida')