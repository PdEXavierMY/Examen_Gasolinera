import time, random
import os
from gasolinera import Station, customerIntervalMin, customerIntervalMax
from cola_gasolinera import Gasolinera
from cliente import Customer
import statistics as stats
from introducir import solicitar_introducir_numero


if __name__ == '__main__':
    tiempoT = solicitar_introducir_numero("Introduzca el tiempo que estará abierta la gasolinera")
    now = time.time() #tiempo actual

    customers = [] #lista de clientes
    idcliente = 1
    for i in range(50): #bucle que introduce los clientes en la lista
        customers.append(Customer('{}'.format(idcliente)))
        idcliente += 1

    gas = Station() #iniciamos la gasolinera

    gasS = Gasolinera(gas, asientos=1)
    gasS.openStation() #abrimos el thread

    while (time.time()-now) < tiempoT:
        c = customers.pop()#Cogemos un cliente y lo eliminamos de la lista
        #New customer enters the barbershop
        gasS.enterGasStation(c)#el cliente c entra
        customerInterval = random.randrange(customerIntervalMin,customerIntervalMax+1) #generamos un intervalo aleatorio entre los dos valores
        time.sleep(customerInterval) #esperamos el intervalo de tiempo generado

    time.sleep(1)
    print ('El tiempo ha terminado, la gasolinera cierra.')
    print('El tiempo medio que tarda un coche desde que llega a la gasolinera hasta que sale de ella es de: {} minutos'.format(stats.mean(gas.tiempomedio)))
    os._exit(0)






    '''El objetivo de la práctica es simular una gasolinera bajo las siguientes premisas.
 A la gasolinera llegan coches a un intervalo aleatorio de hasta T minutos.
 La gasolinera consta de N surtidores de combustible.
 Cuando un coche se pone en la surtidor de combustible, el conductor se baja,
elije el combustible de su elección y llena el depósito. Este trabajo le lleva un
tiempo de entre 5 y 10 minutos.
 Tras llenar el depósito se acerca a la oficina de pago y se pone a la cola de la
caja. Suponga que la caja es única.
 En pagar tarda 3 minutos.
 Tras terminar el pago retira el coche, dejando el surtidor libre para el siguiente
coche.
Realización
Se pide:
 Modelar el problema con los objetos apropiado indicando los estados en que
puede estar cada elemento.
 Se modelarán los coches como Threads que genera el programa principal. A
efectos del ejercicio se generan 50 coches.
 Realizar el problema para un tiempo T de 15 minutos y N de un surtidor de
combustible.
 Calcular el tiempo medio que tarda un coche desde que llega a la gasolinera
hasta que sale de ella.
 A efectos del problema los minutos se tratarán en el programa con centésimas
de segundo.'''