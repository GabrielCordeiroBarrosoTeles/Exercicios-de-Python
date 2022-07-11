'''Crie um programa que leia o nome de uma pessoa e diga se ela tem “cordeiro” no nome.'''
nome = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Sliva? {}'.format('cordeiro' in nome.lower()))