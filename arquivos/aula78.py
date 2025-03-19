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



# l2 = list(s1)
s1 = {8,9,7,5,15,89,12,18,16,21,51,2,15,45,48}
print(s1)
for numero in s1:
    print(0 in s1)

