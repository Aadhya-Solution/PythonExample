import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='bkp.log',
                    filemode='w')
for i in range(10):
    logging.info("Number:%s"%(str(i)))
try:
    1/0
except:
    logging.error("This is error",exc_info=True)