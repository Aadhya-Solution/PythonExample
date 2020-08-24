import xlwt
#----------------------------------------------------------------------
def main():
    """"""
    book = xlwt.Workbook()
    sheet1 = book.add_sheet("PySheet1")
    cols = ["Name", "Age", "Loc", "Cont", "Address"]
    r_1=sheet1.row(0)
    for num in range(5):
        r_1.write(num,cols[num])
    for num in range(1,5):
        row = sheet1.row(num)
        for colNum, col in enumerate(cols):
            value = "Test_Row %s, Col %s"%(num, col)
            print(colNum,'==',value)
            row.write(colNum, value)

    book.save("test44.xls")

#----------------------------------------------------------------------
print('+++',__file__)
print("---",__name__)
if __name__ == "__main__":
    main()
