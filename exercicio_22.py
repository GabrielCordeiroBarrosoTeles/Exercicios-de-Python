'''Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.'''
nome = str(input('Digite seu nome completo: ')).strip()
separa = nome.split()
print('Analisando seu nome...\n'
      'Seu nome maiúsculas é {}\n'
      'Seu nome minúsculas é {}\n'
      'Seu nome tem ao todo {} letras\n'
      'Seu primeiro nome é {} e tem {} letras'
      .format(nome.upper(),nome.lower(),len(nome) - nome.count(' '),separa[0],nome.find(' ')))