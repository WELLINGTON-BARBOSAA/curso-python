# função format 

a = 'AAAAAA'
b = 'Bc'
c = 1.1
string = 'a={nome1} b={nome2} b={nome2}b={nome2} c={nome3:.2f}' 
formato = string.format(
    nome1 = a, nome2 = b, nome3 = c)

"""Ao passar valores para chaves (tudo que tem indice começa no 0) pode utilizar editar sem
precisar seguir a ordem de como era antes"""
print(formato)

# string = 'a={} b{} c={:.2f} {}' 
# Acima vimos que dentro da função format existem 3 valores a serem executados
# Mas quando se chama um chave que não se tem valores aparece esse erro
# Replacement index 3 out of range for positional args tuple
# Quando fala sobre of range, significa que esta tentando chamar algo que já acabou