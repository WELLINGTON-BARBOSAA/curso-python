'''Faça um programa que calcule a soma entre
todos os numeros impares e que são multiplos
 de tres e que se encontram no intervalo de 1 até 500'''

acumulador = 0
soma_primo = 0 


for c in range(1,501,2):
    if c % 3 == 0:
        soma_primo = soma_primo + c
        acumulador = acumulador + 1 

print(f'Foi encontrado o total de {acumulador} números e o valor total desses acumuladores é de {soma_primo}')
