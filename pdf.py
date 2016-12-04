# General imports
from __future__ import print_function
from sys import *

# ReportLab imports
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

#############
# VARIABLES #
#############

point = 1

# coordinates
tmhma_y = 7.38
sxoli_y = 10.38
univ_y = 12.66
date_y = 5.86
middle_x = 20

# Test vars
SXOLI = "ΣΧΟΛΗ ΘΕΤΙΚΩΝ ΕΠΙΣΤΗΜΩΝ ΚΑΙ ΚΑΡΓΙΕΡΙΣΤΩΝ ΚΑΙ ΠΑΤΑΤΕΣ"
TMHMA = "ΒΙΟΛΟΓΙΚΟ"
DATE = "31 Μαρτιου 2016"
UNIV = "ΑΡΙΣΤΟΤΕΛΕΙΟ ΠΑΝΕΠΗΣΤΙΜΙΟ ΘΕΣΣΑΛΟΝΙΚΗΣ"

####################
# DEFINE FUNCTIONS #
####################

# split the string to 2 lines if too big (also the take care of the font)
def reshape(word):
  # set font size
  if (len(word) > 50):
    font = 14
  else:
    font = 15

  new_arr = ["", ""]
  
  if (len(word) > 28):
    # splits in spaces
    tmp = word.split(" ")
    i = 0
    # creates first array entry
    new_arr[0] = new_arr[0] + tmp[i]
    i = i + 1
    while ( len(new_arr[0]) < 26):
      new_arr[0] = new_arr[0] + " " + tmp[i]
      i = i + 1
    # creates second array entry
    if (i < len(tmp)):
      new_arr[1] = new_arr[1] + tmp[i]
      i = i + 1
    while(i < len(tmp)):
      new_arr[1] = new_arr[1] + " " + tmp[i]
      i = i + 1
  else:
    # else just copy what you have to first array entry
    new_arr[0] = word

  return new_arr, font

def draw_asset(font, font_size, asset, asset_y, canv):
  canv.setFont(font, font_size * point)
  for line in asset:
    canv.drawCentredString(20 * cm, asset_y * cm, line)
    asset_y = (asset_y * cm - font_size - 2) / cm

def make_pdf_file(output_filename):
  title = output_filename
  font = "Helvetica"
  c = canvas.Canvas(output_filename, pagesize=(26.55 * cm, 18.2 * cm))
  c.setStrokeColorRGB(0,0,0)
  c.setFillColorRGB(0,0,0)

  univ_font = 12
  draw_asset(font, univ_font, new_univ, univ_y, c)

  draw_asset(font, sxoli_font, new_sxoli, sxoli_y, c)

  draw_asset(font, tmhma_font, new_tmhma, tmhma_y, c)

  # Draw date
  c.setFont(font, 12 * point)
  c.drawCentredString(middle_x * cm, date_y * cm, DATE)

  # Draw side
  c.rotate(90)
  c.setFont(font, 11 * point)
  c.drawCentredString(9.1 * cm, -13.65 * cm, side)

  # finalize
  c.showPage()
  c.save()


########
# MAIN #
########

new_sxoli, sxoli_font = reshape(SXOLI)
new_tmhma, tmhma_font = reshape(TMHMA)
new_univ, scrap = reshape(UNIV)

# build the side of the cover
temp = " "
side = DATE + temp + TMHMA
while (len(side) < 80):
  temp = temp + " "
  side = DATE + temp + TMHMA

make_pdf_file("test.pdf")

print ("Wrote", "test")
