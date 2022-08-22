from fpdf import FPDF
import subprocess

font_path = './font/unifont/'

pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()

fecha="AYSAM"

# add font
pdf.add_font('Simsun', '', font_path + 'SIMSUN.ttf', uni=True)

pdf.set_margins(0, 0, 0)

pdf.set_font('Arial', '', 7)
pdf.cell(166)
pdf.cell(0, 0, 'Reporte: DTECHR_0015', 0)

pdf.image('img/descarga-removebg-preview.png', 10, 10, 25)

pdf.set_font('Arial', 'B', 16)
pdf.set_text_color(18, 179, 179)
pdf.ln(15)
pdf.cell(65)
pdf.cell(0, 0, 'SOLICITUD DE VACACIONES', 0)

pdf.set_font('Arial', '', 8)
pdf.set_text_color(0, 0, 0)
pdf.ln(12)
pdf.cell(10)
pdf.cell(0, 0, 'Gerencia de Recursos', 0)
pdf.ln(3)
pdf.cell(17)
pdf.cell(0, 0, 'Humanos', 0)

pdf.set_font('Arial', '', 12)
pdf.ln(-4)
pdf.cell(160)
pdf.cell(0, 0, 'AYSAM /IE.02/PO.04/a', 0)






pdf.output('prueba222.pdf', 'F')