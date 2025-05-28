'Crie um programa que leia um numero real qualquer '
'pelo teclado e mostra na tela sua porçao inteira'

from math import ceil # esse modo seleciona o metodo a qual o programa todo vai ser usado
import math # Nesse ele inclui todos os metodos da biblioteca dentro do programa

numero = float(input('Digite um numero: '))
inteiro = (numero) 
print(f'Seu numero digitado foi {numero}, ele com porção inteira é de {inteiro}')

#ceil = para mais, flor = para menos e trunc = parte inteira