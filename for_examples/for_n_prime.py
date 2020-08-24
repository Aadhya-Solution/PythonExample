l='''
author:
date:
disc:


'''
# import logging
# logging.basicConfig(format = '[%(asctime)s] [%(levelname)-8s] [%(name)-20s] %(message)s', level = logging.INFO)
# logger = logging.getLogger(__name__)
# logger.info('Loading testbed file: {}'.format(testbed_file))



import logging
logging.basicConfig(filename="test2.log",format="%(asctime)s %(levelname)s %(message)s",
                    filemode = 'w',level=logging.DEBUG)
logging.getLogger()
print(l)
logging.info("Prg for Prime Number")
n1=input("Enter the \
         n1 value:")
n2=input("Enter the n2 value:")
logging.info("Entered Value N1:{}".format(n1))
logging.info("Entered Value N2:{}".format(n2))

for num in range(int(n1),int(n2)):#[10,11,12
    for i in range(2,num): #[2,3,4,...9]
        if num % i == 0:
            logging.error("Not and prime")
            break
    else:
        print("Number is prime",num)
        logging.info("Number is Prime:{}".format(num))