numero_1 = input ("Digite o primeiro numero: ")
numero_2 = input ("Digite o segundo numero: ")

conta_1 = int (numero_1)
conta_2 = int (numero_2)

print(f" a soma dos valores é: {conta_1 + conta_2}")



# Tudo dentro de aspas vira uma STR, por isso foi utilizado a coerção de STR para INT. 
# para o programa identificar que aquilo vai se transformar em um numero inteiro

# nome = input("Digite seu nome: ")
# print(f"Seu nome completo é {nome=}")
# nome= é utilizado para da valor a variavel

# Todo nome de variavel é str, então pode ocorrer erro quando tentar tranformar em int uma str
# digitada pelo usuario, quebrando assim o programa. Ex 
# numero_1 = int(input("Digite o primeiro numero: "))
# O mais seguro de se fazer nessas situações é criar uma outra variavel com nome int_numero1
# de facil identificação e assim fazer a coerção, como ocorre abaixo.

