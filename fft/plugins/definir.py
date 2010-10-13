#!/usr/bin/env python
#--coding: utf-8 --

from PyQt4.QtGui import *
from PyQt4.QtCore import Qt, pyqtSignal
import numpy as np

class Plugin(QGroupBox):
	def __init__(self,dib,parent=None):
		QGroupBox.__init__(self,u"Definir señal",parent)
		self.dib = dib

		self.setLayout(QGridLayout())
		self.layout().addWidget(QLabel("Intensidad"),1,1,1,1)
		self.slider_constante = QSlider(Qt.Horizontal)
		self.slider_constante.setMinimum(-100)
		self.slider_constante.setMaximum(100)
		self.layout().addWidget(self.slider_constante,1,2,1,1)
		self.label_constante = QLabel("0")
		self.slider_constante.valueChanged.connect(self.label_constante.setNum)
		self.layout().addWidget(self.label_constante,1,3,1,1)

		constante = QPushButton("Constante")
		constante.clicked.connect(self.constante)
		self.layout().addWidget(constante,1,4,1,1)

		ruido = QPushButton("Ruido")
		ruido.clicked.connect(self.ruido)
		self.layout().addWidget(ruido,2,1,1,4)

	def constante(self):
		""" Asigno un valor a la señal """
		rango = self.slider_constante.maximum()
		self.dib.cargar(np.repeat(1.0/rango*self.slider_constante.value(),
			self.dib.resolucion))

	def ruido(self):
		""" Creo una señal al azar """
		self.dib.cargar(np.random.random((self.dib.resolucion))*2-1)
