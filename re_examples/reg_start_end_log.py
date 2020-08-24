import re

reg_start=re.compile(r'\s*(.*)\s*-\s*__main__\s*-\s*INFO\s*-\s*::====================::Starting\s*Scheduler\s*::====================::$')
reg_end=re.compile(r'\s*(.*)\s*-\s*__main__\s*-\s*INFO\s*-\s*::====================::Shuting\s*Down\s*Scheduler\s*::====================::$')

def get_start_end(fileName):
    timeDict={}
    pair_count=0
    unpair_count=0
    fd=open(fileName,'r')
    start_flag=False
    end_flag=False
    for eachline in fd.readlines():
        start=reg_start.search(eachline)
        end=reg_end.search(eachline)
        if start:
            start_flag=True
            s_time=start.group(1)
            #print "Start:",start.group(1)
        if end:
            end_flag=True
            e_time=end.group(1)
            #print "End:",end.group(1)
        if start_flag and end_flag:
            print "Start:%s End:%s"%(s_time,e_time)
            start_flag,end_flag=False,False
            pair_count=pair_count+1
        else:
            unpair_count=unpair_count+1
    print "Pair:",pair_count
    print "UnPair:",unpair_count

    return timeDict


get_start_end('scheduler.log')