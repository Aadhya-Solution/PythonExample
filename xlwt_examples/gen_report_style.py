'''
import xlwt
book = xlwt.Workbook()
value = "This is a styled sheet!"
sheet = book.add_sheet("ABC")
style = 'pattern: pattern solid, fore_colour red;'
r=sheet.row(0)
r.write(0, value, xlwt.Style.easyxf(style))
book.save("Added.xls")

import xlwt
from datetime import date
b = xlwt.Workbook()
sheet1 = b.add_sheet("Added Std")
value = date(2009,3,18)
fmt = xlwt.Style.easyxf("""
    font: name Arial;
    borders: left thick, right thick,
    top thin, bottom thick;
    pattern: pattern solid, fore_colour red;
    """, num_format_str='YYYY-MM-DD')
sheet1.write(6,1,value, fmt)
b.save("std_date_fnt.xls")

'''

import xlwt

