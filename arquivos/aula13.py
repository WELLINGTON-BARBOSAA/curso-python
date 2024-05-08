# nome = "Wellington"
# altura = 1.70
# peso = 76
# imc = peso / altura ** 2

# "f-strings"

# linha_1 = f'{nome} tem {altura:.2f} de altura' 
# # a função f' ' fora do parenteses é deixar o codigo mais organizado (f de formatação)
# # altura:.2f significa quantas casas decimais eu quero colocar
# # altura:,.2f significa quantas casas decimais eu quero colocar ou com quantas virgulas (dinheiro)
# linha_2 = f"pesa {peso} e seu imc é"
# linha_3 = f'{imc:.2f}' 
# print(linha_1)
# print(linha_2)
# print(linha_3)



nome = "Wellington"
peso = 71
altura = 1.70
imc = peso / altura ** 2

linha_1 = f'Seu nome é {nome}, e tem de altura {altura:.2f}'
linha_2 = f'Tem um peso de {peso}'
linha_3 = f'seu imc é de {imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

