'''Faça um programa que leia o comprimento do cateto oposto e 
do cateto adjacentede uma tringulo retangulo, 
calcule e mostre o comprimento da hipotenusa'''

import math

cateto_oposto = float(input('Digite o valor do cateto aposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = (cateto_oposto**2) + (cateto_adjacente**2)
hipotenusa2 = math.sqrt(hipotenusa)
print(f'Valor da hipotenusa é da raiz de {hipotenusa} é de {hipotenusa2:.2f}')


#deixar o codigo mais clean