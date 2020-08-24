import pdb
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
    filename='add_num/add_num.log',
    filemode='w')

n=input("Enter N:")
if n==0:
    logging.warning("Given Number is 0")
logging.info("N:{}".format(n))
c=0
for i in range(n):
    c=c+i
    logging.info("i:{}--c:{}".format(i, c))

logging.info("C:{}".format(c))
print("Sum:",c)