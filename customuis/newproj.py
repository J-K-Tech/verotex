# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'customuis/newproj.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from filee import savefile
class csden(QtWidgets.QMainWindow):
    def __init__(self):
        super(QtWidgets.QMainWindow,self).__init__()
        self.setStyleSheet('background-color: rgb(30,30,30);\ncolor: rgb(30,30,30)')
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # corner grips should be "on top" of everything, otherwise the side grips
        # will take precedence on mouse events, so we are adding them *after*;
        # alternatively, widget.raise_() can be used
        
        #size
        self.center


        self.show()
        self.clicked = False

    #center
    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()
    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

class Ui_Form(object):
    def setupUi(self):
        self.Form = csden()
        self.Form.setObjectName("Form")
        self.Form.resize(440, 130)
        self.Form.setMaximumSize(440, 130)
        self.Form.setMinimumSize(440, 130)
        self.Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.Form.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.Form.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.line = QtWidgets.QFrame(self.Form)
        self.line.setGeometry(QtCore.QRect(140, 2, 281, 20))
        self.line.setStyleSheet("background-color: none;")
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.Form)
        self.line_2.setGeometry(QtCore.QRect(0, 2, 31, 20))
        self.line_2.setStyleSheet("background-color: none;")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.label = QtWidgets.QLabel(self.Form)
        self.label.setGeometry(QtCore.QRect(40, 2, 91, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(201, 255, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(201, 255, 208))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Form)
        self.label_2.setGeometry(QtCore.QRect(19, 33, 41, 16))
        self.label_2.setStyleSheet("color : #c9ffd0")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.Form)
        self.lineEdit.setGeometry(QtCore.QRect(70, 30, 361, 22))
        self.lineEdit.setStyleSheet("color: #c9ffd0")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.Form)
        self.pushButton.setGeometry(QtCore.QRect(415, 0, 25, 25))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("customuis\\../exitico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.jusclose)
        self.pushButton_2 = QtWidgets.QPushButton(self.Form)
        self.pushButton_2.setGeometry(QtCore.QRect(408, 102, 31, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: #c9ffd0")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.Form)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 401, 20))
        self.label_3.setStyleSheet("color: #c9ffd0")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.Form)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(4)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #c9ffd0")
        self.label_4.setObjectName("label_4")
        self.pushButton_2.clicked.connect(self.okie)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.Form)
        self.name = ''
        self.named = ''
        self.file = savefile()
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "New Project"))
        self.label_2.setText(_translate("Form", "name:"))
        self.pushButton_2.setText(_translate("Form", "OK"))
        self.label_3.setText(_translate("Form", "have a \"empty\" space here besause i might add something more later"))
        self.label_4.setText(_translate("Form", "*probably a file type selector"))
    def okie(self):
        self.name = self.lineEdit.text()
        
        if self.name != '':
            self.file = savefile()
            self.file.create(name)
            print(self.named)
            self.Form.close()
        else:pass
    def pop(self):
        self.Form.show()
    def jusclose(self):
        self.Form.close()
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
