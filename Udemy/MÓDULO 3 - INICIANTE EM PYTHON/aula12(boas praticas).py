'''
CONSTANTE = 'Variaveis' imutáveis
muitas condições no mesmo if (ruim)
        <- Contagem de complexidade (ruim) (Mais afastado da margem)
'''
velocidade = 61 # Velocidade atual do carro
km_do_carro = 90 # local em que o carro está na ewstrada

RADAR_1 = 60 # velocidade máxima do radar 1 
KM_1 = 100 #local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

# Em Python se usa letras maiúsculas para dizer a outros programadores que isso é uma constante, pois na linguagem não temos esse conceito

#Saber se a velocidade estava acima
velocidade_carro_passou_radar_1 = velocidade>RADAR_1 #variável com a condição para evitar repetições
multado_no_radar_1 = km_do_carro >= (KM_1 - RADAR_RANGE) and  km_do_carro <= (KM_1 + RADAR_RANGE) #Condição numa variavel para poder substituir no código e deixar ele mais limpo

if velocidade_carro_passou_radar_1 : 
    print('Velocidade carro passou da permitida no radar1 ')

if multado_no_radar_1 and \
    velocidade_carro_passou_radar_1: # \ quebra a linha do código (é tipo o Shift + Enter)
    print('Carro Multado em Radar 1')