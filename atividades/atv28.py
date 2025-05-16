'Faça um algoritmo que leia um preço e mostre'
'seu novo preço, com desconto de 5%'

preco = float(input('Digite o valor do preço: '))
des = preco * 15/100
resul_des = preco - des
print(f'O preço original é de {preco}, mas com os desconto de 5% vai fica {resul_des:.2f}')
