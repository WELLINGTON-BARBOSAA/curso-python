'''
CONSTANTE =  "Variáveis" que não vão mudar 
Muitas condições no mesmo if (ruim)
....<- Contagem de complexidade (ruim)
'''
# DICA - Ao escrever o codigo e ele ficar muito extenso como estou escrevendo aqui, basta 
# usar \ para quebrar o codigo e dar 
# Continuidade a escrita do código
velocidade = 62    # velocidade atual do carro
local_carro = 90 # local onde o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1_BR = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

velocidade_passou_radar1 = velocidade > RADAR_1
carro_passou = LOCAL_1_BR >= (RADAR_RANGE - local_carro) and \
    LOCAL_1_BR <= (RADAR_RANGE + local_carro)
carro_multado = carro_passou and velocidade_passou_radar1

if velocidade_passou_radar1:
    print('Carro passou no radar')

if carro_passou:
    print('Carro passou')

if  carro_passou and velocidade_passou_radar1:
    print("Carro multado em radar 1")





















# vel_carro_passou_radar1 = velocidade > RADAR_1
# carro_passou_radar1 = local_carro >= (LOCAL_1_BR - RADAR_RANGE) and \
#    local_carro <= (LOCAL_1_BR + RADAR_RANGE) and \
#       vel_carro_passou_radar1
# carro_multado_radar1 = carro_passou_radar1 and vel_carro_passou_radar1

 
# if vel_carro_passou_radar1:
#    print('Velocidade carro passou radar1')

# if carro_passou_radar1:
#    print('Carro passou radar 1')

# if carro_multado_radar1:
#       print('Carro multado em radar 1')
   


"""DICA -> Quanto mais condições existirem dentro do if (and, or, not)
quanto mais condições, mais complexo fica o código. Pensar um pouco mais para deixar o código Clean 
   DICA -> Código tem que ser limpo"""
