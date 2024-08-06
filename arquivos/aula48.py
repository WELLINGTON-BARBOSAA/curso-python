"""


Listas em Python
Tipo list - Mutável 
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - indices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +"""

#........+01234
#........-54321
string = 'ABCDE' # 5 caracteres (len)

#........0.....1........2..........3...4 
#.......-5...-4.......-3.........-2...-1 
# lista = [123, True, "Wellington", 1.2, []]
# lista[-3] = 'Maria' # Nessa linha é alterado a str de 'Wellington' para 'Maria'
# print(lista)
# print(lista[2], type(lista[2]))

lista = [1, False, 55, 3.2, 'Wellington' , 100] # conchetes significa esta chamando a lista []
lista[4] = 'Maria' # Aqui eu mudei o valor de 'Wellington' para 'Maria'
print(lista)
print(lista[0], lista[3], lista[5])




