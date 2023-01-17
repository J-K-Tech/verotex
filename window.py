import PyQt5 as qt
from windalpha import Ui_verotexmaker as umain
import OpenGL
import OpenGL_accelerate
import sys


a = True
class program():
    def __init__(self):
        self.window = umain()
        self.scr = qt.QtWidgets.QMainWindow()
        self.window.setupUi(self.scr)
        
        size = qt.QtCore.QSize
        #size.height(100)
        #size.width(150)
        #self.picker.setMaximumSize(size)
        #self.window.treeWidget.setItemWidget(,0,self.picker)
    def show(self):
        self.scr.show()
if __name__ == "__main__":
    app = qt.QtWidgets.QApplication(sys.argv)
    verotex = program()
    verotex.show()
    sys.exit(app.exec_())
