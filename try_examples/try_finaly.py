
def doNotRaiseException():
   try:
      print "In doNotRaiseException"
   finally:
      print "Finally executed in doNotRaiseException"
   print "End of doNotRaiseException"

print "Calling doNotRaiseException"
doNotRaiseException()
