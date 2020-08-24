import xlwt

b=xlwt.Workbook() # obj Workbook
s=b.add_sheet("Numbers")
c=0
for i in range(10,20):
     r=s.row(c)
     r.write(0,i)
     c=c+1
b.save('number.xlsx')
