"""
Listas em Python
Tipo list - Mutável 
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - indices e fatiamento
Métodos úteis: 
append - adiciona um item ao final
 insert - adiciona um item no indice escolhido 
 pop - remove do final ou indice escolhido
 del - apaga a lista
 clear - limpa a lista
 extend - estende a lista
 + - concatena a lista
Create, Read, Update, Delete (CRUD)
Criar, Ler, alterar, apagar = lista [i] (CRUD)"""


#........+01234
#........-54321
# string = 'ABCDE' # 5 caracteres (len)

#........0.....1........2..........3...4 
#.......-5...-4.......-3.........-2...-1 
# lista = [123, True, "Wellington", 1.2, []]
# lista[-3] = 'Maria' # Nessa linha é alterado a str de 'Wellington' para 'Maria'
# print(lista)
# print(lista[2], type(lista[2]))

# lista = [1, False, 55, 3.2, 'Wellington' , 100] # conchetes significa esta chamando a lista []
# lista[4] = 'Maria' # Aqui eu mudei o valor de 'Wellington' para 'Maria'
# print(lista)
# print(lista[0], lista[3], lista[5])

# ___________________________________________

#       -4..-3..-2...-1 - DICA - para descobrir ultimo numero do seu indice, comece pelos negativos
#       0....1...2....3
# lista = [10, 20, 30, 40] 

# ______________________________

# lista = [10, 20, 30, 40] # Exemplo de criar [i]
# # lista[2] = 300 # Exemplo de alterar [i]
# # del lista[3] # Exemplo de deletar [i]
# # print(lista)
# # print(lista[2])
# lista.append(50) # da o comando para adicionar mais indices no final deles
# lista.pop() # remove o ultimo indice, no caso o de cima que é o 50
# lista.append(60) # da o comando para adicionar mais indices no final deles
# lista.append(70) # da o comando para adicionar mais indices no final deles
# lista.append(80) # da o comando para adicionar mais indices no final deles
# ultimo_valor = lista.pop() # comando por se é colocando valor do indice dentro do [2], apaga o selecionado
# # lista.clear() - comando para limpar a lista
# lista.insert(0, 131) # comando para selecionar um indice onde deseja coloca - lo
# # O numero 0 indica qual o indice eu quero mexer. Com a virgula separando, coloca o valor que vai ser inserida
# print(lista, 'Removido', ultimo_valor) # remove o ultimo indice, no caso o de cima que é o 80

# _______________________________________________________________
# Concatenando e estendendo listas em Pytnhon

# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6]
# # lista_c = lista_a + lista_b
# lista_d = lista_b.extend(lista_a)
# print(lista_b)

# _________________________________________________

'''Cuidados com dados mutaveis
= - copiado o valor (imutaveis)
= - aponta para o mesmo valor na memoria (mutável)
'''

lista_a = ['Wellington', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy() # Comando copy copia a lista original sem modificação

lista_a [0] = 'Jose'
print(lista_a)
print(lista_b)


# numeros = [1, 2, 3, 4, 5, 6, 7, 8]

# def dividendo (x, y):
#     return x / y

# multi = [dividendo(numero, 2) for numero in numeros]
# print(multi)
