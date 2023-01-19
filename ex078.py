valores = []
for cont in range(0,5):
   valores.append(int(input('Digite um valor: ')))

print(f'O maior valor da lista é {max(valores)} na posição ', end='')
for i,v in enumerate(valores):
    if v == max(valores):
        print(f' {i}')

print(f'O menor valor da lista é {min(valores)} na posição ', end='')
for i,v in enumerate(valores):
    if v == min(valores):
        print(f' {i}')

