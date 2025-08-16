'''Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um separado'''

num = input("Digite um número entre 0 e 9999: ").zfill(4)  # preenche com zeros à esquerda se faltar

print(f'Unidade: {num[3]}')
print(f'Dezena: {num[2]} ')
print(f'Centena: {num[1]}')
print(f'Milhar: {num[0]}')