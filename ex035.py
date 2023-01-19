print('-=-'*15)
print('Analisador de triângulos')
print('-=-'*15)
a = float(input('Informe o primeiro segmento: '))
b = float(input('Informe o segundo segmento: '))
c = float(input('Informe o terceiro segmento: '))
if b + c > a and a + c > b and a + b > c:
    print('Os segmentos acima \033[32mPODEM FORMAR\033[m um triângulo!')
else:
    print('Os segmentos acima \033[31mNÃO PODEM FORMAR\033[m um triângulo!')