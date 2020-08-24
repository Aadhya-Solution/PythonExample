Exception Errors

IOError
If the file cannot be opened.

ImportError
If python cannot find the module

ValueError
Raised when a built-in operation or function receives
an argument that has the right type but an inappropriate value

KeyboardInterrupt
Raised when the user hits the interrupt key (normally Control-C or Delete)

EOFError
Raised when one of the built-in functions (input() or raw_input()) hits an
end-of-file condition (EOF) without reading any data


Exception Errors Examples
except IOError:
    print('An error occurred trying to read the file.')

except ValueError:
    print('Non-numeric data found in the file.')

except ImportError:
    print "NO module found"

except EOFError:
    print('Why did you do an EOF on me?')

except KeyboardInterrupt:
    print('You cancelled the operation.')

except:
    print('An error occurred.')
    
    
    
Exception
                              Base class for all exceptions
StopIteration               Raised when the next() method of an iterator does not point to any object.
SystemExit                  Raised by the sys.exit() function.
StandardError               Base class for all built-in exceptions except StopIteration and SystemExit.
ArithmeticError             Base class for all errors that occur for numeric calculation.
OverflowError               Raised when a calculation exceeds maximum limit for a numeric type.
FloatingPointError         Raised when a floating point calculation fails.
ZeroDivisonError           Raised when division or modulo by zero takes place for all numeric types.
AssertionError              Raised in case of failure of the Assert statement.
AttributeError              Raised in case of failure of attribute reference or assig nment.
EOFError                    Raised when there is no input from either the raw_input() or input() function and the
                            end of file is reached.
ImportError                 Raised when an import statement fails.
KeyboardInterrupt           Raised when the user interrupts prog ram execution, usually by pressing Ctrl+c.
LookupError                 Base class for all lookup errors.
IndexError                  Raised when an index is not found in a sequence.
KeyError                    Raised when the specified key is not found in the dictionary.
NameError                   Raised when an identifier is not found in the local or g lobal namespace.
UnboundLocalError           Raised when trying to access a local variable in a function or method but no value
                            has been assig ned to it.
EnvironmentError            Base class for all exceptions that occur outside the Python environment.
IOError                     Raised when an input/ output operation fails, such as the print statement or the
                            open() function when trying to open a file that does not exist.
OSError                     Raised for operating system-related errors.
SyntaxError                 Raised when there is an error in Python syntax.
IndentationError            Raised when indentation is not specified properly.
SystemError                 Raised when the interpreter finds an internal problem, but when this error is
                            encountered the Python interpreter does not exit.
SystemExit                  Raised when Python interpreter is quit by using the sys.exit() function. If not handled
                            in the code, causes the interpreter to exit.
TypeError                   Raised when an operation or function is attempted that is invalid for the specified
data type.
ValueError                  Raised when the built-in function for a data type has the valid type of arg uments, but
                            the arg uments have invalid values specified.
RuntimeError                Raised when a g enerated error does not fall into any categ ory.
NotImplementedError         Raised when an abstract method that needs to be implemented in an inherited class
                            is not actually implementedh