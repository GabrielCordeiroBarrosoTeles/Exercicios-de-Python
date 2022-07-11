'''Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta , pinta uma área de 2m².'''

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
print('Sua parede tem a dimensão de {}x{}.\n'
      'Sua área é de {}m².\n'
      'Para pintar essa parede, você precisará de {}l de tinta.'
      .format(largura,altura,largura*altura,(largura*altura)/2))