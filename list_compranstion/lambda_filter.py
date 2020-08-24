'''
Filtering

The function filter(function, list) offers
an elegant way to filter out all
the elements of a list,
for which the function function returns
True.

'''
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='11test.log',
                    filemode='w')
fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x % 2, fib)
logging.info("List is %s"%(fib))
print result
#[1, 1, 3, 5, 13, 21, 55]
result = filter(lambda x: x % 2 == 0, fib)
print result
#[0, 2, 8, 34]
logging.info("Result is %s"%(result))