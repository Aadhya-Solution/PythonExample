import xlwt
import xlrd

workbook = xlrd.open_workbook('std.xls')
sheet = workbook.sheet_by_index(0)
data = [[sheet.cell_value(r, col)
                for col in range(sheet.ncols)]
                    for r in range(1,sheet.nrows)]

for i in data:

    total=eval(i[2])+eval(i[3])+eval(i[4])
    i.append(str(total))
workbook = xlwt.Workbook()
sheet = workbook.add_sheet('test')

print(data)

for r,v in enumerate(data):
    p=1
    for c in v:
        sheet.write(r+1, p, c)
        p=p+1
workbook.save('output2.xls')


# 1. std.txt --> Name,age,loc,dob,cont
#    marks
#    xls -- > Name Age Marks Total Marks Result
# 2. Deive name , Ip
# 3. Interface  up/dow