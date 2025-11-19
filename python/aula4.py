
# contando = [1,2,3,4,5,6,7,8,9,10]
# for n in contando:
#     print(n)

# for n in range(1,11): # código mais limpo e profissional
#     print(n)


'''2️⃣ Sistema de login simples
repetir a pergunta por usuário e senha
só parar quando a senha correta for digitada'''
# Arrumar o código pedindo para digitar somenta a senha e ter somente 3 
# tentativas

# while True:

#     nome = input('Digite seu nome completo: ')
#     usuario = input('Digite seu usuario: ')
#     senha = input('Digite sua senha (somente numeros): ')
#     senha_permitida = '123456789'

#     if senha_permitida == senha:
#         print(f'Acesso permitido, {nome}.')
#         break
#     else:
#         print('Acesso negado')


'''3️⃣ Soma de vários números
usar um loop
pedir números até o usuário digitar 0
ao final, mostrar a soma total'''


# soma = 0 

# print('-'*15)
# print(  'BEM VINDO AO SEU CONTADOR')
# print('-'*15)

# while True:

#     usuario = int(input('Digite um numero para somar: '))

#     if usuario == 0:
#         break

#     soma += usuario

# print(f'O resultado da soma é {soma}')


'''Peça ao usuário um número inteiro.
Depois, mostre a tabuada desse número de 1 a 10, uma linha para cada multiplicação.

Exemplo de formato (apenas o formato, não o resultado):'''

print('*' *30)
print(  '   TABUADA')
print('*' *30)

usuario = int(input('Digite um numero para tabuada: '))

for n in range (1, 11):
    print(n*usuario)

# print(f'{numero}x1: {numero*1}')
# print(f'{numero}x2: {numero*2}')
# print(f'{numero}x3: {numero*3}')
# print(f'{numero}x4: {numero*4}')
# print(f'{numero}x5: {numero*5}')
# print(f'{numero}x6: {numero*6}')
# print(f'{numero}x7: {numero*7}')
# print(f'{numero}x8: {numero*8}')
# print(f'{numero}x9: {numero*9}')
# print(f'{numero}x10: {numero*10}')
    