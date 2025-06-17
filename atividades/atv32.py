'''Faça um programa que leia um angulo qualquer e mostre
na tela o valor seno, cosseno e tangente desse angulo.'''

# Seno (sen): sen θ = cateto oposto / hipotenusa
# Cosseno (cos): cos θ = cateto adjacente / hipotenusa
# Tangente (tan ou tg): tan θ = cateto oposto / cateto adjacente 


# angulo = int(input('Digite o valor do angulo: '))

# cat_adj = int(input('Digite o valor do cateto adjacente: '))
# cat_opo = int(input('Digite o valor do cateto oposto: '))
# hipo = int(input('Digite o valor da hipotenusa: '))

# sen = cat_opo / hipo
# cos = cat_adj / hipo
# tan = cat_opo / cat_adj


# print(f'O valor de do Seno é de {sen:.2f}')
# print(f'O valor de Cosseno é de {cos:.2f}')
# print(f'O valor da Tangente é {tan:.2f}')


'sohcahtoa = formulas da trigonometria'

from math import radians, sin, tan, cos

angulo = float(input('Digite o valor do seu angulo: '))

seno = sin(radians(angulo))
print(f'O valor de SENO é de {seno:.2f}')

cosseno = cos(radians(angulo))
print(f'O valor de COSSENO é de {cosseno:.2f}')

tangente = tan(radians(angulo))
print(f'O valor da TANGENTE é de {tangente:.2f}')