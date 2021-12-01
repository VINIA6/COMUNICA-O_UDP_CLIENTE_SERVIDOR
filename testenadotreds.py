'''import threading    
import time
from sensores import sensor
from sensores import atuador


cont = 0
menu = 1 

while True:
  temper = sensor.tempertura(cont,temp)
    temp = 38
    if menu == 1:
       t = threading.Thread(target = atuador.Aquecedor(temp)).start()
       time.sleep(2)
        
    
    print(t)
    cont+=1
'''
from multiprocessing.pool import ThreadPool
import time

pool = ThreadPool(processes=4)

def teste_thread():
  for k in range(100000000):

    pass
    #time.sleep()
  return k

def exec():
    print('Inicio')
    async_call = pool.apply_async(teste_thread)
    async_call1 = pool.apply_async(teste_thread)
    async_call2 = pool.apply_async(teste_thread)
    print('Processando....')
    print(async_call.get() + async_call1.get() + async_call2.get())
    return (async_call.get() + async_call1.get() + async_call2.get())

if __name__ == '__main__':
    print(exec()+1)