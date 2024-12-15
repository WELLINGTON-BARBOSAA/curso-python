print('Calculando seu pace')

#  Distancia
#  Tempo 
#  pace
#  velocidade media

# # calculo = tempo/distancia

# # Calcular o tempo de acordo com cada pace e mostrar na tela


tempo = input('Insira seu tempo: ')
distancia_km = input('Insira a distância: ')

tempo_conv = float (tempo)
distancia_km_conv = float (distancia_km)

calculo_pace = tempo_conv/distancia_km_conv

tempo_em_horas = tempo_conv / 60
velocidade_media = distancia_km_conv/tempo_em_horas

print(f'Seu pace é de : {calculo_pace:.2f} min/Km')
print(f'E sua velocidade média é de: {velocidade_media:.2f} Km/h')



# if tempo_conv.isinstance(tempo_conv, int, float) is False:
#     print('Digite apenas numeros')
    

# if  distancia_km_conv is False:
#     print ('Digite apenas numero')

