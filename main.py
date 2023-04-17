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

    barber = Station() #iniciamos al barbero

    barberShop = Gasolinera(barber, asientos=1) #iniciamos la barbería con un asiento
    barberShop.openShop() #abrimos el thread

    while len(customers) > 0:
        c = customers.pop()#Cogemos un cliente y lo eliminamos de la lista
        #New customer enters the barbershop
        barberShop.enterBarberShop(c)#el cliente c entra a la barbería
        customerInterval = random.randrange(customerIntervalMin,customerIntervalMax+1) #generamos un intervalo aleatorio entre los dos valores
        time.sleep(customerInterval) #esperamos el intervalo de tiempo generado

    time.sleep(1) #esperamos un segundo para que el barbero pueda terminar de cortar el pelo
    print ('Todos los clientes de hoy han sido atendidos')
    os._exit(0) #salimos del programa/terminamos ejecución