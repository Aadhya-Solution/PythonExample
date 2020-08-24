import pyPdf
import abc
import os
filename="C:\Users\PShashik\Documents\CNSSI_4009.pdf"
'''
pdf = pyPdf.PdfFileReader(open(filename, "rb"))
for page in pdf.pages:
    print page.extractText()


fd=pyPdf.PdfFileReader(open(filename, "rb"))
for line in fd.pages:
    try:
        print "===>",line.extractText()
    except:
        pass



from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
password='test'
# Open a PDF document.
fp = open(filename, 'rb')
parser = PDFParser(fp)
document = PDFDocument(parser, password)

print "==",dir(document)
# Get the outlines of the document.
for (level,title,dest,a,se) in outlines:
    print (level, title)
    
'''

import os
import glob
import pyPdf
#
#parent = "C:/Users/victoryee/Google Drive/Projects/extract-pdf-text"
#os.chdir(parent)
#filename = os.path.abspath('naacl06-shinyama.pdf')

def getPDFContent(path):
    content = ""
    # Load PDF into pyPDF
    pdf = pyPdf.PdfFileReader(file(path, "rb"))
    # Iterate pages
    for i in range(1, pdf.getNumPages()):
        # Extract text from page and add to content
        content = pdf.getPage(i).extractText() + "/n"
        content = content.encode('ascii', errors='ignore')
        if i==4:
            print content
            break
                
    # Collapse whitespace
    content = " ".join(content.replace(u"/xa0", " ").strip().split())
    
    return content

# print getPDFContent(filename).encode("ascii", "ignore")
#etPDFContent(filename).encode("ascii", "ignore")
txt=getPDFContent(filename).encode("ascii", "xmlcharrefreplace")
print "*"*40
for line in txt:
    print line