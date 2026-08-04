import json

# pessoa = {
#     'name': 'Wellington',
#     'lastname': 'Barbosa',
#     'adress': [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 57},
#     ],

#     'height': 1.8,
#     'numbers_preferred': (2, 4, 6, 8, 10),
#     'dev': True,
#     'nothing': None
    
# }

# with open('aula117.json', 'w') as arquivo:
#     json.dump(pessoa, 
#               arquivo,
#               indent=2) 

with open('aula117.json', 'r') as arquivo: # o comando procura o arquivo aula117.json
    pessoa = json.load(arquivo)
    print(pessoa['name'])

with open('aula117.json', 'r') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa['height'])

with open('aula117.json','r') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa['lastname'])
