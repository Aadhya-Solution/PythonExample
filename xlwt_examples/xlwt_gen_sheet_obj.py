import xlwt

b=xlwt.Workbook()
s=b.add_sheet("ABC")
s.write(1,3,"Raghu") # R,C, Data
b.save("Sample.xls")
