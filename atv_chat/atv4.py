''' Nível Básico
1 Exercício 1 – Função com argumento padrão: Crie uma função cumprimento que receba um
nome (padrão 'amigo') e mostre: Olá, !'''

def cumprimento(nome):
    return (f'Olá, {nome}')

print(cumprimento('Wellington'))
print(cumprimento('Raimunda'))
print(cumprimento('João'))
print(cumprimento('Maria'))
print(cumprimento('Jose'))



'''2 Exercício 2 – Divisão normal e inteira: 
Peça dois números ao usuário e mostre a divisão normal
(/), divisão inteira (//) e resto (%).'''

numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero: '))
print(numero1/numero2)
print(numero1//numero2)
print(numero1%numero2)


'''3 Exercício 3 – Estrutura de repetição: Mostre todos os números de 1 a 20, mas apenas os
pares.'''


for i in range(1, 21):
    if i % 2 == 0:
        print(i)