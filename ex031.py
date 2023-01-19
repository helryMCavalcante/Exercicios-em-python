distancia = float(input('Informe a distancia da sua viagem: '))
if distancia <= 200:
    preco = distancia*0.50
    print('Você está prestes a começar uma viagem de {:.0f}KM'.format(distancia
                                                                      ))
    print('O preço da sua viagem será de R${:.2f}'.format(preco))