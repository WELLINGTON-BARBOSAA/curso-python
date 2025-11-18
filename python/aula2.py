'''👉
📝Dia 3 – Missão:
Estudar variáveis, tipos de dados e operadores.
Criar um script simples que receba entradas e exiba resultados.'''

print('-' *40)
print('     COLETOR DE DADOS BASICO')
print('-' *40)

nome_completo = input('Digite seu nome completo: ')
idade = int(input('Digite sua idade: '))

print('-' *40)
print(f'O nome do usuario é {nome_completo}, com idade de {idade} anos.')
print('-' *40)

if idade == 30:
    print('Sua idade é linda igual a você <3, volte sempre! ')
else:
    print('Você é feio <3 ')