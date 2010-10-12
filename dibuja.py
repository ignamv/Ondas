#!/usr/bin/env python
#--coding: utf-8 --

from OpenGL.GL import *
from PyQt4.QtGui import *
from PyQt4.QtOpenGL import *
from PyQt4.QtCore import Qt, pyqtSignal
from PyQt4 import QtCore
import numpy as np

class Dibuja(QGLWidget):
	""" Widget que permite ver y modificar con el mouse un array
	Grafica el valor en función del índice como un gráfico de línea
	Al hacer click o arrastrar en el gráfico modifica el valor y actualiza la
	imagen.
	"""

	cambio = pyqtSignal()

	def __init__(self,parent=None):
		QGLWidget.__init__(self,parent)
		self.resolucion = 300
		self.puntos = np.zeros((self.resolucion))

		# Cuando estoy dibujando, uso esto para guardar la última posición
		# registrada del mouse, así puedo interpolar si se salteó puntos
		self.ultimo = None

	def sizePolicy(self):
		return QSizePolicy( QSizePolicy.Ignored, QSizePolicy.Expanding)
	
	def sizeHint(self):
		return QtCore.QSize(640,480)
	def minimumSizeHint(self):
		return QtCore.QSize(640,480)

	def initializeGL(self):
		glClearColor(0,0,0,0)

	def resizeGL(self,w,h):
		glViewport(0,0,w,h)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		glOrtho(0,1,-1,1,-1,1)

	def paintGL(self):
		glClear(GL_COLOR_BUFFER_BIT)
		glColor(1,1,1)
		glBegin(GL_LINE_STRIP)
		for (n,y) in enumerate(self.puntos):
			glVertex(1.0*n/self.resolucion,y,0)
		glEnd()
		glColor(0,1,0)
		glBegin(GL_LINES)
		glVertex(0,0,0)
		glVertex(1,0,0)
		glEnd()


	def mouseMoveEvent(self, ev):
		if ev.buttons() & Qt.LeftButton:
			self.interpolar(ev.x(),ev.y())

	def mousePressEvent(self,ev):
		if ev.buttons() & Qt.LeftButton:
			self.actualizar(ev.x(),ev.y())
	
	def mouseReleaseEvent(self,ev):
		self.ultimo = None
		self.cambio.emit()

	def cargar(self,puntos):
		self.resolucion = len(puntos)
		self.puntos = np.copy(puntos)
		self.cambio.emit()
		self.updateGL()

	def interpolar(self,x,y):
		# Lleno los puntos intermedios
		# Salvo que sea el primero
		if self.ultimo is None:
			self.actualizar(x,y)
			return
		x = int(1.0*x*self.resolucion/self.width())
		y = 1-2.0*y/self.height()
		if x<0 or x>=self.resolucion or y<-1 or y>=1:
			return
		self.puntos[self.ultimo[0]+1:x+1] = np.linspace(
				self.ultimo[1],y,x-self.ultimo[0])
		self.ultimo = (x,y)
		self.updateGL()


	def actualizar(self,x,y):
		x = int(1.0*x*self.resolucion/self.width())
		y = 1-2.0*y/self.height()
		if x<0 or x>=self.resolucion or y<-1 or y>=1:
			return
		self.puntos[int(x)] = y
		self.ultimo = (x,y)
		self.updateGL()

if __name__ == "__main__":
	from os import sys
	a = QApplication(sys.argv)
	v = Dibuja()
	v.show()
	exit(a.exec_())
