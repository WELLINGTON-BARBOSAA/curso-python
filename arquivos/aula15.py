# nome = input("Digite seu nome: ")
# print(f"Seu nome completo é {nome=}")
# nome= é utilizado para da valor a variavel
numero_1 =input("Digite o primeiro numero: ")
numero_2 =input("Digite o segundo numero: ") 
# Todo nome de variavel é str, então pode ocorrer erro quando tentar tranformar em int uma str
# digitada pelo usuario, quebrando assim o programa. Ex 
# numero_1 = int(input("Digite o primeiro numero: "))
# O mais seguro de se fazer nessas situações é criar uma outra variavel com nome int_numero1
# de facil identificação e assim fazer a coerção, como ocorre abaixo.  
int_numero1 = int (numero_1)
int_numero2 = int (numero_2)
print(f'A soma dos numeros é de {int_numero1 + int_numero2}')
