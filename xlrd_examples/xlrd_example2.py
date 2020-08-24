import xlrd

path = 'std.xls'

workbook = xlrd.open_workbook(path)
worksheet = workbook.sheet_by_index(0)

# Change this depending on how many header rows are present
# Set to 0 if you want to include the header data.
offset = 0

rows = []
for i, row in enumerate(range(worksheet.nrows)):
    if i <= offset:  # (Optionally) skip headers
        continue
    r = []
    for j, col in enumerate(range(worksheet.ncols)):
        r.append(worksheet.cell_value(i, j))
    rows.append(r)

print(rows)
print('Got %d rows' % (len(rows) - offset))
print("===>",rows[1])  # Print column headings
print("==>",rows[offset])  # Print first data row sample