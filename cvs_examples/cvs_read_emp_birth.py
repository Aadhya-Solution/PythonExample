import csv

with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print row
            line_count += 1
        else:
            print('\t{} works in \
                  the {} department,\
                   and was born in {}.'.format(row[0],row[1],row[2]))
            line_count += 1
    print('Processed {} lines.'.format(line_count))