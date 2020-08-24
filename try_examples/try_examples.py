try:
    d={}
    print(d['name'])
    l=[1,3,4]
    print(l[2])
    print(a)
    a=10
except (NameError,ZeroDivisionError) as ex:
    print("I got Name Error excetion {}".format(ex))
    print("Provide proper number")
except IndexError:
    print("No element in the list")
except:
    print("This is genertic")

"""
Type1:
     try:
        stmt1
        stm2
        stm3
    except:
        exceptyion block
Type 2:
    try:
        stm1
        stm2
    except excep:
        exp block 
Type3: 
     try:
        stm1
        stm2
    except (excep1,excp2..):
        exp block 
  
type4:
    try:
       stm1
       stm2
       stm3
    except exp1:
         exp1 Block 
    except exp2:
        exp2 Block
    except exp3:
        exp3 Block 
             
Type5:
     try:
        stm1
        stm2
    except (excep1,excp2..):
        exp block 
    except exp3:
         exp1 Block 
    except exp4:
        exp2 Block
Type5:
     try:
        stm1
        stm2
    except (excep1,excp2..):
        exp block 
    except exp3:
         exp1 Block 
    except exp4:
        exp2 Block
    except:
        Generic Block
        
tYPE 6:
    try:
        try Block 
    except:
        excption Block 
    else:
        else block 
        
tYPE 6:
    try:
        try Block 
    except:
        excption Block 
    finally:
        else block 
        
type7:
    try:
        try Block 
    except:
        excption Block 
    else:
        else block 
    finally:
        Finally Block 
        
        
"""