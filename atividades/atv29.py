'''Faça um programa que leia o salario de um funcionario e mostre o seu novo
salario com 20% de aumento'''

# salario_at = float(input('Digite seu salario atual: '))
# reajuste = salario_at * 20/100
# # salario_resj = reajuste + salario_at
# novo_salario = salario_at + reajuste

# print(f'Seu antigo salrio era de R$ {salario_at}, com o resjuaste fica R${novo_salario:.2f}')

def reajuste(preco):
    return preco *20/100

while True:
    try:
        sal_atual = float(input('Digite o valor do seu salario atual: '))
        sal_reaj = reajuste(sal_atual)
        sal_c_reaj = sal_atual + sal_reaj
        print(f'Seu salario sem reajuste é de R${sal_atual:.2f}, mas com reajuste fica R${sal_c_reaj:.2f}')
        break


    except ValueError:
        print('Você não digitou um numero, tente novamente')