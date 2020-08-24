import csv

with open('file.csv') as fd:
    csvReader = csv.reader(fd)
    print csvReader
    #[[c1,c2,c3],[c1,c2,c3],]
    for row in csvReader:
        print row