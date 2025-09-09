'Desenvolva um programa que pergunte a distancia de uma viagem em Km'
'Calcule o preço da passagem, '
'cobrando R$ 0.50 por km para viagens de até 200km e R$ 0.45 para as viagens mais longas'

distancia = int(input('Qual a distância da viagem: '))
km_menor = distancia * 0.50
km_maior = distancia * 0.45

if distancia <= 200:
    print(f'Sua distancia foi de {distancia} Km ')
    print(f'O valor da viagem vai custar {km_menor}')

if distancia > 200:
    print(f'Sua distancia foi de {distancia} Km')
    print(f'O valor da viagem com desconto é de {km_maior}')

else:
    print('Você não digitou nada')