'''Atividade de Listas'''


''' 🧩 Exercícios Básicos com Listas
1️⃣ Criando e acessando

Crie uma lista chamada frutas com 5 nomes de frutas.
Mostre:

A primeira fruta

A terceira fruta

A última fruta

💡 Dica: lembre que os índices começam em 0.'''

# frutas = ['Abobora', 'Melancia', 'Tomate', 'Azeitona', 'Repolho']
# frutas.append('Batata')
# frutas.pop(0)
# print(f'A primeira fruta é: {frutas[0]}')
# print(f'A segunda fruta é: {frutas[1]}')
# print(f'A ultima fruta é: {frutas[4]}')
# frutas[2] = 'Batata'
# print(frutas)

# usuario=str(input('Digite o nome de uma fruta: ')).capitalize() # Coloca a primeira letra maiscula


# if usuario in frutas:
#     print(f'Sua fruta {usuario} esta na lista')
# else:
#     print(f'Sua fruta {usuario} NÃO esta na lista')
frutas = ['Banana', 'Pepino', 'Manga', 'Caju', 'Mandioca']

for fruta in frutas:
    print(fruta)