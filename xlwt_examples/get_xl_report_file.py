import xlwt
def get_data(file_name):
    fd=open(file_name,'r')
    data=[i.split(',') for i in fd.readlines()]
    print(data)
    return data

def xl_report(data):
    wb=xlwt.Workbook()
    sh=wb.add_sheet('Std')
    for r,rv in enumerate(data):
        robj=sh.row(r)
        for c,cv in enumerate(rv):
            robj.write(c,cv.strip())
    wb.save('std_data.xls')
data = get_data('std.txt')
xl_report(data)