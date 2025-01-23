# Exercicios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variavel e mostre o valor
# da variavel

# def multiplicacao (*args):
#     total = 1
#     for numeros in args:
#         total *= numeros
#     return total # para o return ser executado corretamente, sempre colocar um tab a frente
#                  # da função  
# resultado = multiplicacao(1,2,3,4,5,6)
# print(resultado)

# Crie uma função que fala se o numero é par ou ímpar.
# Retorne se o numero é par ou ímpar


# def par_impar(x):
#     return x % 2 == 0

# resultado = par_impar(2)
# print(resultado)

def par_impar (numero):
    multiplo_de2 = numero % 2 == 0
    if multiplo_de2:
        return 'f {numero} é par' 
    return 'f {numero} é impar'


print(par_impar(5))