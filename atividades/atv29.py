'''Faça um programa que leia o salario de um funcionario e mostre o seu novo
salario com 15% de aumento'''

salario_at = float(input('Digite seu salario atual: '))
reajuste = salario_at * 15/100
# salario_resj = reajuste + salario_at
novo_salario = salario_at + reajuste

print(f'Seu antigo salrio era de R$ {salario_at}, com o resjuaste fica R${novo_salario:.2f}')