# Peça ao usuário para digitar 10 números inteiros.
# Use um laço for para percorrer esses números.
# Some apenas os números pares.
# Ao final, exiba a soma dos números pares digitados.

lista = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
soma_pares = 0
for numero in lista:
    if numero % 2 == 0:
        soma_pares += numero
print(f'A soma dos numeros pares é de : {soma_pares}')