'''
Map using lambda function

'''

Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)
print Fahrenheit
C = map(lambda x: (float(5)/9)*(x-32), Fahrenheit)

print "Convertion of Celsius:",C
