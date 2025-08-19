'''Crie um programa que leia o nome de uma
cidade e diga se ela tem o nome santo ou não'''

cid_nasc = str(input('Digit a cidade de nascimento: ')).strip()
print(cid_nasc[:5].upper() == 'SANTO')
