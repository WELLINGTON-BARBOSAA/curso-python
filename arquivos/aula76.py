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


usuario = {
    'Nome': 'Wellington',
    'Sobrenome': 'Gomes de Sousa Barbosa',
    'DatNasc': 15031995,
    'Endereço': 'Morro Doce',
    'CEP': 5267030,
    'CPF': 50822250305,
    'Nome da mae': 'Alaide Gomes de Sousa',
    'Nome do pai': 'Valdemir Barbosa'
}

print(usuario['Nome'])