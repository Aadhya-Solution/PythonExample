def varify_num(num):
   if type(num) in [int,float]:
      return True
   else:
      return False

def get_value(st):
   st1="Enter %s value: "%(st)
   while True:
      number1 = input(st1)
      try:
         number1=float(number1)
         p=varify_num(number1)
         print("==>{}".format(p))
         if p:
            return number1
      except ValueError:
         print("Got error")

while 1:
   n1=get_value('numerator')
   n2=get_value('denominater')
   try:
      result = n1 / n2
# float raises a ValueError exception   
   except ValueError:
      print("You must enter two numbers")
   except ZeroDivisionError:
      print("Attempted to divide by zero")
   else:
      print("Came to else block")
      print("%.3f / %.3f = %.3f" % ( n1, n2, result ))
      break