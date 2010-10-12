#!/usr/bin/env python
#--coding: utf-8 --

from PyQt4.QtGui import *
from PyQt4.QtCore import Qt, pyqtSignal
from PyQt4 import QtCore
import numpy as np
from dibuja import Dibuja
from matplotlib import pyplot as pl
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

class VentanaFFT(QWidget):
	def __init__(self,parent=None):
		QWidget.__init__(self,parent)
		self.resize(800,600)

		# Para dibujar la señal
		self.dib = Dibuja()
		self.dib.cambio.connect(self.espectro)

		# Para graficar la fft
		self.fig = pl.Figure((8,4),dpi=120)
		self.axes = self.fig.add_subplot(111)
		self.canvas = FigureCanvas(self.fig)

		# Dispongo todo 
		#self.canvas.setParent(izquierdo)
		self.setLayout(QGridLayout())
		#self.setLayout(izquierdo)
		self.layout().addWidget(self.dib,1,1)
		self.layout().addWidget(self.canvas,2,1)
		self.layout().addLayout(self.crearBotones(),1,2,2,1)

	def crearBotones(self):
		cont1 = QGroupBox(u"Definir señal")
		cont1.setLayout(QHBoxLayout())
		self.slider_constante = QSlider(Qt.Horizontal)
		self.slider_constante.setMinimum(-10)
		self.slider_constante.setMaximum(10)
		cont1.layout().addWidget(self.slider_constante)
		self.label_constante = QLabel("0")
		self.slider_constante.valueChanged.connect(self.label_constante.setNum)
		cont1.layout().addWidget(self.label_constante)

		cero = QPushButton("Constante")
		cero.clicked.connect(self.constante)
		cont1.layout().addWidget(cero)

		modular = QPushButton("Modular")
		modular.clicked.connect(self.modular)

		ret = QVBoxLayout()
		ret.addWidget(cont1)
		ret.addWidget(modular)
		return ret

	def constante(self):
		""" Vuelvo la señal a cero """
		self.dib.cargar(np.repeat(0.1*self.slider_constante.value(),
			self.dib.resolucion))

	def modular(self):
		""" Multiplico por una portadora """
		# Fportadora / F0
		f = 40
		w = f*2*np.pi/self.dib.resolucion
		x = np.arange(self.dib.resolucion)
		nueva = np.sin(w*x)*self.dib.puntos
		self.dib.cargar(nueva)

	def espectro(self):
		# Grafico la transformada
		espectro = np.fft.rfft(self.dib.puntos)
		self.axes.clear()
		self.axes.grid(True)
		fmax = self.dib.resolucion/2+1
		self.axes.plot(range(1,fmax),
				np.abs(espectro[1:fmax]),'ro')
		self.axes.vlines(range(1,fmax),[0],
				np.abs(espectro[1:fmax]))
		self.canvas.draw()

if __name__ == "__main__":
	from os import sys
	app = QApplication(sys.argv)
	v = VentanaFFT()
	v.showMaximized()
	exit(app.exec_())