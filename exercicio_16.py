'''Crie um programa que leia un número Real qualquer pelo
teclado e mostre na tela a sua porção Inteiro Ex: Digite
um número: 6.127 O número 6.127 tem a parte inteira 6.'''

n = float(input('Digita um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(n,int(n)))