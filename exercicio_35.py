'''Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.'''
print('-=-'*20,'\nAnalisador de Triangulos\n','-=-'*20)
reta_1 = float(input('Primeiro segmento: '))
reta_2 = float(input('Segundo segmento: '))
reta_3 = float(input('Terceiro segmento: '))
if reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_1 + reta_2:
    print('Os segmentos acima PODEM FORMAR um triangulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triangulo!')
