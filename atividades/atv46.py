'''A Confederação Nacional de natação precisa de programa que leia
o ano de nascimento de um atleta e mostra a categoria, de acordo com idade

Até 9 anos - MIRIM 
Até 14 anos - INFANTIL
Até 19 anos - JUNIOR
Até 25 anos - SÊNIOR
Acima de 25 anos - MASTER'''

ANO_ATUAL = 2026

ano_nascimento = int(input('Digite o ano de nascimento: '))
idade = ANO_ATUAL - ano_nascimento
print(f'Sua idade é {idade} anos')

if idade <= 9:
    print('Você é considerado MIRIM')

elif idade <=14:
    print('Você é considerado INFANTIL  ')

elif idade <= 19:
    print('Você é considerado JUNIOR')

elif idade <= 25:
    print('Você é considerado SÊNIOR')

else:
    print('Você é considerado um veterano')