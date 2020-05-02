#!/usr/bin/python
from datetime import date, datetime
from horariot import get_adicional, get_total, write_banco, convert_pdf
from arquivocode import *
from pymsgbox import alert

lista = list()
      
def a(ui):
    
    try:

        testando = ui.leHorario.text().split(':')

        nHour = int(testando[0])
        nMinute = int(testando[1])

        if nHour >= 24 or nHour < 0:                
            raise
        if nMinute > 59 or nMinute < 0:
            raise

        lista.append(ui.leHorario.text())
        ui.label_3.setText(ui.label_3.text() + "\n" + ui.leHorario.text())
        ui.leHorario.setText('')

    except Exception:
        alert(text='Digite um Horario Válido', title='ERRO!', button='OK')  
        ui.leHorario.setText('')


def adicionar(ui, b):
    if b:
        a(ui)
    else:
        pass
    ui.pbAdd.clicked.connect(a)


def calcular(ui):
    
  
    def b():
        nome_Funcionario = ui.leFuncionario.text()
        numDate = date(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)
        weekday_name = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]
        wkday = numDate.weekday()

        try:
            
            if lista:
                total = get_total(lista)
                write_banco(f'{nome_Funcionario}  |  {numDate.strftime("%d/%m/%Y")} {weekday_name[wkday]}  |  Adicional Noturno: {total}')
                lista.clear()
                ui.lResultado2.setText(f'{nome_Funcionario}  |  {numDate.strftime("%d/%m/%Y")} {weekday_name[wkday]}  |  Adicional Noturno: {total}')
                ui.leFuncionario.setText('')     
                ui.label_3.setText('')
                
            else:
                raise
            
        except Exception:
            alert(text='Nada para calcular', title="ERRO", button="OK")

    ui.pbCalcular.clicked.connect(b)


def remover(ui):

    def sla():
        try:
            lista.pop()
            ui.label_3.setText('')

            for i in lista:
                ui.label_3.setText('\n' +i + '\n')  

        except Exception:
            alert(text='Não há nada para remover', title='Erro', button='OK')
    ui.pbRemover.clicked.connect(sla)


def imprimir(ui):

    def c():
        convert_pdf()

    ui.botao.clicked.connect(c)


def get_Ui():
    return ui

    
def get_string(tecla):
        key = tecla
        
        if key == 48:
            return "0"

        elif key == 49:
            return "1"
        
        elif key == 50:
            return "2"

        elif key == 51:
            return "3"

        elif key == 52:
            return "4"

        elif key == 53:
            return "5"

        elif key == 54:
            return "6"

        elif key == 55:
            return "7"

        elif key == 56:
            return "8"
            
        elif key == 57:
            return "9"
        
        elif key == 58:
            return ":"

        else:
            return ""
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    adicionar(ui, False)
    calcular(ui)
    imprimir(ui)
    remover(ui)
    sys.exit(app.exec_())