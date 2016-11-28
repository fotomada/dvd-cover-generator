from __future__ import print_function
#from sys import argv
from sys import *

from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.utils import simpleSplit

point = 1
inch = 72

SXOLI = "ΤΜΗΜΑ ΗΛΕΚΤΡΟΛΟΓΩΝ ΜΗΧΑΝΙΚΩΝ"
TMHMA = "ΤΜΗΜΑ ΗΛΕΚΤΡΟΛΟΓΩΝ ΜΗΧΑΝΙΚΩΝ"
DATE = "12 Ιουνιου 2039"
UNIV = "ΑΡΙΣΤΟΤΕΛΕΙΟ ΠΑΝΕΠΗΣΤΙΜΙΟ ΘΕΣΣΑΛΟΝΙΚΗΣ"

new_sxoli = ["", ""]

if (len(SXOLI) > 50):
    sxoli_font = 14
else:
    sxoli_font = 15

if (len(SXOLI) > 28):
    tmp = SXOLI.split(" ")
    i = 0
    while ( len(new_sxoli[0]) < 26):
        new_sxoli[0] = new_sxoli[0] + " " + tmp[i]
        i = i + 1
    while(i < len(tmp)):
        new_sxoli[1] = new_sxoli[1] + " " + tmp[i]
        i = i + 1
else:
    new_sxoli[0] = SXOLI

new_tmhma = ["", ""]

if (len(TMHMA) > 50):
    tmhma_font = 14
else:
    tmhma_font = 15

if (len(TMHMA) > 28):
    tmp = TMHMA.split(" ")
    i = 0
    while ( len(new_tmhma[0]) < 26):
        new_tmhma[0] = new_tmhma[0] + " " + tmp[i]
        i = i + 1
    while(i < len(tmp)):
        new_tmhma[1] = new_tmhma[1] + " " + tmp[i]
        i = i + 1
else:
    new_tmhma[0] = TMHMA

new_univ = ["", ""]

if (len(UNIV) > 20):
    tmp = UNIV.split(" ")
    i = 0
    while ( len(new_univ[0]) < 26):
        new_univ[0] = new_univ[0] + " " + tmp[i]
        i = i + 1
    while(i < len(tmp)):
        new_univ[1] = new_univ[1] + " " + tmp[i]
        i = i + 1
else:
    new_univ[0] = UNIV

temp = " "
side = DATE + temp + TMHMA
while (len(side) < 70):
    temp = temp + " "
    side = DATE + temp + TMHMA
        
def make_pdf_file(output_filename):
    title = output_filename
    c = canvas.Canvas(output_filename, pagesize=(26.55 * cm, 18.2 * cm))
    c.setStrokeColorRGB(0,0,0)
    c.setFillColorRGB(0,0,0)

    #University dimentions
    univ_font = 12
    c.setFont("Helvetica", univ_font * point)
    univ_y = 12.66
    for line in new_univ:
        c.drawCentredString(19.9 * cm, univ_y * cm, line)
        univ_y = (univ_y * cm - univ_font - 2) / cm

    c.setFont("Helvetica", sxoli_font * point)
    sxoli_y = 10.38
    for line in new_sxoli:
        c.drawCentredString(19.9 * cm, sxoli_y * cm, line)
        sxoli_y = (sxoli_y * cm - sxoli_font - 2) / cm

    c.setFont("Helvetica", tmhma_font * point)
    tmhma_y = 7.38
    for line in new_tmhma:
        c.drawCentredString(19.9 * cm, tmhma_y * cm, line)
        tmhma_y = (tmhma_y * cm - tmhma_font - 2) / cm

    c.setFont("Helvetica", 12 * point)
    #Date dimentions
    c.drawCentredString(19.9 * cm, 5.86 * cm, "5 Ιουνιου 2007")
    #Shol
    c.rotate(90)
    c.setFont("Helvetica", 11 * point)
    c.drawCentredString(9.1 * cm, -13.65 * cm, side)
    c.showPage()
    c.save()

if __name__ == "__main__":
    make_pdf_file("test.pdf")
print ("Wrote", "test")