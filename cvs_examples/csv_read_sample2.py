import csv

# open file
with open('persons.csv', 'r') as f:
    reader = csv.reader(f,delimiter='|')

    # read file row by row
    for row in reader:
        print row