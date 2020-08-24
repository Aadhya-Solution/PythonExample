
for num in range(10,20): #[10,11,12,12,....19]
    for i in range(2,num):
        if num%i == 0:
            #print "Not done:",num
            break
    else:#else for
        print "prim Num",num