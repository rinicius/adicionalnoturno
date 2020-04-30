#!/usr/bin/python
from datetime import date, datetime
from horariot import get_adicional, get_total, write_banco, convert_pdf
from arquivocode import *
from msvcrt import *
from pymsgbox import *


lista = list()

def adicionar(ui):
    
    def a():

        try:

            testando = ui.leHorario.text().split(':')
            
            nHour = int(testando[0])
            nMinute = int(testando[1])

            if nHour >= 24 or nHour < 0:
                print('1')
                raise 
            if nMinute > 59 or nMinute < 0:
                print('2')
                raise

            lista.append(ui.leHorario.text())
            print(ui.leHorario.text())
            ui.label_3.setText(ui.label_3.text() + "\n" + ui.leHorario.text())
            ui.leHorario.setText('')                

        except Exception:
            alert(text='Digite um Horario Válido', title='ERRO!', button='OK')  
            ui.leHorario.setText('')              
            
    ui.pbAdd.clicked.connect(a)

def calcular(ui):
    
    def b():
        nome_Funcionario = ui.leFuncionario.text()
        # string = ''
        # for i in lista:
        #     string += f'{i}\n\n'
        # ui.lResultado.setText(string)
        numDate = date(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)
        weekday_name = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]
        wkday = numDate.weekday()
        total = get_total(lista)
        write_banco(f'{nome_Funcionario}  |  {numDate.strftime("%d/%m/%Y")} {weekday_name[wkday]}  |  Adicional Noturno: {total}')
        lista.clear()
        ui.lResultado2.setText(f'{nome_Funcionario}  |  {numDate.strftime("%d/%m/%Y")} {weekday_name[wkday]}  |  Adicional Noturno: {total}')
        ui.leFuncionario.setText('')     
        ui.label_3.setText('')           
            
    ui.pbCalcular.clicked.connect(b)

def remover(ui):
    def sla():
        lista.pop()
        ui.label_3.setText('')
        for i in lista:
            ui.label_3.setText('\n' +i + '\n')    
    
    ui.pbRemover.clicked.connect(sla)

def imprimir(ui):
    def c():
        convert_pdf()
    ui.botao.clicked.connect(c)


# def key_pressioned(ui):

#     if 13 in list(msvcrt.getch()):
#         adicionar(ui)
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()    
    adicionar(ui)
    calcular(ui)
    imprimir(ui)
    remover(ui)
    #key_pressioned(ui)
    sys.exit(app.exec_())


"""

import msvcrt

def monitor(key):

    if 13 in key:
        print('Enter')

    else:
        print(key)

for i in range(0, 5):
    monitor(list(msvcrt.getch()))


numDate = date(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)

weekday_name = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]
wkday = numDate.weekday()

total = get_total()

print(f'{numDate.strftime("%d/%m/%Y")} {weekday_name[wkday]} | Adicional Noturno: {total}')

write_banco(f'{numDate.strftime("%d/%m/%Y")} {weekday_name[wkday]} | Adicional Noturno: {total}')

convert_pdf()


"""

# pyuic5 arquivo.ui -o arquivo.py -x