#Desempacotamento em chamadas
#de metodos e funções

string = 'ABC'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

for nome in lista:
    print(nome, end=' ') # esse movimento quebra a linha 

print(*lista)
print(*string)
print(*tupla)

# residencia = [

# ['Jose Alfredo', 'Raimundo Neto', 'Augusto Antonio'],
# ['Fernada Lima', 'Monique Santanda', 'Bruno Cesar'],
# ['Rihana Gomes', 'Lebron Barbosa', 'Stan lee'],

# ]


# print(*residencia, sep='\n') # Esse comando desempacota e quebra linha deixando organizado o código