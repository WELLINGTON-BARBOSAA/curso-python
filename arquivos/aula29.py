'''
Introdução ao try/except
try -> tentar executar o codigo
except -> ocorreu algum erro ao tentar executar'''

numero_str = input('Vou dobrar o numero que vc digitou: ')
# DICA - > Para mudar o nome de uma variavel sem precisar
# mudar todas, clica na  primeira variavel e aperte F2
try:
    numero_float = float(numero_str)
    print("FLOAT: ", numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2 :.2f}')
except:
    print('Isso não é um número')


# numero_1 = input  ("Digite o primeiro numero: ")
# numero_2 = input  ("Digite o segundo numero: ")
# conta_1 = int (numero_1)
# conta_2 = int (numero_2)

# try:
#     print(f"Resultado da conta é: {conta_1 + conta_2}")

# except:
#     print('Voce não digitou um numero')
