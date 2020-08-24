from datetime import date
from xlwt import Workbook, XFStyle, Borders, Pattern, Font

fnt = Font()
fnt.name = 'Arial'
borders = Borders()
borders.left = Borders.THICK
borders.right = Borders.THICK
borders.top = Borders.THICK
borders.bottom = Borders.THICK
pattern = Pattern()
pattern.pattern = Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = 0x0D
pattern2 = Pattern()
pattern2.pattern = Pattern.SOLID_PATTERN
pattern2.pattern_fore_colour = 0x0A

style = XFStyle()
style.num_format_str='YYYY-MM-DD'
style.font = fnt
style.borders = borders
style.pattern = pattern

style2=XFStyle()
style2.num_format_str='YYYY-MM-DD'
style2.font = fnt
style2.borders = borders
style2.pattern = pattern2
book = Workbook()
sheet = book.add_sheet('A Date')
for i in range(0,10,2):
    #sheet.write(i,1,date(2016,3,10+i),style)
    sheet.write(i,2,date(2016,3,18),style)
book.save('date222.xls')

