'''Faça um Programa que pergunte quanto você ganha por hora 
e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês.'''

salario_hora = float(input('Digite seu ganho por hora: '))
horas_trabalhadas = float(input('Carga horária por dia: '))

salario_mes = (salario_hora * horas_trabalhadas) * 30

print(f'Seu salario no final do mês é: {salario_mes:.2f}')

#print(salario_hora)

