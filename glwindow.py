import PyQt5 as qt
from OpenGL.GL import *
import OpenGL_accelerate as gla
import numpy as np

class glwindow(qt.QtWidgets.QOpenGLWidget):
    def __init__(self,window):
        super().__init__(window)
        self.initializeGL()
        self.color = (0.5,0.5,0.5)
        self.glcolor = (0.0,0.0,0.0)
    def setcolor(self,color):
        self.color = color
        r = (self.color[0]/255)
        g = (self.color[1]/255)
        b = (self.color[2]/255)
        a = 1.0
        self.glcolor(r,g,b,a)
        glClearColor(self.glcolor[0],self.glcolor[1],self.glcolor[2],self.glcolor[3])
        glClear(GL_COLOR_BUFFER_BIT)
        
        