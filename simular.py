#!/usr/bin/env python
#--coding: utf-8 --

from normales import *
from visual import *

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Simulacion(QWidget):
	def __init__(self,modos=None,parent=None):
		QWidget.__init__(self,parent)
		self.setWindowTitle(u"Simulación de cuerda")
		self.resize(800,600)

		if modos is None:
			modos = [(1.0,0.0)]
		self.normales = ModosNormales(modos)
		self.ver = VerOnda()

		self.setLayout(QGridLayout())

		self.layout().addWidget(self.ver,1,1,1,2)
		self.t = 0
		
		caja = QGroupBox(u"Frecuencia de simulación")
		lcaja = QVBoxLayout()
		scroll = QScrollBar(Qt.Horizontal)
		scroll.setMinimum(0)
		scroll.setMaximum(100)
		scroll.setValue(40)
		scroll.valueChanged.connect(self.setPaso)
		lcaja.addWidget(scroll)
		self.freq = QLabel()
		caja.setLayout(lcaja)
		#lcaja.addWidget(freq)
		self.layout().addWidget(caja,2,1,1,1)

		caja = QGroupBox("Modos")
		lcaja = QVBoxLayout()

		self.paso = 0.005
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.tick)
		self.timer.start(10)

	def setPaso(self,paso):
		self.paso = 0.0001 * paso

	def tick(self):
		self.t += self.paso
		self.t %= 1
		#print self.t
		self.normales.calcular(self.t)
		self.ver.mostrar(self.normales.posicion)

if __name__ == "__main__":
	from os import sys
	app = QApplication(sys.argv)
	#modos = [(1.0,0),(0.0,0.0),(0.0,0.0)]
	#modos = [(math.cos(math.pi*i)/2/i**2,0) for i in range(1,13)]
	modos = [(9*math.sin(n*math.pi/2)/n**2/math.pi**2,0) for n in range(1,20)]
	s = Simulacion(modos)
	s.show()
	exit(app.exec_())
