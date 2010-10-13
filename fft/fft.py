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
		self.layout().addWidget(QLabel(
			"Dibuje la onda arrastrando el mouse"),1,1)
		self.layout().addWidget(self.dib,2,1)
		self.layout().addWidget(self.canvas,3,1)
		self.layout().addLayout(self.crearBotones(),1,2,3,1)

	def crearBotones(self):
		ret = QVBoxLayout()

		for widget in self.cargar_plugins():
			ret.addWidget(widget)

		return ret

	def cargar_plugins(self):
		import os,imp
		widgets = []
		# Dónde busco plugins
		dirs = [os.getcwd()+'/plugins']
		for nombre in open("plugins.cfg"):
			nombre = nombre.strip()
			if len(nombre) == 0 or nombre[0] == '#':
				continue
			try:
				fp,path,descripcion = imp.find_module(nombre,dirs)
				modulo = imp.load_module(nombre, fp, path, descripcion)
				widgets.append(modulo.Plugin(self.dib))
			except ImportError:
				print "Error cargando plugin",nombre
				continue
			finally:
				if fp:
					fp.close()
		return widgets

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
