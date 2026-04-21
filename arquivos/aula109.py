from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')


pessoas = [
    'João', 'Maria', 'André', 'Aparecida'
]

calças = [
    ['Preta', 'Branca'],
    ['P', 'M', 'G', 'EXG'],
    ['Osasco', 'Santa Helena', 'São Luiz']

]

# print(*list(combinations(pessoas,2 )), sep='\n') # não se repete as combinações
# print()
# print(*list(permutations(pessoas,2 )), sep='\n') # aqui se repete as combinações
print_iter(product(*calças))