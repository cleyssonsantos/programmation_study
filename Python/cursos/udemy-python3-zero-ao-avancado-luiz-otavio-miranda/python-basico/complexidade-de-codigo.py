"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    < - Contagem de complexidade (ruim)
"""
velocidade = 61 # velocidade atual do carro
local_carro = 101 # local em que o carro está na estrada

# Contantes, coisas que não vão mudar no código
RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

carro_ultrapassou_velocidade_permitida_do_radar_1 = velocidade > RADAR_1
carro_esta_no_local_do_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
local_carro <= (LOCAL_1 + RADAR_RANGE)

carro_foi_multado_no_radar_1 = carro_esta_no_local_do_radar_1 and carro_ultrapassou_velocidade_permitida_do_radar_1


if carro_foi_multado_no_radar_1:
    print("Carro multado em RADAR_1.")
