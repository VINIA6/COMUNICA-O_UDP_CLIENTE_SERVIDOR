import random 
import numpy as np 
import time

def sensor_tempertura(cont_tempo):

    valor_inicial = 38.1
    h = 10
    l=15

    if cont_tempo == h:
        semente = random.randint(0,15)
        print('Semente',semente)
        if semente==1 or 9 or 14: 
            valor_inicial = valor_inicial + 0.5
        h=h+10    
    if cont_tempo == l:
        semente = random.randint(0,15)
        print('Semente',semente)
        if  semente==2 or 7 or 15:
            valor_inicial = valor_inicial - 0.5
        l=l+15
    return float(np.round(valor_inicial,2))
    
def sensor_humidade_terra(cont_tempo):
    
    valor_inicial = 50
    
    h = 10
    l=15
    
    if cont_tempo == h:
        semente = random.randint(0,15)
        print('Semente',semente)
        if semente==1 or 9 or 10 or  14 or 3 or 5: 
            valor_inicial = valor_inicial + 1
        h=h+10    
    if cont_tempo == l:
        semente = random.randint(0,15)
        print('Semente',semente)
        if  semente==2 or 7 or 15 or 4 or 12 :
            valor_inicial = valor_inicial - 1
        l=l+15

    return float(np.round(valor_inicial,2))
   

def nivel_co2(cont_tempo):
    #SERÁ EM PORCENTAGEM DEVE TER UMA MARGEM CONSTANTE
    # 0 A 100 

    valor_inicial = 60
    
    h = 10
    l=15
    
    if cont_tempo == h:
        semente = random.randint(0,15)
        print('Semente',semente)
        if semente==1 or 9 or 10 or  14 or 3 or 5: 
            valor_inicial = valor_inicial + 0.3
        h=h+10    
    if cont_tempo == l:
        semente = random.randint(0,15)
        print('Semente',semente)
        if  semente==2 or 7 or 15 or 4 or 12 :
            valor_inicial = valor_inicial - 0.3
        l=l+15

    return float(np.round(valor_inicial,2))


'''cont_tempo = 0 
while True :
    time.sleep(1)
    print('-'*25)
    print('Co2: ', nivel_co2(cont_tempo))
    print('Temperatura ºC: ',sensor_tempertura(cont_tempo))
    cont_tempo = cont_tempo + 1'''