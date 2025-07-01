print('Calculando seu pace')

#  Distancia
#  Tempo 
#  pace
#  velocidade media

# # calculo = tempo/distancia

# # Calcular o tempo de acordo com cada pace e mostrar na tela


while True:
    try:
        tempo = float (input('Digite seu tempo na corrida: '))
        km = float(input('Digite a distância: '))
        pace = tempo/km
        print(f'Seu pace é de {pace:.2f} min/Km')
        break
    
    except ValueError:
        print('Voce digitou algo errado, tente novamente')

# melhorar o codigo usando funções