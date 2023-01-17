from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from info import Ui_MainWindow as info
import sys
from customuis.newproj import Ui_Form as newpro
from customuis.newpatt import Ui_Form as newptt
from customuis.newpatt import *
class dropdownmenu(QtWidgets.QWidget):
    def __init__(self,parent):
        super(QtWidgets.QWidget).__init__(parent)
        self.title_bar = title(self)
        self.status_bar = status(self)

        self.layout  = QHBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addWidget(self.title_bar)
        self.layout.addStretch(1)
        self.layout.addWidget(self.status_bar)
        self.layout.setSpacing(0)

class TitleBar(QtWidgets.QWidget):
    height = 35
    def __init__(self):
        super(TitleBar, self).__init__()
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)

        self.menu_bar = QMenuBar()
        self.menu_bar.setContentsMargins(0,0,0,0)
        self.menu_bar.setStyleSheet("""
            QMenuBar::item:selected {background-color:rgb(80,80,80); };
            color: rgb(201, 255, 208);
            background-color: rgb(30, 30, 30);
            font-size: 14px;
            padding: 4px; 
        """)  
        self.ico = self.menu_bar.addMenu(QtGui.QIcon('ico.png'),'')
        self.icoinfo=self.ico.addAction('info')
        self.icohelp=self.ico.addAction('help')
        self.menu_file = self.menu_bar.addMenu('file')
        self.menu_file_new=self.menu_file.addAction('new')
        self.menu_file_open=self.menu_file.addAction('open')
        self.menu_file_save=self.menu_file.addAction('save')
        self.menu_file_saveas=self.menu_file.addAction('save as...')
        self.icoinfo.triggered.connect(self.info)
        self.menu_file_save.triggered.connect(self.save)
        self.menu_file_saveas.triggered.connect(self.saveas)
        self.menu_file_open.triggered.connect(self.open)
        self.menu_file_new.triggered.connect(self.new)

        self.menu_work=self.menu_bar.addMenu('properties')

        self.layout.addWidget(self.menu_bar) 
        self.setLayout(self.layout)

        self.start = QPoint(0, 0)
        self.pressing = False
        self.maximaze = False
        self.projname = ''
        self.newf = newpro()
        self.newf.setupUi()
        self.projname = self.newf.named


    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end-self.start
            self.parent.move(self.mapToGlobal(self.movement))
            self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False
    def info(self):
        self.openwindow(1)
    def save(self):
        self.openwindow(2)
    def saveas(self):
        self.openwindow(3)
    def open(self):
        self.openwindow(4)
    def new(self):
        self.openwindow(5)

    def openwindow(self,value):
        if value == 1:
            self.pop = info()
            self.pop.pop()
        if value == 2:
            self.projname = self.newf.named
            self.pop = QFileDialog.getSaveFileName(self, 'Save File',self.projname,'vrtx')
        if value == 3:
            self.projname = self.newf.named
            self.pop = QFileDialog.getSaveFileName(self, 'Save File As...',self.projname,'vrtx\nsai2\npsd','vrtx')
        if value == 4:
            self.pop = QFileDialog.getOpenFileName(self, 'Open File','vrtx\nsai2\npsd','vrtx')
        if value == 5:
            self.newf.pop()
            

class patterntex(QtWidgets.QGroupBox):
    def __init__(self):
        super(QtWidgets.QGroupBox,self).__init__()
        self.setMinimumSize(QtCore.QSize(200, 250))
        
        self.setMaximumSize(QtCore.QSize(200, 250))
        self.setContentsMargins(2,2,2,2)
        self.setFlat(False)
        self.setCheckable(False)
        self.setObjectName("texture")
        self.setStyleSheet('color: rgb(201,255,208);\nbackground-color:rgba(70,70,70,0)')
        self.name = QtWidgets.QLabel('name:',self)
        self.name.setGeometry(QtCore.QRect(10, 150, 50, 22))
        self.wid = QtWidgets.QLabel('width:',self)
        self.wid.setGeometry(QtCore.QRect(10, 180, 50, 22))
        self.hei = QtWidgets.QLabel('height:',self)
        self.hei.setGeometry(QtCore.QRect(10, 210, 50, 22))
        self.keySequenceEdit_7 = QtWidgets.QLineEdit(self)
        self.keySequenceEdit_7.setGeometry(QtCore.QRect(70, 150, 113, 22))
        self.keySequenceEdit_7.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.keySequenceEdit_7.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.keySequenceEdit_7.setStyleSheet("background-color: rgb(29, 29, 29);")
        self.keySequenceEdit_7.setObjectName("keySequenceEdit_7")
        self.keySequenceEdit_8 = QtWidgets.QLabel(self)
        self.keySequenceEdit_8.setGeometry(QtCore.QRect(70, 180, 113, 22))
        self.keySequenceEdit_8.setStyleSheet("background-color: rgb(29, 29, 29);")
        self.keySequenceEdit_8.setObjectName("keySequenceEdit_8")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self)
        self.graphicsView_3.setGeometry(QtCore.QRect(50, 30, 100, 100))
        self.graphicsView_3.setStyleSheet("background-color: rgb(80, 80, 80);\n"
"")
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.keySequenceEdit_9 = QtWidgets.QLabel(self)
        self.keySequenceEdit_9.setGeometry(QtCore.QRect(70, 210, 113, 22))
        self.keySequenceEdit_9.setStyleSheet("background-color: rgb(29, 29, 29);")
        self.keySequenceEdit_9.setObjectName("keySequenceEdit_9")
        self.setTitle(str(self.keySequenceEdit_7.text()))
        self.qTimer = QTimer()
        self.qTimer.setInterval(100)
        self.qTimer.timeout.connect(self.update)
        self.qTimer.start()
    def update(self):
        self.setTitle(str(self.keySequenceEdit_7.text()))
        self.qTimer.start()



class SideGrip(QtWidgets.QWidget):
    def __init__(self, parent, edge):
        QtWidgets.QWidget.__init__(self, parent)
        self.setStyleSheet('background-color: rgb(30,30,30);\ncolor: rgb(30,30,30)')
        if edge == QtCore.Qt.LeftEdge:
            self.setCursor(QtCore.Qt.SizeHorCursor)
            self.resizeFunc = self.resizeLeft
        elif edge == QtCore.Qt.TopEdge:
            self.setCursor(QtCore.Qt.SizeVerCursor)
            self.resizeFunc = self.resizeTop
        elif edge == QtCore.Qt.RightEdge:
            self.setCursor(QtCore.Qt.SizeHorCursor)
            self.resizeFunc = self.resizeRight
        else:
            self.setCursor(QtCore.Qt.SizeVerCursor)
            self.resizeFunc = self.resizeBottom
        self.mousePos = None
        self.pressed = False

    def resizeLeft(self, delta):
        window = self.window()
        width = max(window.minimumWidth(), window.width() - delta.x())
        geo = window.geometry()
        geo.setLeft(geo.right() - width)
        window.setGeometry(geo)

    def resizeTop(self, delta):
        window = self.window()
        height = max(window.minimumHeight(), window.height() - delta.y())
        geo = window.geometry()
        geo.setTop(geo.bottom() - height)
        window.setGeometry(geo)

    def resizeRight(self, delta):
        window = self.window()
        width = max(window.minimumWidth(), window.width() + delta.x())
        window.resize(width, window.height())

    def resizeBottom(self, delta):
        window = self.window()
        height = max(window.minimumHeight(), window.height() + delta.y())
        window.resize(window.width(), height)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.mousePos = event.pos()
            self.pressed = True

    def mouseMoveEvent(self, event):
        if self.mousePos is not None:
            delta = event.pos() - self.mousePos
            self.resizeFunc(delta)

    def mouseReleaseEvent(self, event):
        self.mousePos = None
        self.pressed = False

class gripp(QtWidgets.QSizeGrip):
    def __init__(self,parent):
        super(QtWidgets.QSizeGrip,self).__init__(parent)
        self.clicked = False
    def mousePressEvent(self, event):
        self.clicked = True
    def mouseReleaseEvent(self, event):
        self.clicked = False

class cssden(QtWidgets.QMainWindow):
    _gripSize = 3
    def __init__(self):
        super(QtWidgets.QMainWindow,self).__init__()
        self.setStyleSheet('background-color: rgb(30,30,30);\ncolor: rgb(30,30,30)')
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.sideGrips = [
            SideGrip(self, QtCore.Qt.LeftEdge), 
            SideGrip(self, QtCore.Qt.TopEdge), 
            SideGrip(self, QtCore.Qt.RightEdge), 
            SideGrip(self, QtCore.Qt.BottomEdge), 
        ]
        # corner grips should be "on top" of everything, otherwise the side grips
        # will take precedence on mouse events, so we are adding them *after*;
        # alternatively, widget.raise_() can be used
        
        self.cornerGrips = [gripp(self) for i in range(4)]
        #size
        self.setFixedSize(320, 450)
        self.center
        self.move(500,300)



        self.show()
        self.clicked = False

    #center
    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def mousePressEvent(self, event):
        if self.cornerGrips[0].clicked == True:
            pass
        elif self.cornerGrips[1].clicked == True:
            pass
        elif self.cornerGrips[2].clicked == True:
            pass
        elif self.cornerGrips[3].clicked == True:
            pass
        else:self.oldPos = event.globalPos()
        self.clicked = True

    def mouseMoveEvent(self, event):
        if self.clicked == True:
            delta = QPoint (event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
    def mouseReleaseEvent(self,event):
        self.clicked = False
        
    @property
    def gripSize(self):
        return self._gripSize

    def setGripSize(self, size):
        if size == self._gripSize:
            return
        self._gripSize = max(2, size)
        self.updateGrips()

    def updateGrips(self):
        self.setContentsMargins(*[self.gripSize] * 4)

        outRect = self.rect()
        # an "inner" rect used for reference to set the geometries of size grips
        inRect = outRect.adjusted(self.gripSize, self.gripSize,
            -self.gripSize, -self.gripSize)

        # top left
        self.cornerGrips[0].setGeometry(
            QtCore.QRect(outRect.topLeft(), inRect.topLeft()))
        # top right
        self.cornerGrips[1].setGeometry(
            QtCore.QRect(outRect.topRight(), inRect.topRight()).normalized())
        # bottom right
        self.cornerGrips[2].setGeometry(
            QtCore.QRect(inRect.bottomRight(), outRect.bottomRight()))
        # bottom left
        self.cornerGrips[3].setGeometry(
            QtCore.QRect(outRect.bottomLeft(), inRect.bottomLeft()).normalized())

        # left edge
        self.sideGrips[0].setGeometry(
            0, inRect.top(), self.gripSize, inRect.height())
        # top edge
        self.sideGrips[1].setGeometry(
            inRect.left(), 0, inRect.width(), self.gripSize)
        # right edge
        self.sideGrips[2].setGeometry(
            inRect.left() + inRect.width(), 
            inRect.top(), self.gripSize, inRect.height())
        # bottom edge
        self.sideGrips[3].setGeometry(
            self.gripSize, inRect.top() + inRect.height(), 
            inRect.width(), self.gripSize)

    def resizeEvent(self, event):
        QtWidgets.QMainWindow.resizeEvent(self, event)
        self.updateGrips()

class viewer(QtWidgets.QGraphicsView):
    def __init__(self,imports):
        a,self.patternwin,self.patternamm,self.patternrow,self.hex = imports
        super(QtWidgets.QGraphicsView,self).__init__(a)
        self._zoom = 0
        self.mx = 0
        self.my = 0
        self.setMouseTracking(True)
    def wheelEvent(self,event):    
        if event.angleDelta().y() > 0:
            factor = 1.25
            self._zoom += 1
        else:
            factor = 0.8
            self._zoom -= 1
        if self._zoom > 0:
            self.scale(factor, factor)
        elif self._zoom == 0:
            self.fitInView()
        else:
            self._zoom = 0


class editor(QtWidgets.QWidget):
    def __init__(self,mainwin,patternwin,tex):
        super(QtWidgets.QWidget,self).__init__()
        self.setContentsMargins(9,9,9,9)
        self.mainw = mainwin
        self.patternwin = patternwin
        self.patternamm = 1
        self.patternrow = 0
        self._scene = QtWidgets.QGraphicsScene(self)
        
        
        imports = (self._scene,self.patternwin,self.patternamm,self.patternrow,tex)
        self.view = viewer(imports)
        self.view.layout = QtWidgets.QBoxLayout(2,self.view)
        self.view.layout.setContentsMargins(0,0,0,0)
        self.view.layout.setAlignment(QtCore.Qt.AlignCenter)
        self.layout = QtWidgets.QBoxLayout(2,self)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.view,1)
        self.editormenu = editormenu(self.view)
        self.editormenu.hide()
    def mousePressEvent(self,event):
        if event.buttons() == Qt.RightButton:
            pos = event.pos()
            x = pos.x()
            y = pos.y()
            ppos = self.pos()
            xx = ppos.x()
            yy = ppos.y()
            posy = self.mainw.pos()
            xxx = posy.x()
            yyy = posy.y()
            self.editormenu.move(xx+x+xxx+280,yy+y+yyy+20)
            self.editormenu.show()
        
class sure(QtWidgets.QMenu):
    def __init__(self,par,layoutimport):
        super(QtWidgets.QMenu,self).__init__()
        self.a = newptt()
        self.pattern = self.addAction('close pattern without saving?')
        self.pattern.setDisabled(True)
        self.patterno = self.addAction('yes')
        self.patternum = self.addAction('no')
        self.patterno.triggered.connect(lambda: self.np(par))
        self.XY = self.a.ww,self.a.hh
    def np(self,par):
        wid = par.layout.itemAt(0).widget()
        wid.setParent(None)
        wid.destroy()
        self.a.pop(par,patterntex)


class editormenu(QtWidgets.QMenu):
    def __init__(self,par):
        super(QtWidgets.QMenu,self).__init__()
        self.a = newptt()
        self.pattern = self.addAction('new pattern')
        self.pattern.triggered.connect(lambda: self.np(par))
        self.XY = self.a.ww,self.a.hh
        layoutimport = patterntex
        self.sure = sure(par,layoutimport)
        self.setContentsMargins(0,0,0,0)
        self.setStyleSheet("\n"
"QMenu::item:selected {background-color:rgb(110,110,110); color:rgb(201,255,208);}\n"
"QMenu::item {background-color:rgb(80,80,80); color:rgb(201,255,208);}\n"
"Qmenu { background-color: rgb(80,80,80);color:rgb(201,255,208);};\n"
"border-color: rgb(50, 50, 50);"
"border-right-color: rgb(50, 50, 50)")
    def np(self,par):
        if par.layout.itemAt(0) == None:
            
            self.a.pop(par,patterntex)
        else:
            pos = self.pos()
            x = pos.x()
            y= pos.y()

            self.sure.move(x+50,y+0)
            self.sure.show()

        
