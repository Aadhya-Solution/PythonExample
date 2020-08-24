from pyPdf import PdfFileReader

path='C:\Users\PShashik\Documents\CNSSI_4009.pdf'
pdf_toread = PdfFileReader(path)

# 1 is the number of the page
page_one = pdf_toread.getPage(4)

# This will dump the content (unicode string)
# According to the doc, the formatting is dependent on the
# structure of the document
print page_one.extractText()