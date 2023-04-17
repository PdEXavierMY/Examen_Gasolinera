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