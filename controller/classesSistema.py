#!/usr/bin/python
# -*- coding: utf-8 -*-
from wiringx86 import GPIOGalileoGen2 as GPIO

gpio = GPIO(debug=False)



class Home(object):

	'''App para controlar os dispositivos cadastrados em uma residencia automatizada'''

	def __init__(self):
		self.comodo = {}

	def setComodo(self):
		pass

	def getComodo(self):
		pass

	def alterar_comodo(self):
		pass

	def excluir_comodo(self):
		pass

class Comodo(object):

	def __init__(self):
		self.dispositivos={}

	def getDevices(self):
		pass

	def setDevices(self):
		pass
	def deleteDevices(self):
		pass

class Device(object):

	def __init__(self):
		self.name = ''
		self.id = 0
		self.state = False

	def OnDevice(self, comodo):
		return gpio.digitalWrite(comodo, gpio.HIGH)


	def offDevice(self, comodo):
		return gpio.digitalWrite(comodo, gpio.LOW)