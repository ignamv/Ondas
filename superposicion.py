#!/usr/bin/env python

from math import cos,pi
from matplotlib import pyplot as pl
import numpy

from os import sys
# Cantidad de ondas superpuestas
if len(sys.argv) == 2:
	n = int(sys.argv[1])
else:
	n = 6

# Frecuencia inicial
f0 = 1
# Espaciado de frecuencias
df = 0.05
# Ciclos del pulso a graficar
ciclos = 5
# Puntos a graficar
puntos = 10000

y = numpy.zeros((puntos))
x = numpy.linspace(0,ciclos/df,puntos)

for i in range(n):
	w = 2*pi*(f0+i*df)
	y += numpy.cos(w*x)

pl.plot(y)
pl.show()
