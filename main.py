import time, random
import os
from gasolinera import Station, customerIntervalMin, customerIntervalMax
from cola_gasolinera import Gasolinera
from cliente import Customer
from introducir import solicitar_introducir_numero, solicitar_introducir_palabra


if __name__ == '__main__':
    nclientes = solicitar_introducir_numero("Introduzca el número de clientes que desea introducir")
    #variable que almacena el número de clientes que se van a introducir

    customers = [] #lista de clientes
    for i in range(nclientes): #bucle que introduce los clientes en la lista
        customers.append(Customer('{}'.format(solicitar_introducir_palabra("Introduzca el nombre del cliente"))))

    gas = Station() #iniciamos la gasolinera

    gasS = Gasolinera(gas, asientos=1)
    gasS.openStation() #abrimos el thread

    while len(customers) > 0:
        c = customers.pop()#Cogemos un cliente y lo eliminamos de la lista
        #New customer enters the barbershop
        gasS.enterGasStation(c)#el cliente c entra
        customerInterval = random.randrange(customerIntervalMin,customerIntervalMax+1) #generamos un intervalo aleatorio entre los dos valores
        time.sleep(customerInterval) #esperamos el intervalo de tiempo generado

    time.sleep(1)
    print ('Todos los clientes de hoy han sido atendidos')
    os._exit(0)