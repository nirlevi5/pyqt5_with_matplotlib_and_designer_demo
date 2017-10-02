# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MplMainWindow(object):
    def setupUi(self, MplMainWindow):
        MplMainWindow.setObjectName("MplMainWindow")
        MplMainWindow.resize(800, 600)
        self.mplcentralwidget = QtWidgets.QWidget(MplMainWindow)
        self.mplcentralwidget.setObjectName("mplcentralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mplcentralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mplhorizontalLayout = QtWidgets.QHBoxLayout()
        self.mplhorizontalLayout.setObjectName("mplhorizontalLayout")
        self.mpllineEdit = QtWidgets.QLineEdit(self.mplcentralwidget)
        self.mpllineEdit.setObjectName("mpllineEdit")
        self.mplhorizontalLayout.addWidget(self.mpllineEdit)
        self.mplpushButton = QtWidgets.QPushButton(self.mplcentralwidget)
        self.mplpushButton.setObjectName("mplpushButton")
        self.mplhorizontalLayout.addWidget(self.mplpushButton)
        self.verticalLayout.addLayout(self.mplhorizontalLayout)
        self.mpl = MplWidget(self.mplcentralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mpl.sizePolicy().hasHeightForWidth())
        self.mpl.setSizePolicy(sizePolicy)
        self.mpl.setObjectName("mpl")
        self.verticalLayout.addWidget(self.mpl)
        MplMainWindow.setCentralWidget(self.mplcentralwidget)
        self.mplmenubar = QtWidgets.QMenuBar(MplMainWindow)
        self.mplmenubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.mplmenubar.setObjectName("mplmenubar")
        self.menuFile = QtWidgets.QMenu(self.mplmenubar)
        self.menuFile.setObjectName("menuFile")
        MplMainWindow.setMenuBar(self.mplmenubar)
        self.actionOpen = QtWidgets.QAction(MplMainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionQuit = QtWidgets.QAction(MplMainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.mplmenubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MplMainWindow)
        QtCore.QMetaObject.connectSlotsByName(MplMainWindow)

    def retranslateUi(self, MplMainWindow):
        _translate = QtCore.QCoreApplication.translate
        MplMainWindow.setWindowTitle(_translate("MplMainWindow", "MainWindow"))
        self.mplpushButton.setText(_translate("MplMainWindow", "PushButton"))
        self.menuFile.setTitle(_translate("MplMainWindow", "File"))
        self.actionOpen.setText(_translate("MplMainWindow", "Open"))
        self.actionQuit.setText(_translate("MplMainWindow", "Quit"))

from mplwidget import MplWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MplMainWindow = QtWidgets.QMainWindow()
    ui = Ui_MplMainWindow()
    ui.setupUi(MplMainWindow)
    MplMainWindow.show()
    sys.exit(app.exec_())

