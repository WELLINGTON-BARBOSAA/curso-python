'Enumerate - enumera os iteraveis (indices)'

# [(0,'Wellington')], (1, 'vai ser'), (2, 'Programador')]
lista = ['Wellington', 'Vai ser', 'Programador']
lista.append('Welliigton')


# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)

for tupla_enumerada in enumerate(lista):
    print('For da tupla')
    for valor in tupla_enumerada:
        print(f'\t{valor}')


# lista_enumerada = tuple(enumerate(lista))
# lista_enumerada = list(enumerate(lista)) # coerção de lista e tupla, outro jeito de enum iteravel
# lista_enumerada = tuple(enumerate(lista))

# print(lista_enumerada)

# for item in enumerate(lista): um metodo de fazer enumerar iterador
#     print(item)

# lista_enumerada=(enumerate(lista))
# print(next(lista_enumerada))