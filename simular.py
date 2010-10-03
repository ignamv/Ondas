#!/usr/bin/env python
#--coding: utf-8 --

from normales import *
from visual import *

from PyQt4.QtGui import *
from PyQt4.QtCore import QTimer

class Simulacion(QWidget):
	def __init__(self,parent=None):
		QWidget.__init__(self,parent)
		self.setWindowTitle(u"Simulación de cuerda")
		self.resize(800,600)
		self.normales = ModosNormales([(0.5,0),(0.25,0)],False,True)
		self.ver = VerOnda()
		self.setLayout(QVBoxLayout())
		self.layout().addWidget(self.ver)
		self.t = 0
		self.paso = 0.01
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.tick)
		self.timer.start(25)

	def tick(self):
		self.t += self.paso
		print self.t
		self.normales.calcular(self.t)
		self.ver.mostrar(self.normales.posicion)

if __name__ == "__main__":
	from os import sys
	app = QApplication(sys.argv)
	s = Simulacion()
	s.show()
	exit(app.exec_())
