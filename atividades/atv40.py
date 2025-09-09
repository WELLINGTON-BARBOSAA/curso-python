'Desenvolva um programa que pergunte a distancia de uma viagem em Km'
'Calcule o preço da passagem, '
'cobrando R$ 0.50 por km para viagens de até 200km e R$ 0.45 para as viagens mais longas'

distancia = int(input('Qual a distância da viagem: '))
preco_total = distancia * 0.50
preco_desc = distancia * 0.45

if distancia <= 200:
    print(f'A distancia foi de {distancia}, no valor de  R$ {preco_total:.2f}')

else:
    print(f'A distância foi {distancia}, no valor de R$ {preco_desc:.2f}')
