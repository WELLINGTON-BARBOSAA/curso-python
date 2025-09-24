'''Escreva um programa que pergunte o salario de um funcionario e calcule o valor
de seu aumento.
Para salarios superiores as R$ 1.250,00, calcule o aumento de 10%
Para os aumentos inferiores ou iguais, o aumento é de 15% '''

nome = input('Digite seu nome: ')
salario_func = float(input('Digite o valor do seu salario: '))

aumento10 = (salario_func * 10) / 100
aumento15 = (salario_func * 15) / 100

if salario_func > 1250.00 :
    print(f'{nome}, seu o valor do seu salario é de R$ {salario_func:.2f}')
    print(f'Mas com o aumento vai ficar no valor de R$ {aumento10 + salario_func:.2f}')

elif salario_func <= 1250.00:
    print(f'{nome}, seu salario é de R$ {salario_func:.2f}')
    print(f'Mas com o novo aumento fica R$ {aumento15 + salario_func:.2f}')