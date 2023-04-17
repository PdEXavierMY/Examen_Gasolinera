from threading import Event, Lock
import time, random
from introducir import solicitar_introducir_numero, solicitar_introducir_numero_extremo_superior

mutex = Lock()# para que no se pueda acceder a la barberia mientras se esta cortando el pelo

#variables reutilizables en todo el programa
gasDurationMin = solicitar_introducir_numero("Introduzca el tiempo mínimo para repostar")
#variable que almacena el tiempo mínimo que tardará en repostar
gasDurationMax = solicitar_introducir_numero_extremo_superior("Introduzca el tiempo máximo para respostar", gasDurationMin)
#variable que almacena el tiempo máximo que tardará en repostar
customerIntervalMin = solicitar_introducir_numero("Introduzca el intervalo mínimo entre clientes")
#variable que almacena el intervalo mínimo entre clientes
customerIntervalMax = solicitar_introducir_numero_extremo_superior("Introduzca el intervalo máximo entre clientes", customerIntervalMin)
#variable que almacena el intervalo máximo entre clientes

class Station:
	refillEvent = Event()#EEvento que controla cuando se echa gasolina

	def sleep(self):
		self.refillEvent.wait()#Definimos que si se duerme entonces el evento se para

	def wakeUp(self):
		self.refillEvent.set()#Definimos que si se despierta entonces el evento se activa

	def refill(self, customer):
		self.refillEvent.clear()#Se limpia el evento

		print ('{} está repostando'.format(customer.name))

		randomrefilltime = random.randrange(gasDurationMin, gasDurationMax+1)
		time.sleep(randomrefilltime)
		print ('{} ha terminado de repostar'.format(customer.name))