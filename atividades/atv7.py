# my_list = [1, 2]
# print(my_list * 3)
# print(my_list + [3,4])

' Faça um Programa que peça dois números e imprima o maior deles. '

try:

    numero1 = int(input('Digite um numero: '))
    numero2 = int(input('Digite outro: '))

    if numero1 > numero2 : 
        print (f'O numero {numero1} é maior que o numero {numero2}')
    elif numero2 > numero1:
        print(f'O numero {numero2} é maior que o numero {numero1}')
    elif numero1 == numero2:
        print('Números iguais')

except ValueError:
    print('Você não digitou um numero')