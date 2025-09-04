''' Escreva um programa que leia a velocidade de um carro
Se ele ultrapassar 80km/h, mostre a mensagem dizendo que foi multado
A multa vai custar R$ 7,00 por km acima do limite'''

vel_carro = int(input('Digite a velocidade do carro: '))
multa = (vel_carro - 80) * 7
print(f'Sua velocidade é de {vel_carro}Km/hss')
if vel_carro < 80 :
    print('Sua velocidade esta normal')

else:
    print('MULTADO COM SUCESSO')
    print(f'Sua multa é de R$ {multa}')
    
# fazer essa atividade usando funções