# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/XonStat.ui'
#
# Created: Mon May 27 14:54:21 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(500, 150)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(10000, 10000))
        MainWindow.setWindowTitle(_fromUtf8("XonStat Tool"))
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btnImport = QtGui.QPushButton(self.centralwidget)
        self.btnImport.setGeometry(QtCore.QRect(390, 30, 99, 23))
        self.btnImport.setObjectName(_fromUtf8("btnImport"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(10, 10, 371, 36))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.lbImport = QtGui.QLabel(self.splitter)
        self.lbImport.setTextFormat(QtCore.Qt.AutoText)
        self.lbImport.setObjectName(_fromUtf8("lbImport"))
        self.lineImport = QtGui.QLineEdit(self.splitter)
        self.lineImport.setObjectName(_fromUtf8("lineImport"))
        self.splitter_2 = QtGui.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(10, 70, 371, 36))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.lbExport = QtGui.QLabel(self.splitter_2)
        self.lbExport.setTextFormat(QtCore.Qt.AutoText)
        self.lbExport.setObjectName(_fromUtf8("lbExport"))
        self.lineExport = QtGui.QLineEdit(self.splitter_2)
        self.lineExport.setObjectName(_fromUtf8("lineExport"))
        self.btnExport = QtGui.QPushButton(self.centralwidget)
        self.btnExport.setGeometry(QtCore.QRect(390, 90, 99, 23))
        self.btnExport.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.btnExport.setObjectName(_fromUtf8("btnExport"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.btnImport.setText(_translate("MainWindow", "Import", None))
        self.lbImport.setText(_translate("MainWindow", "Choose file to import", None))
        self.lbExport.setText(_translate("MainWindow", "Choose file to export", None))
        self.btnExport.setText(_translate("MainWindow", "Export", None))

