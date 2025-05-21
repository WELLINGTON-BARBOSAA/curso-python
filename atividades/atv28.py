'Faça um algoritmo que leia um preço e mostre'
'seu novo preço, com desconto de 5%'

# preco = float(input('Digite o valor do preço: '))
# des = preco * 15/100
# resul_des = preco - des
# print(f'O preço original é de {preco}, mas com os desconto de 5% vai fica {resul_des:.2f}')


def desconto (preco):
    return preco *15/100

# print(desconto(300))

while True:
    try:
        preco_atual = float(input('Digite o preço do valor: '))
        preco_desconto = desconto(preco_atual)
        preco_final = preco_atual - preco_desconto
        print(f'O produto custa R$ {preco_atual:.2f}, mas com o desconto fica R$ {preco_final:.2f}')    
        break
    except ValueError: 
        print('Voce não digitou um numero, tente novamente') 