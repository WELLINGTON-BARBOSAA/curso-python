''' Um professor quer sortear um dos seus quatro alunos 
para apagar o quadro. Faça um programa que ajude ele, 
lendo o nome deles e escrevendo o nome do ganhador '''


import random

aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]

sorteado = random.choice(lista)
print(f'O nome ganhador do sorteio foi:  {sorteado}')