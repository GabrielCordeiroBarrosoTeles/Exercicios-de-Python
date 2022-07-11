'''Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.'''
nome = str(input('Digite seu nome completo: ')).strip()
name = nome.split()
print('Muito prazer em te conhecer!\nSeu prmeiro nome é {}\nSeu último nome é {}'
      .format(name[0],name[len(name)-1]))
