#!/usr/bin/env python

from math import cos,pi
from matplotlib import pyplot as pl

from os import sys
# Cantidad de ondas superpuestas
if len(sys.argv) == 2:
	n = int(sys.argv[1])
else:
	n = 6

# Frecuencia inicial
f0 = 50
# Espaciado de frecuencias
df = 5
# Ciclos de la portadora a calcular
ciclos = 50
# Puntos por segundo
puntos = 1000

y = [0 for i in xrange(ciclos*puntos/f0)]

for i in range(n):
	f = (f0+i*df)
	w = 2*pi*f/puntos
	for x in range(len(y)):
		y[x] += cos(w*x)

pl.plot(y)
pl.show()
