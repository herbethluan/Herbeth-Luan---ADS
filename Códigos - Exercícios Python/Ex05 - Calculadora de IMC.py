altura = float(input('Qual a sua altura? [Metros]: '))
peso = float(input('Qual o seu peso? [Kilos]: '))
imc = peso / altura ** 2

if imc < 16.9:
    print('Seu IMC é {:.2f} e está muito abaixo do peso ideal.'.format(imc))
elif imc < 18.4:
    print('Seu IMC é {:.2f} e está abaixo do peso ideal.'.format(imc))
elif imc < 24.9:
    print('Seu IMC é {:.2f} e está no peso ideal.'.format(imc))
elif imc < 29.9:
    print('Seu IMC é {:.2f} e está acima do peso.'.format(imc))
elif imc < 34.9:
    print('Seu IMC é {:.2f} e está em obesidade grau I.'.format(imc))
elif imc < 40: 
    print('Seu IMC é {:.2f} e está em obesidade grau II.'.format(imc))
elif imc > 40:
    print('Seu IMC é {:.2f} e está em obesidade grau III.'.format(imc))
