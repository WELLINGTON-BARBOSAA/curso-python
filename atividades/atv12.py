# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa. 


# lista_inversa = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in lista_inversa:
#     print(i)

# Solicita ao usuário que insira 10 números reais
numeros = []
for i in range(10):
    num = float(input(f'Digite o {i+1}º número: '))
    numeros.append(num)

# Exibe os números na ordem inversa
print('\nNúmeros na ordem inversa:')
for num in reversed(numeros):
    print(num)
