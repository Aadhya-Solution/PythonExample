'''
import pdfminer
import slate
filename="C:\Users\PShashik\Documents\CNSSI_4009.pdf"
with open(filename) as f:
    doc = slate.PDF(f)
    
print doc
'''

import os
import glob
from pyPdf import PdfFileReader

path="C:\Users\PShashik\Documents\CNSSI_4009.pdf"
 
filename = os.path.abspath(path)
 
input = PdfFileReader(file(filename, "rb"))
for page in input.pages:
    #for k,v in page.items():
    #    print dir(k),dir(v)
    #    print v
    #    break
    #break
    source = page.extractText().encode('ascii', errors='ignore')
    print source + '\n\n'
    