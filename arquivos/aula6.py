# Conversão de tipos, coerção
# type convertion , typecasting, coercion
# é o ato de converter um em outro
# tipos imutaveis e primitivos
# str, int, float e bool

print(1 + 1)
print('a' + 'a')  # Polimorfismo, quando usa o mesmo operado para fazer coisas diferentes
 
# Colocando as aspas o numero um deixa de ser um int,
# para se tornar um str, assim dando erro ao executar como aparece no terminal.
print('1', type('1'))
print(1.1, type('1.1'))
print('Mal', type('Mal'))

print(int('-22'), type(int('-22')))
# Ao colocar qualquer caractere em aspas , ela se torna um str -> String
# Mas para fazer a coerção disso é usado o comando que necessita a tranformação ex: acima
# foi colocado int, porque queria tranformar um str em um int = inteiro.
print(int("22") + 22)
print(float("22") + 22)
print(type(float("22") + 22))
# Lembrando que a execução é feita de dentro para fora de acordo com os parenteses
print(bool(""))
print(bool("  "))
print(str(11) + 'b')
print(str(354) + "u")
print(str(8) + "b")

"Ctrl + Shift + A = transformar um comando em comentario"