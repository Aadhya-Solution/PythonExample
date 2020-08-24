while True:
      p=raw_input("enter value:")
      try:
          t=int(p)
          print "Int:",t
          if type(t) is int:
             break
      except ValueError:
          print "Provide proper Value:"
