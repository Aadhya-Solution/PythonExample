
>>> while 1 print ’Hello world’
File "<stdin>", line 1
while 1 print ’Hello world’
ˆ
SyntaxError: invalid syntax

>>> 10 * (1/0)
Traceback (innermost last):
File "<stdin>", line 1
ZeroDivisionError: integer division or modulo

>>> 4 + spam*3
Traceback (innermost last):
File "<stdin>", line 1
NameError: spam

>>> ’2’ + 2
Traceback (innermost last):
File "<stdin>", line 1
TypeError: illegal argument type for built-in operation



while 1:
    try:
        x = int(raw_input("Please enter a number: "))
        break
    except ValueError:
        print "Oops! That was no valid number. Try again..."
