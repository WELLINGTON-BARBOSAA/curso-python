'''Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e 
continue pedindo até que o usuário informe um valor válido. '''

while True:

    numero = int(input('Digite uma nota: '))

    if numero > 10: 
        print('Nota invalida, tente novamente')
        continue
    else :
        print(f'Válida, sua nota foi: {numero}')
        break
