#!/usr/bin/env python

from PyQt4.QtGui import *
from PyQt4.QtCore import Qt, pyqtSignal
import numpy as np

class Plugin(QGroupBox):
	def __init__(self, dib,parent=None):
		QGroupBox.__init__(self,"Modular",parent)
		self.dib = dib

		self.setLayout(QHBoxLayout())

		self.layout().addWidget(QLabel("Frecuencia de portadora:"))
		self.slider_freq = QSlider(Qt.Horizontal)
		self.slider_freq.setMinimum(1)
		self.slider_freq.setMaximum(self.dib.resolucion/2-1)
		self.slider_freq.setValue(40)
		self.layout().addWidget(self.slider_freq)
		self.label_freq = QLabel(str(self.slider_freq.value()))
		self.slider_freq.valueChanged.connect(self.label_freq.setNum)
		self.layout().addWidget(self.label_freq)

		modular = QPushButton("Modular")
		modular.clicked.connect(self.modular)
		self.layout().addWidget(modular)

	def modular(self):
		""" Multiplico por una portadora """
		# Fportadora / F0
		f = self.slider_freq.value()
		w = f*2*np.pi/self.dib.resolucion
		x = np.arange(self.dib.resolucion)
		nueva = np.sin(w*x)*self.dib.puntos
		self.dib.cargar(nueva)

