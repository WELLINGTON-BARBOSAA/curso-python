'''Faça um programa que leia o comprimento do cateto oposto e 
do cateto adjacentede uma tringulo retangulo, 
calcule e mostre o comprimento da hipotenusa'''

# import math

# cateto_oposto = float(input('Digite o valor do cateto aposto: '))
# cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))
# hipotenusa = (cateto_oposto**2) + (cateto_adjacente**2)
# hipotenusa2 = math.sqrt(hipotenusa)
# print(f'Valor da hipotenusa é da raiz de {hipotenusa} é de {hipotenusa2:.2f}')


#deixar o codigo mais clean

# import math

# cateto_oposto = float(input('Digite o valor do cateto oposto: '))
# cateto_adj = float(input('Digite o valor do cateto adjacente: '))
# hipotenusa = math.hypot(cateto_oposto, cateto_adj)
# print(f'O valor da hipotenusa é de {hipotenusa:.2f}')

'Fazer uma com funções e tratamento de exceções'
'Tem como usar modulo com funções'


def hipotenusa(c_oposto, c_adjacente):
    return (c_oposto ** 2) + (c_adjacente **2) 

while True:
    try:
        cateto_oposto = float(input('Digite o cateto oposto: '))
        cateto_adjacente = float(input('Digite o cateto adjacente: '))
        valor_hipotenusa = hipotenusa(cateto_oposto,cateto_adjacente)
        print(f'Valor da hipotenusa é de {valor_hipotenusa:.2f}')
        break

    except Exception:
        print("Você digitou algo errado")

