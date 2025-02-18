# Manipulando chaves e valores em dicionarios

pessoas = {}


chave = 'nome completo'

pessoas[chave] = 'Luiz Otavio' # Criando Chaves
pessoas['Sobrenome'] = 'Miranda'

pessoas[chave] = 'Maria' #Editando chave
#print(pessoas[chave])
print(pessoas['Sobrenome'])

del pessoas ['Sobrenome'] # Apagando chaves
print(pessoas['Sobrenome'])

