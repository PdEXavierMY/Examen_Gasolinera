from threading import Event, Lock
import time, random
from introducir import solicitar_introducir_numero, solicitar_introducir_numero_extremo_superior

mutex = Lock()# para que no se pueda acceder a la barberia mientras se esta cortando el pelo

#variables reutilizables en todo el programa
haircutDurationMin = solicitar_introducir_numero("Introduzca el tiempo mínimo de corte de pelo")
#variable que almacena el tiempo mínimo que tardará en cortar el pelo
haircutDurationMax = solicitar_introducir_numero_extremo_superior("Introduzca el tiempo máximo de corte de pelo", haircutDurationMin)
#variable que almacena el tiempo máximo que tardará en cortar el pelo
customerIntervalMin = solicitar_introducir_numero("Introduzca el intervalo mínimo entre clientes")
#variable que almacena el intervalo mínimo entre clientes
customerIntervalMax = solicitar_introducir_numero_extremo_superior("Introduzca el intervalo máximo entre clientes", customerIntervalMin)
#variable que almacena el intervalo máximo entre clientes

class Barber:
	barberWorkingEvent = Event()#El barbero se crea un evento que es cuando está trabajando

	def sleep(self):
		self.barberWorkingEvent.wait()#Definimos que si se duerme entonces el evento se para

	def wakeUp(self):
		self.barberWorkingEvent.set()#Definimos que si se despierta entonces el evento se activa

	def cutHair(self, customer):
		#Definiendo que el barbero está trabajando
		self.barberWorkingEvent.clear()#Se limpia el evento

		print ('A {} le están cortando el pelo'.format(customer.name))

		randomHairCuttingTime = random.randrange(haircutDurationMin, haircutDurationMax+1)
		time.sleep(randomHairCuttingTime)#ponemos un tiempo aleatorio que tardará en cortar el pelo
		print ('{} ha terminado'.format(customer.name))