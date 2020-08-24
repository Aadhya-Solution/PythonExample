import xlwt
#----------------------------------------------------------------------
def main():
    """"""
    book = xlwt.Workbook()
    sheet1 = book.add_sheet("Student Details", cell_overwrite_ok=True)
    cols = ["Name", "Age", "M1", "M2", "M3"]
    for i,v in enumerate(cols):
        row = sheet1.row(0)
        row.write(i,v)
    for num in range(1,3):
        row = sheet1.row(num)
        for index, col in enumerate(cols):
            value=input("%s"%(col))
            row.write(index, value)

    book.save("std.xls")

#----------------------------------------------------------------------
print('+++',__file__)
print("---",__name__)
if __name__ == "__main__":
    main()