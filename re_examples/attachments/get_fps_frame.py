import re
import os

def get_frame_fps(fileName):
    pat = r".*\s*total\s+frame\=(\d+)\s*fps\=([\d\.]+)"
    fd=open(fileName,'r')
    l=fd.readlines()
    data_dict ={}
    for i in l:
        m=re.search(pat,i)
        if m:
            frame=m.group(1)
            fps=m.group(2)
            data_dict.update({'frame':frame,'fps':fps})

    return data_dict

def report(data):
    line="-"*30
    print line
    print "Frame     FPS"
    print line
    print "{}      {}".format(data['frame'],data['fps'])
    print line

if __name__ == '__main__':
    fileName="face_with_detect_json.txt"
    data= get_frame_fps(fileName)
    report(data)