jogador = {}
partidas = []
jogador['Nome'] = str(input('Nome do Jogador: '))
tot = int(input('Quantas partidas jogadas: '))
for c in range(0,tot):
    partidas.append(int(input(f'Quantos gols feitos na {c+1}º partida: ')))
jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f' O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas')
for i,v in enumerate(jogador['Gols']):
    print(f'    => Na {i+1}º partida fez {v} gol(s)     ')
print(f'Foi um total de {jogador["Total"]} gols')

