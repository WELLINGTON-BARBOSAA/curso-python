'''🔹 Exercício 9 – Contagem com while '''

# contador = 1
# user = int(input('Digite um numero: '))

# while contador <= user:
#     print(contador)
#     contador = contador +1


# Peça um número ao usuário.

# Use um while para contar de 1 até esse número.

#Exemplo:
#Entrada → 5
#Saída → 1 2 3 4 5 '''



'''🔹 Exercício 10 – Cadastro simples

Crie uma lista vazia.
Dentro de um while, peça nome, idade e cidade de uma pessoa.
Guarde esses dados em um dicionário.
Adicione esse dicionário na lista.
Pergunte se o usuário quer continuar cadastrando.
Ao final, mostre todos os cadastros.'''

cadastro = []

while True:
    nome = input('Digite seu nome completo: ')
    cidade = input('Digite sua cidade: ')
    idade = int(input('Qual sua idade: '))

    dados_usuario = {
        'Nome': nome,
        'Cidade': cidade,
        'idade': idade
    }

    cadastro.append(dados_usuario)

    sair = input('Deseja sair: ').startswith('s')
    if sair == True:
        break


for c in cadastro:
    print(f'{c}')