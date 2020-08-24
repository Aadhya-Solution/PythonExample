import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='test_todays_log.log',
                    filemode='w')
n1=input("Enter n:")
logging.info("Valaue:"+str(n1))
for n in range(1,n1+1):
   p=n
   sn=str(n)
   logging.info(sn)
   for i in range(n-1,0,-1):
      p=p*i
      sn=sn+"x"+str(i)
   print("Fact(%d)=%s=%d"%(n,sn,p))
   logging.error("Fact(%d)=%s=%d"%(n,sn,p))

a,b=input('A and B:')
try:
   c=a/b
   print("%s/%s=%s"%(a,b,c))
except ZeroDivisionError as e:
   logging.error(e)