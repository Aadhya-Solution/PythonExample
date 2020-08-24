import xlrd

def get_data_from_file(file_name,start_row,end_row):
    b=xlrd.open_workbook(file_name)
    sh=b.sheet_by_index(0)
    l=[]
    for r in range(sh.nrows):
         if r in [3,4,5,7]:
            continue
         temp=[]
         for c in range(sh.ncols):
             if r>=start_row and r<=end_row:
                  temp.append((sh.cell_value(r,c)))
         l.append(temp)
    return l

data= get_data_from_file("sample.xls")
for i in data:
    print(i)