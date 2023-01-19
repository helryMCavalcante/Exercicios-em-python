frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print('O nome {} invertido fica {}'.format(junto, inverso))
if junto == inverso:
    print('A frase digitada É UM palíndromo!')
else:
    print('A frase digitada NÃO É UM palíndromo')