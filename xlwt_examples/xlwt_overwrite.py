from xlwt import Workbook

book = Workbook()
sheet1 = book.add_sheet('Sheet 1',cell_overwrite_ok=True)
sheet1.write(0,0,'original')
sheet = book.get_sheet(0)
sheet.write(0,0,'new2')
sheet2 = book.add_sheet('Sheet 2',cell_overwrite_ok=True)
sheet2.write(0,0,'original')
sheet2.write(0,0,'new2')
book.save("test5.xls")