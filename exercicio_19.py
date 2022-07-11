'''Um professor quer sortear um dos seus quatros alunos para apagar o quadro.
Faça um programa que ajude ele,lendo o nome deles e escreva o nome do escolhido'''
from random import choice
aluno_1 = (input('Primeiro aluno: '))
aluno_2 = (input('Segundo aluno: '))
aluno_3 = (input('Terceiro aluno: '))
aluno_4 = (input('Quarto aluno: '))
print('O aluno escolhido foi {}'. format(choice([aluno_1,aluno_2,aluno_3,aluno_4])))
