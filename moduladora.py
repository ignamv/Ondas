#!/usr/bin/env python
#--coding: utf-8 --

# Grafica la moduladora de un pulso formado por un paquete de ondas
# Permite especificar la cantidad de ondas superpuestas
# Saqué la variable que especifica el espaciado de frecuencias porque sólo
# afecta la escala horizontal.

from math import sin,e,pi
from matplotlib import pyplot as pl

from os import sys
# Cantidad de ondas superpuestas
if len(sys.argv) == 2:
	n = int(sys.argv[1])
else:
	n = 6

# Ciclos de la moduladora a graficar
ciclos = 2
# Puntos a graficar por ciclo
puntos = 200

# Período = 2pi/dw
# Cada punto = 2pi/dw/puntos

y = []
for x in xrange(1,ciclos*puntos):
	try:
		y.append(sin(x*n*2*pi/puntos)/sin(x*2*pi/puntos))
	except ZeroDivisionError:
		y.append(y[-1])

pl.plot(y)
pl.show()
