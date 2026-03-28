soma = 0
contador = 0
for c in range (1,6):
    num = (float(input('Digite o {}º número: '.format(c))))
    soma = soma + num
    contador = contador + 1
print('Foram digitados {:.1f} números e a média entre eles é {:.1f}'.format(contador, soma / contador))



