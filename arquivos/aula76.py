# Dicionarios em Python (tipo dict)
# Dicionarios são estruturas de dados do tipo
# par de 'chave' e 'valor'.
# Chaves podem ser consideradas como "indice"
# que vimos na lista e podem ser de tipos imutaveis
# como: str, int, float, bool, tuple, etc.
# Valor pode ser de qualquer tipo, incluindo outro
# dicionário
# Usamos as chaves - {} - ou a class dict para criar
# dicionarios
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list

'Criando um jogo'

personagem = {
    'Nome': 'Arthur',
    'Sobrenome': 'Morgan',
    'DataNasc': '1983',
    'Idade': 47,
    'Altura': 1.80,
    'Peso': 1.85,
    'Endereços' : [
        {'Cidade': 'Valentines', 'Logradouro': 'Zona Rural', 'Numero': 'S/N' },
         {'Cidade': 'Sant Denis', 'Logradouro': 'Zona Rural', 'Numero': 'S/N' },
         {'Cidade': 'Rhoades', 'Logradouro': 'Zona Rural', 'Numero': 'S/N'},
    ],

}

# print(personagem['Endereços'])
# print(personagem['Peso'])
# print(personagem['DataNasc'])
# print(personagem['Sobrenome'])


for chave in personagem:
    print(chave, personagem[chave])