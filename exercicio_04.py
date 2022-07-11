#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possives sobre ele.
a = input('Digite algo: ')
print('O tipo primitivo deste valor é {}\n'
      'So´tem espaços? {}'
      '\nÉ um numero? {}'
      '\nÉ alfabético? {}'
      '\nÉ alfanúmerico? {}'
      '\nEstá em maiúsculas? {}'
      '\n Está em minúsculas? {}'
      '\nEstá capitalizada? {}'
      .format(
              type(a),
              a.isspace()
              ,a.isnumeric()
              ,a.isalpha()
              ,a.isalnum()
              ,a.isupper()
              ,a.islower()
              ,a.istitle() ))
