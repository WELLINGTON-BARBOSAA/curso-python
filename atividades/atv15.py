# Faça um Programa que pergunte quanto você ganha por hora e 
# o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês. 

ganho_hora = float(input('Quanto voce ganha por hora: '))
horas_tbdas = float(input('Digite sua carga horaria por dia: '))

ganho_mensal = (ganho_hora * horas_tbdas) * 30

print(ganho_mensal)