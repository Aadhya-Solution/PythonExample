import time

def display_formate(date):
    print "+%30s+"%("-"*50)
    print "+%10s%10s%10s+"%(''*10,'System Date',''*10)
    print "+%30s+"%("-"*50)
    print "+%10s+"%(date)
    print "+%30s+"%("-"*50)

def display_sys_date():
    while True:
        p=time.ctime()
        display_formate(p)
        time.sleep(10)

if __name__ == '__main__':
    display_sys_date()