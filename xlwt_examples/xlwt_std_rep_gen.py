import xlwt
# Write Program to read a csv file of studnet data and create xls report
# shiva,20,Blore,India, 20000
# Name   Age   City  Nation Salary
# Shiva   20   Blore   India  20000
def get_csv_data(csv_file_name):
   fd=open(csv_file_name, 'r')
   std_list=[]
   for i in fd.readlines():
      data = i.strip().split(',') #[shiva,20,Blore,India, 20000]
      std_list.append(data)
   return std_list #[[shiva,20,Blore,India, 20000],[shiva,20,Blore,India, 20000],[shiva,20,Blore,India, 20000]]

def gen_xl_report(data):
   b=xlwt.Workbook()
   s=b.add_sheet("Std Details")
   r=s.row(0)
   r.write(0,'Name')
   r.write(1,'Age')
   r.write(2, 'City')
   r.write(3, 'Nation')
   r.write(4, 'Salary')

   c=1
   for each_std in data:
      print(each_std)
      r=s.row(c)
      r.write(0,each_std[0])
      r.write(1,each_std[1])
      r.write(2, each_std[2])
      r.write(3, each_std[3])
      r.write(4, each_std[4])
      c=c+1
   b.save("std_complete_details.xls")

data= get_csv_data("std_scv.txt")
gen_xl_report(data)