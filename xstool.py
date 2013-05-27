#!/usr/bin/python3

import sys
import os

from PyQt4 import QtCore, QtGui

from ui.mainwindow import Ui_MainWindow

class XonStatForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.keypath = os.path.expanduser('~/.xonotic/key_0.d0si')
                
        QtCore.QObject.connect(self.ui.btnImport, QtCore.SIGNAL("clicked()"), self.file_import)
        QtCore.QObject.connect(self.ui.btnExport, QtCore.SIGNAL("clicked()"), self.file_export)
        
    def file_import(self):
        sourcepath = self.ui.lineImport.text()
        
        with open(sourcepath, 'rb') as sourcefile:
            cache = sourcefile.read()
        with open(self.keypath, 'wb') as keyfile:
            keyfile.write(cache)

    def file_export(self):
        descpath = self.ui.lineExport.text()
        
        with open(self.keypath, 'rb') as keyfile:
            cache = keyfile.read()
        with open(descpath, 'wb') as descfile:
            descfile.write(cache)

        

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = XonStatForm()
    myapp.show()
    sys.exit(app.exec_())
