'''Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.'''
medida = float(input('Uma distância em metros: '))
print('A medida de {}m coresponde a {:.0f}cm e {:.0f}mm.'.format(medida,medida*100,medida*1000))