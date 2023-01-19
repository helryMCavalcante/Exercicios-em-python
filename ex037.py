from time import sleep

num = int(input('Digite um número inteiro: '))
print('''Escolha uma base para conversão
[1] Converter para Binario
[2] Converter para Octal
[3] Converter para Hexadecimal''')

opção = int(input('Sua opção: '))
print('Sua opção foi {}'.format(opção))
print('Convertendo...')
sleep(3)

if opção == 1:
    print('{} convertido em binario é igual á {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido em Octal é igual á {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido em Hexadecimal é igual á {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida. Digite novamente!')