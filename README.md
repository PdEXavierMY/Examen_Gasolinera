# Examen_Gasolinera

[Este](https://github.com/Xavitheforce/Examen_Gasolinera) es el enlace a mi repositorio.

El ejercicio requerido es el siguiente:

""" El objetivo de la práctica es simular una gasolinera bajo las siguientes premisas.
- A la gasolinera llegan coches a un intervalo aleatorio de hasta T minutos.
- La gasolinera consta de N surtidores de combustible.
- Cuando un coche se pone en la surtidor de combustible, el conductor se baja,
elije el combustible de su elección y llena el depósito. Este trabajo le lleva un
tiempo de entre 5 y 10 minutos.
- Tras llenar el depósito se acerca a la oficina de pago y se pone a la cola de la
caja. Suponga que la caja es única.
- En pagar tarda 3 minutos.
- Tras terminar el pago retira el coche, dejando el surtidor libre para el siguiente
coche.

Realización
Se pide:
- Modelar el problema con los objetos apropiado indicando los estados en que
puede estar cada elemento.
- Se modelarán los coches como Threads que genera el programa principal. A
efectos del ejercicio se generan 50 coches.
- Realizar el problema para un tiempo T de 15 minutos y N de un surtidor de
combustible.
- Calcular el tiempo medio que tarda un coche desde que llega a la gasolinera
hasta que sale de ella.
- A efectos del problema los minutos se tratarán en el programa con centésimas
de segundo. """

El código empleado para resolverlo es el siguiente:

Cliente:
```py
class Customer:
	def __init__(self, name):
		self.name = name
```


Gasolinera:
```py
from threading import Event, Lock
import time, random

mutex = Lock()# para que no se pueda acceder a la barberia mientras se esta cortando el pelo

#variables reutilizables en todo el programa
gasDurationMin = 5
#variable que almacena el tiempo mínimo que tardará en repostar
gasDurationMax = 10
#variable que almacena el tiempo máximo que tardará en repostar
customerIntervalMin = 8
#variable que almacena el intervalo mínimo entre clientes
customerIntervalMax = 13
#variable que almacena el intervalo máximo entre clientes

class Station:
	refillEvent = Event()#EEvento que controla cuando se echa gasolina
	tiempomedio = []#Lista que almacena los tiempos de espera de los clientes

	def sleep(self):
		self.refillEvent.wait()#Definimos que si se duerme entonces el evento se para

	def wakeUp(self):
		self.refillEvent.set()#Definimos que si se despierta entonces el evento se activa

	def refill(self, customer):
		self.refillEvent.clear()#Se limpia el evento

		print ('{} está repostando'.format(customer.name))

		randomrefilltime = random.randrange(gasDurationMin, gasDurationMax+1)
		time.sleep(randomrefilltime)
		print ('{} ha terminado de repostar tras {} minutos'.format(customer.name, randomrefilltime))
		print ('{} va a pagar'.format(customer.name))
		time.sleep(3)
		print ('{} ha pagado'.format(customer.name))
		self.tiempomedio.append(randomrefilltime+3)
```

Cola:
```py
from threading import Thread
from gasolinera import gasDurationMax, customerIntervalMin, customerIntervalMax, mutex

class Gasolinera:
	waitingCustomers = [] #lista de clientes

	def __init__(self, gasolinera, asientos):
		self.gasolinera = gasolinera
		self.asientos = asientos
		print ('Gasolinera iniciada con {} sitios'.format(asientos))
		print ('Mínimo intervalo de Clientes = {}'.format(customerIntervalMin))
		print ('Máximo intervalo de Clientes = {}'.format(customerIntervalMax))
		print ('Tiempo mínimo para repostar = {}'.format(gasDurationMax))
		print ('Tiempo máximo para repostar = {}'.format(customerIntervalMax))
		print ('---------------------------------------')

	def openStation(self):
		print ('La gasolinera se está abriendo')
		workingThread = Thread(target = self.customerRefilling)
		workingThread.start()

	def customerRefilling(self):
		while True:
			mutex.acquire()#bloqueamos hasta que suceda el release

			if len(self.waitingCustomers) > 0:
				c = self.waitingCustomers[0]#cogemos al primer cliente y lo eliminamos de la lista
				del self.waitingCustomers[0]
				mutex.release()
				self.gasolinera.refill(c)
			else:
				mutex.release()
				print ('Sin clientes en espera...')
				self.gasolinera.sleep()
				print ('Procediendo a repostar...')

	def enterGasStation(self, customer):
		mutex.acquire() #bloqueamos hasta que suceda el release
		print ('>>>>> {} llegó a la gasolinera y está buscando un sitio'.format(customer.name))

		if len(self.waitingCustomers) == self.asientos: #si la sala de espera está llena
			print ('No hay sitios, {} se marcha.'.format(customer.name))
			mutex.release()
		else:
			print ('{} va a esperar'.format(customer.name))
			self.waitingCustomers.append(customer) #añadimos al cliente a la lista de clientes en espera
			mutex.release()
			self.gasolinera.wakeUp()
```

Main:
```py
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
```
