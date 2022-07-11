a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
#Verificar quem é menor

if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
if a < b and a < c:
    menor=a
#Verificar quem é maior
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
if a > b and a > c:
        maior = a
print('O menor calor digitado foi {}.\nO maior valor digitado foi {}'.format(menor,maior))

