'''Crie um sistema que leia um número e mostre o seu dobro, triplo e a raiz quadrada'''
import  math
n = int(input('Digite um numero: '))
print('O dobro de {} vale {}.\nO triplo d {} vale {}.\nA raiz quadrada de {} vale {:.2f}'.format(n,(n*2),n,(n*3),n,math.sqrt(n)))
