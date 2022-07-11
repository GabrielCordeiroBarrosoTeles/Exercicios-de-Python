'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.'''
n = int(input('Informe um número: '))
print('Analisando o número {}\n'
      'Unidade: {}\n'
      'Dezena: {}\n'
      'Centena: {}\n'
      'Milhar: {}\n'
      .format(n,n // 1 % 10,n //  10 % 10,n // 100 % 10,n // 1000 % 10))
