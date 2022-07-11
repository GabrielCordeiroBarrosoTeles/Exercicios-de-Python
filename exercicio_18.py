'''Faça um programa queleia um ângulo qualquer e mostre
na tela o valor do seno, cosseno e tangente desse ãngulo'''
from math import radians,sin,cos,tan
angulo = float(input('Digita um ângulo qualquer: '))
print('O ângulo de {} tem o SENO de {:.2f}\n'
      'O ângulo de {} tem o COSSENO de {:.2f}\n'
      'O ângulo de {} tem o TANGENTE de {:.2f}'
      .format(angulo,sin(radians(angulo)),angulo,cos(radians(angulo)),angulo,tan(radians(angulo))))

