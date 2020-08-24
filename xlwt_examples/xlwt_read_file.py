import xlwt
import re
import os
import time

def xl_write(list_line_dict):
    book = xlwt.Workbook()
    print("list_line_dict:",list_line_dict)
    for fileName,value2 in list_line_dict.items():
        sheet1 = book.add_sheet(fileName)
        cols = ["Name", "DOB"]
        row = sheet1.row(0)
        row.write(0,cols[0])
        row.write(1,cols[1])
        cal=1
        print("--->",value2)
        for num in range(len(value2)):
            row = sheet1.row(cal+num)
            value=value2[num]
            print(num,"==>",value)
            row.write(0, str(value['name']))
            row.write(1,str(value['dob']))
    book.save('std_report_xls2.xls')

def machLine(eachline):
    reg_compile=re.compile(r'\s*(\w+)\s*\d+\s*\w+\s*(\d+/\d+/\d+)\s*.*')
    reg_match=reg_compile.search(eachline)
    temp_dict={}
    if reg_match:
        temp_dict.update({'name':reg_match.group(1),'dob':reg_match.group(2)})
        return temp_dict#{'dob': '20/03/2010', 'name': 'Shiva'}

def read_file(fileName):
    fd=open(fileName,'r')
    list_line=[]
    for eachile in fd.readlines():
        getValue=machLine(eachile)
        if getValue:
            list_line.append(getValue)
    return list_line
    #xl_write(list_line)

if __name__ == '__main__':
    dirName='/home/shashi/PycharmProjects/pythonExamples/pythonExamples/std_details'
    folder_path=os.path.join("/home/shashi/PycharmProjects/pythonExamples/pythonExamples",dirName)
    print(folder_path)
    file_list=os.listdir(folder_path)
    print(file_list)
    dict_file={}
    for each_file in file_list:
        each_file_absPath=os.path.join(folder_path,each_file)
        #print each_file_absPath
        eachFileList=read_file(each_file_absPath)
        dict_file.update({os.path.basename(each_file_absPath):eachFileList})
    xl_write(dict_file)


