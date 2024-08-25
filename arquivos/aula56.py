"""
split e join com list e str
split - divide uma string (retorna uma lista)
join - une uma string"""
# strip corta os espaços onde tiver\rtrip corta os da direita e lstrip corta os da esquerd

frase = 'Olha só, a Duda passou em medicina'
lista_frases_cruas = frase.split(',') # divide um uma string em determinado caracter

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(lista_frases)

frases_unidas = '/'.join(lista_frases) # '/' indica qual caractere eu quero usar como separador
print(frases_unidas)


# join é um metodo de string, que cria ela vazia
# vai ser usado para separação pa os itens do seu iteravel
# apenas string, lista e tuplas. Se caso colocar numeros no metodo join o codigo da erro