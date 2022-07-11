'''Faça um programa que leia uma frase pelo teclado e mostre
quantas vezes aparece a letra “A”, em que posição ela aparece
a primeira vez e em que posição ela aparece a última vez.'''
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.\n'
      'A primeira letra A aparece na posição {}\n'
      'A última letra A apareceu na posição {}.'
      .format(frase.count('A'),frase.find('A')+1,frase.rfind('A')+1))