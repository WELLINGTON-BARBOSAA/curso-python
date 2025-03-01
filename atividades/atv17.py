# Escreva um programa para ler o número total de eleitores de um município, o
# numero de votos brancos, nulos e válidos. Apresente a porcentagem que cada
# um representa em relação ao total de eleitores. 

eleitores_aptos = int(input('Digite a quantidade de votantes: '))
compareceram = int(input('Digite a quantidade de presentes: '))
votos_brancos = int(input('Digite a quantidade de votos brancos: '))
votos_nulos = int(input('Digite a quantidade de votos nulos: '))

votos_validos =  compareceram - (votos_brancos + votos_nulos)
print(f'A quantidade de votantes nessa eleição é de : {votos_validos}')

porcentagem_votos_brancos = (votos_brancos / compareceram) * 100
porcentagem_votos_nulos = (votos_nulos / compareceram) * 100
porcentagem_votos_validos = (votos_validos / compareceram) * 100 

print(f'A porcentagem de votos brancos é de : {porcentagem_votos_brancos:.2f}%')
print(f'A porcentagem de votos nulos é de : {porcentagem_votos_nulos:.2f}%')
print(f'A porcentagem em votos validos é de: {porcentagem_votos_validos:.2f}%')
