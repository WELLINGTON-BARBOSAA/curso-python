# Exercicio 
# Peça ao usuario para digitar seu nome
# Peça ao usuario para digitar sua idade
# Se nome e idade forem digitados:
#     Exiba:
#         Seu nome é {nome}
#         Seu nome invertido é {nome invertido}
#         Seu nome contém (ou não) espaços
#         Seu nome tem {n} letras
#         A primeira letra do seu nome é {letra}
#         A ultima letra do seu nome é {letra}
# Se nada for digitado em nome ou idade:
#     Exiba "Desculpe, você deixou campos vazios.

nome = input ("Digite seu nome: ")
idade = input ("Digite sua idade: ")


if nome:
    print(f'Seu nome é : {nome}')
    print(f'Seu nome é invertido é : {nome[::-1]}')
    print(f'A primeira letra do seu nome é : {nome[0]}')
    print(f'A ultima letra do seu nome é : {nome[9]}')
    print(len(nome))
else:
    print("Desculpe, voce deixou campos vazios")

# Faltando como é contar se tem ou não espaço no nome





