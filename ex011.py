larg = float(input('Largura da parede: '))
altu = float(input('Altura da parede: '))
area = larg * altu
tinta = area / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m². \nPara pintar essa parede, você precisará de {}l de '
      'tinta'.format(larg, altu, area, tinta))
