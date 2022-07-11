'''Escreva um programa que faça o computador “pensar” em um número
inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi
o número escolhido pelo computador. O programa deverá escrever na tela
se o usuário venceu ou perdeu.'''
from random import randint
from time import sleep
pc = randint(0,5)#Faz o computador "Pensar"
print('-=-'*20)
print('Vou pensar em um númeo entre 0 e 5. Tente advinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? '))#Jogador tenta advinhar
print('PROCESSANDO...')
sleep(3)
if jogador==pc:
    print('PARABÉNS!Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não n {}'. format(pc,jogador))
