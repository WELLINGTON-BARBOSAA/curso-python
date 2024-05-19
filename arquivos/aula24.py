# Operadores in e in not 
# Strings são iteráveis
# 0 1 2 3 4 5 6 7 8 9   
# W e l l i n g t o n
#-9-8-7-6-5-4-3-2-1-0

# nome = input ("Digite seu nome: ")
# print (f'Seu nome é: {nome}') 

nome = 'Wellington'
# print(nome[0])
# print(nome[-10])
# print ('g' in nome)
# print ('t' in nome)
# print (10 * '--')
# print ('a' not in nome)

# not in inverte  situação, 
# o que era false se torna true 
# e o que era True vira False

nome = input('Digite seu nome: ')
encontrar = input ("O que deseja encontrar?: ")

if encontrar in nome:
    print (f"{encontrar} tem em {nome} ")
else:
    print (f"{encontrar} não tem em {nome}")
