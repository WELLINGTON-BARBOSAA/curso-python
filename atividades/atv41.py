# ''' Faça um programa que leia um ano e diga se ele é bissexto'''

from datetime import date
ano = int(input('Qual o ano deseja analisar: Digite 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100!= 0 or ano % 400 == 0:
    print('O ano é BISSEXTO')
else:
    print('O ano NÃO é bissexto')
