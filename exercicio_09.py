'''Faça um programa que leia um número Inteiro qualquer e mostre na tela a tabuada.'''
num = int(input('Digite um número para ver sua tabuada: '))
print('-'*12)
print('Tabuada do {}\n'
      '{} x {:2} = {}\n'
      '{} x {:2} = {}\n'
      '{} x {:2} = {}\n'
      '{} x {:2} = {}\n'
      '{} x {:2} = {}\n'
      '{} x {:2} = {}\n'
      '{} x {:2} = {}\n'
      '{} x {:2} = {}\n'
      '{} x {:2} = {}\n'
      '{} x {:2} = {}'
      .format(
              num,num,1,num*1,
              num,2,num*2,
              num,3,num*3,
              num,4,num*4,
              num,5,num*5,
              num,6,num*6,
              num,7,num*7,
              num,8,num*8,
              num,9,num*9,
              num,10,num*10 ))
print('-'*12)
