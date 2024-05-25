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
# #     Exiba "Desculpe, você deixou campos vazios.

# nome = input(f'Digite seu nome: ')
# idade = input(f'Sua idade é: ')

# if nome and idade:
#     print(f"Seu nome é {nome}")
#     print(f'Seu nome invertido é {nome[::-1]}')

#     if ' ' in nome:
#         print("Seu nome tem espaço")

#     else:
#         print("Seu nome NÃO tem espaço")
    
#     print(f'Seu nome tem {len(nome)[0]} letras')
#     print(f'A primeira letra do seu nome é {nome[0]}: ')
#     print(f'A ultima letra do seu nome é {nome[-1]}')


# else:
#     print("Voce deixou campos vazios") 

# EXERCICIO RESOLVIDO PELO LUIZ OTÁVIO e WELLINGTON <3

nome = input("Digite seu nome completo: ")
idade = input("Digite sua idade: ")

if nome and idade:
    print(f'Seu nome completo é: {nome}')
    print(f'Sua idade é: {idade}')
    print(f'Seu nome invertido é: {nome[::-1]}')

    if " " in nome:
        print("Seu nome completo TEM espaço")

    else:
        print('Seu nome completo NÃO espaço')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome: {nome[0]}')
    print(f'A ultima letra do seu nome é:{nome[-1]} ')
else:
    print('Você deixou campos vazios')