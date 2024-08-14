'Introdução ao desempacotamento'

# nomes = ['Welllinton', 'vai ser', 'Programador']
# nome1, nome2, = nomes
# print(nomes)

_, nome1, _, *_ = ['Wellington', 'Vai ser','Programador'] #modo de separar cada valor do pacote
print(nome1, _) # uma convenção que é usada por todos dev, o _ é uma variavel que não vai ser usada
# Quando for ignorar o valor utilizar _