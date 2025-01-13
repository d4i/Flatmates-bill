import os
import webbrowser
from fpdf import FPDF


class PdfReport:
    """
    Creates a pdf file which contains data about the flatmates
    such as their names, their due amount and period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generates(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.image("Files/house.png", w = 30, h = 30)

        pdf.set_font(family='Times', style='B', size=24)
        pdf.cell(w=0, h=50, txt='Flatmates Bill', border=0, ln=1, align='C')

        pdf.set_font(family='Times', style='B', size=16)
        pdf.cell(w=100, h=50, txt='Period:', border=0, align='C')
        pdf.cell(w=150, h=50, txt=bill.period, border=0, ln=1)

        pdf.set_font(family='Times', style='', size=14)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0, align='C')
        pdf.cell(w=100, h=25, txt=flatmate1_pay, border=0, align='', ln=1)

        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0, align='C')
        pdf.cell(w=100, h=25, txt=flatmate2_pay, border=0, align='', ln = 1)

        pdf.cell(w=100, h=25, txt="Total", border=0, align='C')
        pdf.cell(w=100, h=25, txt=str(bill.amount), border=0, align='')

        os.chdir('Files')
        pdf.output(self.filename)

        webbrowser.open(self.filename)
