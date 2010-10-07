#!/usr/bin/env python
#--coding: utf-8 --

import math
import numpy

class ModosNormales():
	""" Simula los modos normales de una cuerda/resorte/etc """
	def __init__(self,modos=None,izqFijo=True,derFijo=True,resolucion=60):
		""" modos es una lista de duplas con la amplitud de la componente
		coseno y seno de cada modo.
		izqFijo y derFijo determinan si los bordes son libres o fijos
		resolucion es la cantidad de puntos de la cuerda que se calculan """
		self.izqFijo = izqFijo
		self.derFijo = derFijo
		self.modos = modos or []
		self.resolucion = resolucion
		self.posicion = numpy.zeros((resolucion))
		# Cada modo tiene un componente espacial cuya fase inicial la determina
		# la condición de borde izquierdo.
		# Si los dos bordes son iguales, la forma del primer modo cubre pi
		# De lo contrario, cubre pi/2
		# Cada modo adicional recorre medio ciclo más (pi)
		# Ángulo recorrido por el primer modo
		self.k = math.pi
		if izqFijo ^ derFijo:
			self.k -= math.pi/2

	def calcular(self,T):
		""" Calcula la posición de cada punto a tiempo t """
		#print "Calculando para",T
		# Inicio la posición de la cuerda.
		# Voy a ir sumándole cada modo
		self.posicion = numpy.zeros((self.resolucion))
		for (n,amplitudes) in enumerate(self.modos):
			# Calculo la forma del modo
			fase_inicial = [0,math.pi/2][self.izqFijo]
			fase_final = fase_inicial + self.k + n*math.pi
			# A es la amplitud correspondiente a este modo e instante
			a = amplitudes[0]*math.cos(2.0*math.pi*T*2**n) + \
				amplitudes[1]*math.sin(2.0*math.pi*T*2**n)
			fases = numpy.linspace(fase_inicial,fase_final,self.resolucion)
			self.posicion += a*numpy.cos(fases)

	def mostrar(self):
		""" Escribe la forma de la cuerda a la consola """
		from os import sys
		# No conviene tener límites que cambian, queda muy feo
		#m = min(self.posicion)
		#M = max(self.posicion)
		m = -1.0
		M = 1.0
		yres = 12
		paso = (M-m)/yres
		for n in xrange(yres):
			y = M - n*paso
			#print y
			for i in xrange(self.resolucion):
				sys.stdout.write([' ','-'][abs(self.posicion[i]-y) < paso/2.0])
			print
			
		print

if __name__ == "__main__":
	modos = [(1.5*math.cos(0.5*i*math.pi/2.0)/(i)**2,0) for i in xrange(1,8)]
	print modos
	a = ModosNormales(modos)
	t = 0.0
	paso = 0.01
	while 1:
		print t
		a.calcular(t)
		a.mostrar()
		t += paso
		if raw_input():
			break
