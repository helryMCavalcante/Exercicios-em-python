matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaP = somaT = maior = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Informe os valores para preencher as linhas e colunas {[l]} {[c]}: '))
        if matriz[l][c] % 2 == 0:
            somaP += matriz[l][c]
    somaT += matriz[l][2]

for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]

print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^7}]', end='')
    print()
print('-='*30)

print(f'A soma dos valores pares da matriz é {somaP}')
print(f'A soma dos valores na terceira coluna é {somaT}')
print(f'O maior valor da segunda linha é {maior}')