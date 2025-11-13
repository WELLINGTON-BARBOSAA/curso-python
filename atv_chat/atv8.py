'''💻 Desafio: Catálogo de Produtos

Crie um programa que:
1️⃣ Comece com uma lista vazia chamada catalogo.
2️⃣ Dentro de um loop while, o programa deve pedir ao usuário:

NOME DO PRODUTO
PREÇO
QUANTIDADE NO ESTOQUE

3️⃣ Guarde essas informações em um dicionário, com as chaves:

'nome', 'preco', 'quantidade'

4️⃣ Adicione esse dicionário à lista catalogo.
5️⃣ Pergunte se o usuário quer cadastrar outro produto.

Se responder “s”, continua.

Se responder “n”, o programa para.'''

catalogo = []
soma = 0
maior_preco = 0
nome_mais_caro = ''

while True:
    nome_produto = input('Digite o nome do produto: ')
    preço = float(input('Preço do produto: '))
    quant_estoque = int(input('Quantidade no estoque: '))

    dados_produtos = {
        'nome': nome_produto,
        'preco': preço,
        'quantidade': quant_estoque
    }

    catalogo.append(dados_produtos)
    
    soma += preço * quant_estoque
        
    parar = input('Quer cadastrar outro produto: ').lower().startswith('n')
    if parar == True:
        break

for produto in catalogo:
    print(f"Nome do produto: {produto['nome']} | Valor R$ {produto['preco']:.2f} | Quantidade: {produto['quantidade']}")

print('------- CONFERINDO O NOME E PREÇO MAIS CARO -------')
print('------- CARREGANDO -------')

for i in catalogo:
    if i['preco'] > maior_preco:
        maior_preco = i['preco']
        nome_mais_caro = i['nome']
print(f'O nome do produto mais caro é {nome_mais_caro} ')
print(f'O maior preço é: {maior_preco:.2f}  ')

print('--------- CARREGANDO A SOMA DE TODOS OS PRODUTOS -------------')

print(f'A soma de todos os  produtos é de R${soma:.2f}')


