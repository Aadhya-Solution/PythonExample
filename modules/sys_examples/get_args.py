import sys

print(sys.argv) # List len --->1 that means its not having any args
def verify_inputs(value):
    try:
        if type(eval(value)) in [int , float]:
            return True
        else:
            return False
    except (NameError,Exception):
        print("Inpvalid Data type...!!")
        return False
try:
    if len(sys.argv)>1:
        if sys.argv[1] == 'add':
            value = sys.argv[2]
            if verify_inputs(value):
                a = int(sys.argv[2])
            value = sys.argv[3]
            if verify_inputs(value):
                b = int(sys.argv[3])
                print("{}+{}={}".format(a,b,a+b))
        if sys.argv[1] == 'sub':
            a = int(sys.argv[2])
            b = int(sys.argv[3])
            print("{}-{}={}".format(a, b, a - b))
except IndexError:
    print("Provide proper arguments...!!")


python get_arg_oper.py add 45 56
