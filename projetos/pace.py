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

# tempo = float(input('Insira seu tempo: '))
# distancia_km = float(input('Insira a distância: '))

# calculo_pace = tempo/distancia_km

# tempo_em_horas = tempo/60
# velocidade_media = distancia_km/tempo_em_horas

# print(f'Seu pace é de : {calculo_pace:.2f} min/Km')
# print(f'E sua velocidade média é de: {velocidade_media:.2f} Km/h')

    