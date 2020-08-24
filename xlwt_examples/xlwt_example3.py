from datetime import date
import xlwt

#----------------------------------------------------------------------
def main():
    """"""
    book = xlwt.Workbook()
    sheet1 = book.add_sheet("PySheet1")

    cols = ["A", "B", "C", "D", "E"]
    txt = "Row %s, Col %s"

    for num in range(5):
        row = sheet1.row(num)
        for index, col in enumerate(cols):
            value = txt % (num+1, col)
            row.write(index, value)

    value = date(2009,3,18)
    fmt = xlwt.Style.easyxf("""
    font: name Arial;
    borders: left thick, right thick,
    top thin, bottom thick;
    pattern: pattern solid, fore_colour red;
    """, num_format_str='YYYY-MM-DD')
    sheet1.write(6,1,value, fmt)

    book.save("test334.xls")

#----------------------------------------------------------------------
if __name__ == "__main__":
    main()