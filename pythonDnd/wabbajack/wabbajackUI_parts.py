# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wabbajack_for_parts.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 250)
        MainWindow.setMinimumSize(QtCore.QSize(450, 250))
        MainWindow.setMaximumSize(QtCore.QSize(450, 250))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainframe = QtWidgets.QFrame(self.centralwidget)
        self.mainframe.setGeometry(QtCore.QRect(0, 0, 450, 250))
        self.mainframe.setStyleSheet("background-color: lightgrey\n"
"")
        self.mainframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainframe.setObjectName("mainframe")
        self.cast_btn = QtWidgets.QPushButton(self.mainframe)
        self.cast_btn.setGeometry(QtCore.QRect(325, 180, 100, 30))
        self.cast_btn.setObjectName("cast_btn")
        self.frame = QtWidgets.QFrame(self.mainframe)
        self.frame.setGeometry(QtCore.QRect(0, 0, 450, 150))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 450, 150))
        self.textBrowser.setStyleSheet("background-color:rgb(236, 236, 236)")
        self.textBrowser.setAcceptRichText(True)
        self.textBrowser.setObjectName("textBrowser")
        self.item_selector = QtWidgets.QComboBox(self.mainframe)
        self.item_selector.setGeometry(QtCore.QRect(20, 180, 110, 30))
        self.item_selector.setObjectName("item_selector")
        self.item_selector.addItem("")
        
        self.drink_juice = QtWidgets.QCheckBox(self.mainframe)
        self.drink_juice.setGeometry(QtCore.QRect(330, 160, 100, 20))
        self.drink_juice.setObjectName("drink_juice")
        
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cast_btn.setText(_translate("MainWindow", "cast"))
        self.textBrowser.setPlaceholderText(_translate("MainWindow", "cast output"))
        self.item_selector.setItemText(0, _translate("MainWindow", "Wabbajack"))
        self.drink_juice.setText(_translate("MainWindow", "drink juice"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

