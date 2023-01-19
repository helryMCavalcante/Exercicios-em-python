cont = num = 0
while True:
    print('-=-'*10)
    num = int(input('Quer ver a tabuada de qual valor?'))
    if num < 0:
        break
    for cont in range(1,11):
        print(f'{num} x {cont} = {num * cont}')


