from math import factorial
num = int(input('Digite um número: '))
c = num
f = factorial(num)
print('{}! = '.format(num), end='')
while c > 0 :
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
print('{}'.format(f))