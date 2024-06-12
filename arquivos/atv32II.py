""" Faça um programa que pergunte a hora ao usuario e, 
baseando-se no horario descrito, exiba a saudação apropriada. Ex
Bom dia 0-11, Boa tarde 13-17 e Boa noite 18-23 """

entrada = input('Digite a hora em numero inteiro: ')

try:
    entrada = int(entrada)
    
    if entrada >= 0 and entrada <= 11:
        print('Bom dia, Usuario')
        print('Seja bem vindo')

    elif entrada >= 13 and entrada <= 17:
        print('Boa tarde, usuario')
        print('Seja bem vindo')

    elif entrada >= 18 and entrada <= 23:
        print('Boa Noite, usuario ')
        print('Seja bem vindo')
    
    else:
        print("Isso não é um numero")

except:
    print('Você não digitou um numero')


















# MINHAS TENTATIVAS 
# # saudação = input('Digite a hora por gentileza: ')
# boa_dia = 
# boa_tarde = 
# boa_noite = 

# if saudação and boa_dia:
#     print('Bom dia')

# if saudação and boa_tarde:
#     print('Boa tarde')

# if saudação and boa_noite:
#     print('Boa noite')
