# # Dicionarios em Python (tipo dict)
# # Dicionarios são estruturas de dados do tipo
# # par de 'chave' e 'valor'.
# # Chaves podem ser consideradas como "indice"
# # que vimos na lista e podem ser de tipos imutaveis
# # como: str, int, float, bool, tuple, etc.
# # Valor pode ser de qualquer tipo, incluindo outro
# # dicionário
# # Usamos as chaves - {} - ou a class dict para criar
# # dicionarios
# # Imutáveis: str, int, float, bool, tuple
# # Mutável: dict, list



# # Manipulando chaves e valores em dicionarios

# pessoas = {}


# chave = 'nome completo'

# pessoas[chave] = 'Wellington Gomes'
# print(pessoas[chave])

# pessoas['Sobrenome'] = 'Barbosa de Sousa'
# print(pessoas['Sobrenome'])

# pessoas['Lugar no mundo'] = 'São Paulo'
# print(pessoas['Lugar no mundo'])

# del pessoas['Lugar no mundo']
# print(pessoas['Lugar no mundo']) # chave não encontrada porque foi apagada

# # Manipulando chaves e valores em dicionários
# pessoa = {}

# ##
# ##

# chave = 'nome'

# pessoa[chave] = 'Luiz Otávio'
# pessoa['sobrenome'] = 'Miranda'


# print(pessoa[chave])

# pessoa[chave] = 'Maria'

# del pessoa['sobrenome']
# print(pessoa)
# print(pessoa['nome'])

# # print(pessoa.get('sobrenome'))
# if pessoa.get('sobrenome') is None:
#     print('NÃO EXISTE')
# else:
#     print(pessoa['sobrenome'])
'______________________________________________________________________'
# # print('ISSO Não vai')
# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
# import copy

# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'l1': [0, 1, 2],
# }
# d2 = d1.copy()

# d2['c1'] = 1000
# d2['l1'][1] = 999999

# print(d1)
# print(d2)


# pessoa = {
#     'Nome': 'Wellington',
#     'Sobrenome': 'Gomes de Sousa Barbosa',
#     # 'Idade': 30

# }

# pessoa.setdefault('Idade', 800)
# print(pessoa['Idade'])
'____________________________________________________________________'

# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}
# print(p1['nome'])
# print(p1.get('nome', 'Não existe'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)
# p1.update({
#     'nome': 'novo valor',
#     'idade': 30,
# })
# p1.update(nome='novo valor', idade=30)
# tupla = (('nome', 'novo valor'), ('idade', 30))
lista = [['nome', 'novo valor'], ['idade', 30]]
p1.update(lista)
print(p1)