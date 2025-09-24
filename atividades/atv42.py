'''Faça um programa que leia três numeros
e mostre qual é o maior e qual é o menor '''

try:

    a = int(input('Digite o primeiro numero: '))
    b = int(input('Digite o segundo numero: '))
    c = int(input('Digite o terceiro numero: '))

except ValueError:
    print('Voce não digitou um numero')
    
menor = min(a,b,c)
print(f'O menor numero é {menor}')

maior = max(a,b,c)
print(f'O maior numero digita é {maior}: ')

# O que é a função min()?
# É uma função embutida (built-in) do Python, ou seja, 
# já vem pronta na linguagem, não precisa importar nada.
# O papel dela é retornar o menor valor entre dois ou mais elementos passados como argumentos.