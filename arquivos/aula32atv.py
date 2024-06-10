"""
Faça um programa que peça ao usuario para digitar um numero inteiro,
informe se este número é par ou ímpar. 
Caso o usuario não digite um numero inteiro, informe que não é um numero"""

entrada = input('Digite um numero: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'impar'

    if par_impar:
            par_impar_texto = 'par'

    print(f'O numero {entrada_int} é {par_impar_texto}')
else:
    print('Você não digitou um numero')



# usuario = input('Digite um numero inteiro: ')
# usuario = (int(usuario))

# if usuario % 2 == 0:
#     print("O numero que vc digitou é PAR")

# if  usuario % 2 == 1:
#     print("O numero que vc digitou é ÍMPAR")  


