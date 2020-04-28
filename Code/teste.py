#!/usr/bin/python
from datetime import date, datetime
from horariot import get_adicional, get_total, write_banco, convert_pdf
from arquivocode import *

lista = list()

def adicionar(ui):
    

    def a():
        lista.append(ui.leHorario.text())
        print(ui.leHorario.text())
        ui.leHorario.setText('')

    ui.pbAdd.clicked.connect(a)

def calcular(ui):
    def b():
        string = ''
        for i in lista:
            string += f'{i}\n\n'
        print(string)
        ui.lResultado.setText(string)

        numDate = date(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)
        weekday_name = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]
        wkday = numDate.weekday()
        total = get_total(lista)
        print(f'{numDate.strftime("%d/%m/%Y")} {weekday_name[wkday]} | Adicional Noturno: {total}')
        write_banco(f'{numDate.strftime("%d/%m/%Y")} {weekday_name[wkday]} | Adicional Noturno: {total}')
        #convert_pdf()
    
    ui.pbCalcular.clicked.connect(b)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    adicionar(ui)
    calcular(ui)
    sys.exit(app.exec_())


"""


numDate = date(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)

weekday_name = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]
wkday = numDate.weekday()

total = get_total()

print(f'{numDate.strftime("%d/%m/%Y")} {weekday_name[wkday]} | Adicional Noturno: {total}')

write_banco(f'{numDate.strftime("%d/%m/%Y")} {weekday_name[wkday]} | Adicional Noturno: {total}')

convert_pdf()


"""
