#!/usr/bin/env python

from math import pi,e,cos
from cmath import phase
from grafourier import *

#def cn(n,rel):
	#return 1j/2/pi/n*(e**(1j*2*pi*n*rel)-1)

#def cn10(n):
	#return cn(n,0.1)

rel = 0.5
cn = [1j/2/pi/n*(e**(1j*2*pi*n*rel)-1) for n in range(1,90)]

graficar(cn)
