from re import S
from PyQt5 import QtCore, QtGui, QtWidgets
import wabbajack as wj
import wabbajackJuice as wjjuice
import sys
WIDTH = 450
HEIGHT = 250


class Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(WIDTH, HEIGHT)
        MainWindow.setMinimumSize(QtCore.QSize(WIDTH, HEIGHT))
        MainWindow.setMaximumSize(QtCore.QSize(WIDTH, HEIGHT))
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.mainframe = QtWidgets.QFrame(self.centralwidget)
        self.mainframe.setGeometry(QtCore.QRect(0, 0, WIDTH, HEIGHT))
        self.mainframe.setStyleSheet("background-color: lightgrey\n")
        self.mainframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainframe.setObjectName("mainframe")
        
        self.juice_box = QtWidgets.QRadioButton(self.mainframe)
        self.juice_box.setGeometry(QtCore.QRect(325, 160, 100, 20))
        self.juice_box.setObjectName("juice_box")
        self.juice_box.setChecked(False)
    
        self.cast_btn = QtWidgets.QPushButton(self.mainframe)
        self.cast_btn.setGeometry(QtCore.QRect(325, 180, 100, 30))
        self.cast_btn.setObjectName("cast_btn")

        self.cast_btn.clicked.connect(self.call_it)
        
        self.frame = QtWidgets.QFrame(self.mainframe)
        self.frame.setGeometry(QtCore.QRect(0, 0, WIDTH, 150))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setText("")
        self.textEdit.setGeometry(QtCore.QRect(0, 0, WIDTH, 150))
        self.textEdit.setStyleSheet("background-color:rgb(236, 236, 236)")
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        
        
        self.item_selector = QtWidgets.QComboBox(self.mainframe)
        self.item_selector.setGeometry(QtCore.QRect(20, 180, 110, 30))
        self.item_selector.setObjectName("item_selector")
        self.item_selector.addItem("")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cast_btn.setText(_translate("MainWindow", "Cast"))
        self.item_selector.setItemText(0, _translate("MainWindow", "Wabbajack"))
        self.juice_box.setText(_translate("MainWindow", "Drink juice"))
        self.cast_btn.clicked.connect(self.call_it)
    
    def call_it(self):
        checked = self.juice_box.isChecked()
        if checked:
            self.cast_btn.clicked.connect(self.drink_juice) 
        else:
            self.cast_btn.clicked.connect(self.cast)

    def cast(self):
        self.textEdit.setText(wj.cast())
    def drink_juice(self):
        self.textEdit.setText(wjjuice.drink_juice())
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

