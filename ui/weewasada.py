        self.verotexmaker.center()
        self.verotexmaker.oldPos = self.verotexmaker.pos()
        self.verotexmaker.show()

    def center(self):
        qr = self.verotexmaker.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.verotexmaker.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.verotexmaker.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.verotexmaker.oldPos)
        self.verotexmaker.move(self.verotexmaker.x() + delta.x(), self.verotexmaker.y() + delta.y())
        self.verotexmaker.oldPos = event.globalPos()