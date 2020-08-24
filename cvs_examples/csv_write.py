import csv

with open('persons.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',')
    filewriter.writerow(['Name', 'Profession'])
    filewriter.writerow(['Sita', 'Software Developer'])
    filewriter.writerow(['Shiva', 'Software Developer'])
    filewriter.writerow(['Raghu', 'Manager'])