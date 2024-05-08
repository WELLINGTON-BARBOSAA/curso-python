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


nome = 'Wellington Gomes de Sousa Barbosa'
idade = 29
peso = 71
altura = 1.70
imc = peso / altura ** 2

linha_1 = f'Seu nome é:{nome}'
linha_2 = f'Sua idade é: {idade}'
linha_3 = f'Seu peso é:{peso}'
linha_4 = f'Sua altura é: {altura:.2f}'
linha_5 = f'seu imc é de: {imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
print(linha_4)
print(linha_5)

