print('*' *30)
print(  'Bem vindo ao seu cadastro')
print('*' *30)


nome = input('Nome completo: ')
ano_nasc = int(input('Ano de Nascimento: '))
cidade = input('Cidade: ')
altura = input('Digite sua altura: ')
bairro = input('Digite o bairro onde mora: ')
numero_casa = input('Digite o numero da sua casa: ')
ano_atual = 2025

print('=' *50)
print(  'CARREGANDO DADOS')
print('=' *50)

print(f'Seu nome é: {nome}')
print(f'Sua atual idade é: {ano_atual - ano_nasc}')
print(f'Sua cidade atual é: {cidade}')
print(f'Sua altura é: {altura}')
print(f'Bairro onde mora: {bairro}')
print(f'Numero da casa: {numero_casa}')

print('-' *30)
print(  'DADOS ENCERRRADO')
print('-' *30)