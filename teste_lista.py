
lista2 = [21,22,23,24,25,26,27,28,29, 5050,30,31,32,33,34,35,36,37,38]

antigo = 0 
novo = 0 


for i in range(0,len(lista2)):
    
    x=novo
    novo=lista2[i]
    antigo=x
    if novo == 5050:
        print(antigo)
        print(novo)
