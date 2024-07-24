'''AULA DE COMO O FOR FUNCIONA POR BAIXO DOS PANOS
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador 
'''
# for letra in texto
texto = 'Luiz' # iterável 

# iteratador = iter(texto) # iterator

# while True:           DA LINHA 11 A 16 É A FORMA QUE O FOR AGE, SEM PRECISAR DAR VOLTAS
#     try:
#         letra = next(iteratador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)

# ISSO TORNA A EXECUAÇÃO DO PROGRAMA MAIS SIMPLES