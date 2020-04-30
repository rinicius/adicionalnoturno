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
        MainWindow.resize(932, 556)
        MainWindow.setMinimumSize(QtCore.QSize(932, 556))
        MainWindow.setStyleSheet("background: #fff;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(260, 30, 411, 51))
        font = QtGui.QFont()
        font.setFamily("Times, Times New Roman, serif")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(62)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font-family: \"Times, Times New Roman, serif\";\n"
"font-weight: 500;\n"
"font-variant: small-caps;\n"
"font-size: 36pt;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.pbAdd = QtWidgets.QPushButton(self.frame)
        self.pbAdd.setGeometry(QtCore.QRect(160, 320, 271, 71))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pbAdd.setFont(font)
        self.pbAdd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pbAdd.setStyleSheet("#pbAdd {\n"
"color: #494949 !important;\n"
"text-transform: uppercase;\n"
"text-decoration: none;\n"
"background: #ffffff;\n"
"padding: 20px;\n"
"border: 4px solid #494949 !important;\n"
"}\n"
"\n"
"#pbAdd:hover {\n"
"color: #ffffff !important;\n"
"background: #f6b93b;\n"
"border-color: #f6b93b !important;\n"
"}")
        self.pbAdd.setObjectName("pbAdd")
        self.pbCalcular = QtWidgets.QPushButton(self.frame)
        self.pbCalcular.setGeometry(QtCore.QRect(470, 320, 270, 71))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pbCalcular.setFont(font)
        self.pbCalcular.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pbCalcular.setStyleSheet("#pbCalcular {\n"
"color: #494949 !important;\n"
"text-transform: uppercase;\n"
"text-decoration: none;\n"
"background: #ffffff;\n"
"padding: 20px;\n"
"border: 4px solid #494949 !important;\n"
"}\n"
"\n"
"#pbCalcular:hover {\n"
"color: #ffffff !important;\n"
"background: #0000ff;\n"
"border-color: #0000ff !important;\n"
"}")
        self.pbCalcular.setObjectName("pbCalcular")
        self.leHorario = QtWidgets.QLineEdit(self.frame)
        self.leHorario.setGeometry(QtCore.QRect(340, 240, 211, 31))
        self.leHorario.setObjectName("leHorario")
        self.lResultado2 = QtWidgets.QLabel(self.frame)
        self.lResultado2.setGeometry(QtCore.QRect(127, 460, 671, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.lResultado2.setFont(font)
        self.lResultado2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lResultado2.setStyleSheet("text-align: center;")
        self.lResultado2.setText("")
        self.lResultado2.setAlignment(QtCore.Qt.AlignCenter)
        self.lResultado2.setObjectName("lResultado2")
        self.lNome = QtWidgets.QLabel(self.frame)
        self.lNome.setGeometry(QtCore.QRect(340, 140, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Times, Times New Roman, serif")
        font.setPointSize(12)
        self.lNome.setFont(font)
        self.lNome.setStyleSheet("font-family: \"Times, Times New Roman, serif\";\n"
"font-size: 12pt;\n"
"font-variant: small-caps;\n"
"")
        self.lNome.setObjectName("lNome")
        self.leFuncionario = QtWidgets.QLineEdit(self.frame)
        self.leFuncionario.setGeometry(QtCore.QRect(340, 160, 211, 31))
        self.leFuncionario.setObjectName("leFuncionario")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(110, 445, 701, 71))
        self.textEdit.setObjectName("textEdit")
        self.botao = QtWidgets.QPushButton(self.frame)
        self.botao.setGeometry(QtCore.QRect(833, 0, 81, 61))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.botao.setFont(font)
        self.botao.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao.setAutoFillBackground(False)
        self.botao.setStyleSheet("#botao {\n"
"color: #494949 !important;\n"
"text-transform: uppercase;\n"
"text-decoration: none;\n"
"background: #ffffff;\n"
"padding: 20px;\n"
"border: 4px solid #494949 !important;\n"
"}\n"
"\n"
"#botao:hover {\n"
"color: #ffffff !important;\n"
"background: #ff0000;\n"
"border-color: #ff0000 !important;\n"
"}")
        icon = QtGui.QIcon.fromTheme("pdf")
        self.botao.setIcon(icon)
        self.botao.setObjectName("botao")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(340, 220, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Times, Times New Roman, serif")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("font-family: \"Times, Times New Roman, serif\";\n"
"font-size: 12pt;\n"
"font-variant: small-caps;\n"
"")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 111, 311))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("border-style: dotted;\n"
"border-width: 2px;")
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_3.setIndent(0)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(16, 72, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Times, Times New Roman, serif")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-family: \"Times, Times New Roman, serif\";\n"
"font-size: 9pt;\n"
"font-variant: small-caps;\n"
"font-weight: bold;\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pbRemover = QtWidgets.QPushButton(self.frame)
        self.pbRemover.setGeometry(QtCore.QRect(15, 400, 101, 31))
        self.pbRemover.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pbRemover.setStyleSheet("#pushButton {\n"
"color: #494949 !important;\n"
"text-transform: uppercase;\n"
"text-decoration: none;\n"
"background: #ffffff;\n"
"padding: 20px;\n"
"border: 4px solid #494949 !important;\n"
"}\n"
"\n"
"#pushButton:hover {\n"
"color: #ffffff !important;\n"
"background: #aa0000;\n"
"border-color: #aa0000 !important;\n"
"}")
        self.pbRemover.setObjectName("pbRemover")
        self.label.raise_()
        self.label_2.raise_()
        self.pbAdd.raise_()
        self.pbCalcular.raise_()
        self.leHorario.raise_()
        self.lNome.raise_()
        self.leFuncionario.raise_()
        self.textEdit.raise_()
        self.lResultado2.raise_()
        self.botao.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.pbRemover.raise_()
        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
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
        self.lNome.setText(_translate("MainWindow", "Nome do funcionário"))
        self.botao.setText(_translate("MainWindow", "PDF"))
        self.label.setText(_translate("MainWindow", "Horário"))
        self.label_4.setText(_translate("MainWindow", "Últimas Entradas"))
        self.pbRemover.setText(_translate("MainWindow", "Remover"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
