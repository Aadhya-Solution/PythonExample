import xlwt

#----------------------------------------------------------------------
def add_sheet(book, name):
    """
    Add a sheet with one line of data
    """
    value = "This sheet is named: %s" % name
    sheet = book.add_sheet(name)
    sheet.write(0,0, value)

#----------------------------------------------------------------------
def add_styled_sheet(book, name):
    """
    Add a sheet with styles
    """
    value = "This is a styled sheet!"
    sheet = book.add_sheet(name)
    style = 'pattern: pattern solid, fore_colour red;'
    sheet.row(0).write(0, value, xlwt.Style.easyxf(style))

#----------------------------------------------------------------------
def main():
    """"""
    book = xlwt.Workbook()
    sheet1 = book.add_sheet("PySheet1")

    cols = ["A", "B", "C", "D", "E"]

    for num in range(1,6):
        row = sheet1.row(num)
        for index, col in enumerate(cols):
            value = "Row %s, Col %s" % (num, col)
            row.write(index, value)

    add_sheet(book, "PySheet2")
    add_styled_sheet(book, "StyledSheet")

    book.save("test444.xls")

#----------------------------------------------------------------------
if __name__ == "__main__":
    main()
