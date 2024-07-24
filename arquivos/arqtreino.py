nome = 'Eduarda'
i = 0
letra_por_letra = ''

while i < len(nome):
    letra_por_letra = nome [i]
    letra_por_letra += f'*{letra_por_letra}*'
    i += 1

    print(letra_por_letra)


# nome = 'Welllington'  # Iteráveis

# indice = 0
# novo_nome = ''
# while indice < len(nome):
#     letra = nome [indice]
#     novo_nome += f'*{letra}'
#     indice += 1

# print(novo_nome)