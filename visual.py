#!/usr/bin/env python

from PyQt4.QtGui import *
from PyQt4.QtOpenGL import *
from OpenGL.GL import *

class VerOnda(QGLWidget):
	def __init__(self,parent=None):
		QGLWidget.__init__(self,parent)
		self.setWindowTitle("Ver Onda")
		self.resize(800,600)
		self.posicion = None

	def mostrar(self,posicion):
		self.posicion = posicion
		self.updateGL()

	def initializeGL(self):
		glClearColor(0,0,0,0)
	
	def resizeGL(self,w,h):
		glViewport(0,0,w,h)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		glOrtho(0.0,1.0,-1.0,1.0,-1.0,1.0)

	def paintGL(self):
		glClear(GL_COLOR_BUFFER_BIT)
		if self.posicion is None:
			return
		glBegin(GL_LINE_STRIP)
		glColor(1,0,0)
		for (n,y) in enumerate(self.posicion):
			x = 1.0*n/(len(self.posicion)-1)
			glVertex(x,self.posicion[n],0.0)
		glEnd()
	
if __name__ == "__main__":
	from os import sys
	from normales import *
	normales = ModosNormales([(1.0,0.0)])
	normales.calcular(0)
	a = QApplication(sys.argv)
	v = VerOnda()
	v.show()
	v.mostrar(normales.posicion)
	normales.mostrar()
	exit(a.exec_())
