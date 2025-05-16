'''Faça um programa que leia a largura e altura de uma parde em metros
Calcule a sua area e a quantidade de tinta necessaria para pinta la 
sabendo que cada litro de tinta pinta uma area de 2m²'''

# largura = float(input('Qual é a largura da parede: '))
# altura = float(input('Qual altura da parede: '))
# cal_area = altura * largura
# print(f'As medidas são {largura} x {altura}, sua area calculada é de : {cal_area:.2f} M²')
# tinta = cal_area / 2
# print(f'Será necessario {tinta}L de tinta para pintar area.')

def area (altura, largura):
    return altura * largura

print(f'Sua area é de {area(5,5)}M²')


# Meter um try e except para o usuario poder digitar o valor 
