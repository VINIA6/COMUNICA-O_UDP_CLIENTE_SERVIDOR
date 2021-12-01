import random 
import numpy as np 


class sensor(): 
    '''def tempertura(cont_tempo, valor_inicial):

        h = 10
        l=15

        if cont_tempo == h:
            semente = random.randint(0,15)
            
            if semente==1 or 9 or 14: 
                valor_inicial = valor_inicial + 0.5
            h=h+10    
        if cont_tempo == l:
            semente = random.randint(0,15)
            
            if  semente==2 or 7 or 15:
                valor_inicial = valor_inicial - 0.5
            l=l+15
        return float(np.round(valor_inicial,2))'''
    def tempertura(valor_inicial):
        return valor_inicial

    def humidade(cont_tempo, valor_inicial):

        h = 10
        l=15

        if cont_tempo == h:
            semente = random.randint(0,15)
            
            if semente==1 or 9 or 14: 
                valor_inicial = valor_inicial + 0.4
            h=h+10    
        if cont_tempo == l:
            semente = random.randint(0,15)
            
            if  semente==2 or 7 or 15:
                valor_inicial = valor_inicial - 0.4
            l=l+15

        return float(np.round(valor_inicial,2))

    def co2(cont_tempo,valor_inicial):
        #SERÁ EM PORCENTAGEM DEVE TER UMA MARGEM CONSTANTE
        # 0 A 100 

        h = 10
        l=15

        if cont_tempo == h:
            semente = random.randint(0,15)
            
            if semente==1 or 9 or 14: 
                valor_inicial = valor_inicial + 0.3
            h=h+10    
        if cont_tempo == l:
            semente = random.randint(0,15)
            
            if  semente==2 or 7 or 15 :
                valor_inicial = valor_inicial - 0.3
            l=l+15

        return float(np.round(valor_inicial,2))


class atuador():
    def Aquecedor(temperatura):
        temperatura = temperatura + 1.83
        return temperatura
    def Resfriador(temperatura):
        temperatura = temperatura - 20.0
        return temperatura
    def Sistema_Irrig(humidade):
        humidade = humidade + 1.03
        return humidade
    def Injetor_Co2(gas):
        gas = gas + 1
        return gas 

