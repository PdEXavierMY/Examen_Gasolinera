from threading import Thread
from barbero import haircutDurationMin, customerIntervalMin, customerIntervalMax, mutex

class BarberShop:
	waitingCustomers = [] #lista de clientes que están esperando

	def __init__(self, barber, asientos):
		self.barber = barber
		self.asientos = asientos
		print ('BarberShop iniciado con {} sitios'.format(asientos))
		print ('Mínimo intervalo de Clientes = {}'.format(customerIntervalMin))
		print ('Máximo intervalo de Clientes = {}'.format(customerIntervalMax))
		print ('Tiempo mínimo de corte de pelo = {}'.format(haircutDurationMin))
		print ('Tiempo máximo de corte de pelo = {}'.format(customerIntervalMax))
		print ('---------------------------------------')

	def openShop(self):
		print ('La barbería se está abriendo')
		workingThread = Thread(target = self.barberGoToWork)#declaramos un hilo para que el barbero trabaje
		workingThread.start()#iniciamos el hilo del barbero

	def barberGoToWork(self):
		while True:
			mutex.acquire()#bloqueamos hasta que suceda el release

			if len(self.waitingCustomers) > 0:
				c = self.waitingCustomers[0]#cogemos al primer cliente y lo eliminamos de la lista
				del self.waitingCustomers[0]
				mutex.release()
				self.barber.cutHair(c)#hacemos que el barbero le corte el pelo al cliente escogido
			else:
				mutex.release()
				print ('Sin clientes en espera, tomando un descanso...')
				self.barber.sleep()
				print ('El barbero se ha despertado')

	def enterBarberShop(self, customer):
		mutex.acquire() #bloqueamos hasta que suceda el release
		print ('>>>>> {} entró en la tienda y está buscando un sitio'.format(customer.name))

		if len(self.waitingCustomers) == self.asientos: #si la sala de espera está llena
			print ('La sala de espera está llena, {} se va a marchar.'.format(customer.name))
			mutex.release()
		else:
			print ('{} se ha sentado en la sala de espera'.format(customer.name))
			self.waitingCustomers.append(customer) #añadimos al cliente a la lista de clientes en espera
			mutex.release()
			self.barber.wakeUp()#Despertamos al barbero