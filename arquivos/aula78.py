# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set() # vazio
# s1 = {'Wellington', 1,2,3} # com dados
# print(s1)



# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# l1 = [1,2,3,4,5,8,8,8,8,8,8,8,8,9,10] # valores duplicados
# l2 = set(l1) # Coerção 
# print(type(l1))



# # l2 = list(s1)
# s1 = {8,9,7,5,15,89,12,18,16,21,51,2,15,45,48}
# print(s1)
# for numero in s1:
#     print(0 in s1)


# metodos uteis em set
# add, update, clear e discard

# l1 = set()
# l1.add('Wellington') # add Só aceita um valor por vez 
# l1.add(1234567)
# l1.update(('Boa tarde', 1,2,5,5)) # tem que colocar aspas duplas para poder colocar + de 1 valor
# # l1.clear() # ele vai limpar o set 
# l1.discard('Boa tarde')
# l1.discard('Wellington') # serve para apagar valores
# print(l1)

# Operadores úteis: 
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {3, 2, 4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s1 - s2
s3 = s1 ^ s2 # esse mostra o que não tem em ambos, a ordem nesse caso não faz diferença
print(s3) 