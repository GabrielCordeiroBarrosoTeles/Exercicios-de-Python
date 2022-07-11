'''Faça um algoritmo que leia o salario de um funcionário e mostre seu novo salário, com 15% de aumeto.'''
salario = float(input('Qual é o salário do Funcionário? R$ '))
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario,salario+(salario*15/100)))