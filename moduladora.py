#!/usr/bin/env python
#--coding: utf-8 --

# Grafica la moduladora de un pulso formado por un paquete de ondas
# Permite especificar la cantidad de ondas superpuestas
# Saqué la variable que especifica el espaciado de frecuencias porque sólo
# afecta la escala horizontal.

from math import sin,e,pi
from matplotlib import pyplot as pl
import numpy

from os import sys
# Cantidad de ondas superpuestas
if len(sys.argv) == 2:
	n = int(sys.argv[1])
else:
	n = 6

# Ciclos de la moduladora a graficar
ciclos = 2
# Puntos a graficar
puntos = 200

x = numpy.linspace(0,2*pi*ciclos,puntos)
y = numpy.sin(x*n)/numpy.sin(x)

pl.plot(y)
pl.show()
