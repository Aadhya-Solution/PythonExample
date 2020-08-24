try:
    a=input("Enter A:")
    b=input("Enter B:")
    c=int(a)+int(b)
except:
    print("Provide Peropewr Values")
finally:
    print("Value is {}".format(c))