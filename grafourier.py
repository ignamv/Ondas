#!/usr/bin/env python
#--coding: utf-8 --

from math import pi,e,cos
from cmath import phase
from matplotlib import pyplot as pl
import numpy

def graficar(cn,xmax=1000,ciclos=2):
	""" Evalúa la función cn para encontrar los coeficientes de Fourier de una
	función, y la grafica con nmax senos """
	# Cantidad de puntos
	w0 = 2*pi*ciclos

	x = numpy.linspace(0,ciclos,xmax)
	y = numpy.zeros(xmax)
	for (n,c) in enumerate(cn):
		y += numpy.real(c*numpy.exp(1j*w0*(n+1)*x))

	#y = numpy.real(cn[1]*numpy.exp(1j*w0*2*x))

	pl.plot(x,y)
	pl.show()

