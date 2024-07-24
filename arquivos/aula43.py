' Aula sobre laço de repetição - for'

# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0 

# while senha_salva != senha_digitada:
#         senha_digitada = input(f'Sua senha ({repeticoes}x): ')

#         repeticoes += 1
# print(f'Seu laço teve *{repeticoes}* repetições')
# print('O laço a seguir pode ter repetições infinitas')

nome = 'Bala'
novo_nome = ''
for letra in nome:
    novo_nome += f'/{letra}'
    print(letra)
print(novo_nome)


