# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arquivocode.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(795, 427)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(270, 10, 211, 33))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pbAdd = QtWidgets.QPushButton(self.frame)
        self.pbAdd.setGeometry(QtCore.QRect(90, 260, 271, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pbAdd.setFont(font)
        self.pbAdd.setStyleSheet("")
        self.pbAdd.setObjectName("pbAdd")
        self.pbCalcular = QtWidgets.QPushButton(self.frame)
        self.pbCalcular.setGeometry(QtCore.QRect(410, 260, 271, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pbCalcular.setFont(font)
        self.pbCalcular.setStyleSheet("background-color: rgb(255, 124, 84);")
        self.pbCalcular.setObjectName("pbCalcular")
        self.lResultado = QtWidgets.QLabel(self.frame)
        self.lResultado.setGeometry(QtCore.QRect(30, 40, 47, 191))
        self.lResultado.setText("")
        self.lResultado.setObjectName("lResultado")
        self.leHorario = QtWidgets.QLineEdit(self.frame)
        self.leHorario.setGeometry(QtCore.QRect(270, 150, 211, 31))
        self.leHorario.setObjectName("leHorario")
        self.lResultado_2 = QtWidgets.QLabel(self.frame)
        self.lResultado_2.setGeometry(QtCore.QRect(616, 30, 141, 61))
        self.lResultado_2.setText("")
        self.lResultado_2.setObjectName("lResultado_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(340, 110, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 795, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Adicional Noturno"))
        self.pbAdd.setText(_translate("MainWindow", "Adicionar"))
        self.pbCalcular.setText(_translate("MainWindow", "Calcular"))
        self.label.setText(_translate("MainWindow", "Horário"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
