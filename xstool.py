import sys
from PyQt4 import QtCore, QtGui

from ui.mainwindow import Ui_MainWindow
from fileutils import file_import

class XonStatForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
                
        QtCore.QObject.connect(self.ui.btnImport, QtCore.SIGNAL("clicked()"), file_import(self.ui.lineImport.text()))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = XonStatForm()
    myapp.show()
    sys.exit(app.exec_())
