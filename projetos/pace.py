print('Calculando seu pace')

#  Distancia
#  Tempo 
#  pace
#  velocidade media

# # calculo = tempo/distancia

# # Calcular o tempo de acordo com cada pace e mostrar na tela


tempo = input('Insira seu tempo: ')
distancia_km = input('Insira a distância: ')

tempo_conv = int (tempo)
distancia_km_conv = int (distancia_km)

if tempo_conv  is False:
    print('Digite apenas numeros')
    

if distancia_km_conv is False:
    print('Digite apenas numero')


calculo_pace = tempo_conv/distancia_km_conv
velocidade_media = distancia_km_conv/tempo_conv

print(f'Seu pace é de : {calculo_pace} m/Km')
print(f'E sua velocidade média é de: {velocidade_media:.2f} Km/m')



# if tempo_conv.isinstance(tempo_conv, int, float) is False:
#     print('Digite apenas numeros')
    

# if  distancia_km_conv is False:
#     print ('Digite apenas numero')

