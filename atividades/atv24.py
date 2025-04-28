"Escreva um programa que pergunte a quantidade de km percorrido por um carro alugado"
"e a quantidade de dias pelos quais foram alugados. Calcule o preço a pagar, "
"sabendo que o carro custa 60 reais por dias e 0,15 por Km rodado "

# dias_alugado = int(input('Quantos dias alugado: '))
# km_alugado = float(input('Quantos Km percorridos: '))

# a_pagar = (dias_alugado * 60) + (km_alugado * 0.15)

# print(f'o valor total a pagar é de: {a_pagar}')


def km_percorrido(quilometragem):
    return quilometragem * 0.15

def dias_alugado(dias):
    return dias * 60

while True:
    try:
        quilometragem = float(input('Quantos km: '))
        dias = int(input('Quantos dias alugados: '))
        pagar = km_percorrido(quilometragem) + dias_alugado(dias)
        print(f'o valor a pagar é de : {pagar}')
        break

    except ValueError:
        print('Voce digitou algo errado, tente novamente')
