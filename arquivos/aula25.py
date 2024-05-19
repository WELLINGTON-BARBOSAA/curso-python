'''
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456789)
'''
nome = 'Wellington'
idade = 29
cor = "Negra"
variavel = '%s tem a idade de %i, e sua cor é %s' % (nome, idade, cor)
print(variavel)