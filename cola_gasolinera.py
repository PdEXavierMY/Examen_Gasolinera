from threading import Thread
from gasolinera import gasDurationMax, customerIntervalMin, customerIntervalMax, mutex

class gasolinera:
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
				self.station.refill(c)
			else:
				mutex.release()
				print ('Sin clientes en espera...')
				self.station.sleep()
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
			self.station.wakeUp()#Despertamos al barbero