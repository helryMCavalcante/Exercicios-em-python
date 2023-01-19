peso = float(input('Informe seu peso: '))
altura =float(input('Infome sua altura: '))
imc = peso / pow(altura, 2)
if imc < 18.5:
    print('Seu IMC é de {:.1f}, você está abaixo do peso!'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é de {:.1f}, você está com o peso ideal!'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é de {:.1f}, você está com sobrepeso!'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é de {:.1f}, você está obeso!'.format(imc))
else:
    print('Seu IMC é de {:.1f}, você está com obesidade móbida'.format(imc))
