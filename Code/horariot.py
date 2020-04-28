import datetime
from fpdf import FPDF 

listahorario = list()

def write_banco(frase):
    frase1 = str(frase)
    f = open("Banco/banco.txt", "a")
    f.write(f'{frase1}\n')
    f.close()


def convert_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    pdf.cell(200, 10, txt = "Histórico do Adicional Noturno", ln = 1, align = 'C')
    pdf.cell(200, 20, txt = "", align = 'L') 
    
    f = open("Banco/banco.txt", "r")

    for x in f: 
        pdf.cell(200, 10, txt = x, ln = 1, align = 'L') 

    pdf.output("Historico/historico.pdf") 


def get_adicional(lista):
    
    resultadohora = list()
    resultadomin = list()
    resultado = list()

    horarioAN = [22, 00]

    for i in lista:
        resultadoHour = 0
        
        try:

            horariof = i.split(':')
            horariof = [int(i) for i in horariof]

            if horariof[0] == 0:
                break
            
            resultadoMinute = horariof[1]

        except ValueError:
            print('Insira um horário válido')
            continue
        
        except IndexError:
            print('Insira um horário válido')
            continue


        if horariof[0] > 9 and horariof[0] < 22:
            continue
        else:
            pass

        if horarioAN[0] == horariof[0]:
            resultadoHour = 0
        else:
            if horariof[0] >= 5 and horariof[0] <= 9:
                resultadoHour = 7
            elif horarioAN[0] < horariof[0]:
                resultadoHour = horariof[0] - horarioAN[0]
            else:
                resultadoHour = (horarioAN[0] - horariof[0] - 24) * -1


        resultadohora.append(resultadoHour)
        resultadomin.append(resultadoMinute)

        resultado.append(resultadohora)
        resultado.append(resultadomin)        

    return resultado


def get_total(lista):
    
    resultado = get_adicional(lista)

    total = sum(resultado[1]) + (sum(resultado[0]) * 60)       

    return str(datetime.timedelta(minutes=total))
