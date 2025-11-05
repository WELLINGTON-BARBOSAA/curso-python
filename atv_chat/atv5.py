# Nível Intermediário

'''1 Exercício 4 – Fatiamento de string: Peça o nome completo do usuário e mostre: as 3 primeiras
# letras, as 3 últimas letras e o nome em maiúsculo.'''

# usuario = str(input('Digite seu nome: '))
# print('As três primeiras letras do seu nome é: ', usuario[:3])
# print('A três ultimas do seu nome é: ', usuario[-3:])
# print('Seu nome em maiusculo fica assim: ', usuario.upper())

'''2 Exercício 5 – Lista e condições: Dada a lista [5, 8, 12, 15, 21, 30], imprima apenas os números
maiores que 10.'''

# lista = [5, 8, 12, 15, 21, 30]
# for i in lista:
#     if i > 10:
#         print('Os numeros maiores que 10 são: ', i)

'''3 Exercício 6 – Função matemática: Crie uma função quadrado_par que receba uma lista de
números e retorne apenas os quadrados dos pares.'''

# def quadrado_par(lista):
#     resultado = []
#     for num in lista:
#         if num % 2 == 0:        # verifica se é par
#             resultado.append(num ** 2)
#     return resultado

# print(quadrado_par([1, 2, 3, 4, 5]))


'''4 Exercício 7 – Dicionário: Crie um dicionário para representar uma pessoa com nome, idade e
cidade. Peça esses dados ao usuário e depois imprima'''

dados_pessoas = {
    'Nome': input('Digite seu nome: '),
    'Cidade': input ('Digite sua cidade: '),
    'Idade': int(input('Digite sua idade: '))
}

print(f'Seu nome é {dados_pessoas['Nome']}')
print(f'Sua cidade é {dados_pessoas["Cidade"]}')
print(f'Sua idade é {dados_pessoas["Idade"]} anos')