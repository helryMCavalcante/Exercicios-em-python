import math
angulo = float(input('Digite o angulo que você deseja: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O Ângulo de {} tem o SENO de {:.2f}'.format(angulo,sen))
print('O Ângulo de {} tem o COSSENO de {:.2f}'.format(angulo,cos))
print('O Ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tan))