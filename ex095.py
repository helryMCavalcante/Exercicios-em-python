jogador = {}
partidas = []
time = []
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do Jogador: '))
    tot = int(input('Quantas partidas jogadas: '))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f'Quantos gols feitos na {c+1}º partida: ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar: [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite S ou N')
    if resp in 'N':
        break
print('-=' * 40)
print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 40)
for k,v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15} ', end='')
    print()
print('-=' * 40)
while True:
    busca = int(input('Informe o codigo do jogador que deseja analisar (999 para parar):'))
    if busca == 999:
        break
    if busca >= len(time):
        print('ERRO! Codigo invalido!')
    else:
        print(f' => LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}:')
        for i,g in enumerate(time[busca]["Gols"]):
            print(f'    No jogo {i+1}º fez {g} gols')
    print('-=' * 40)
print('VOLTE SEMPRE!')