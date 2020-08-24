import logging
import time
import os

class GenLog:
    def __init__(self):
        path=self.get_abs_path()
        folder_name = time.ctime()
        folder_name_path = os.path.join(path,folder_name)
        self.create_folder(folder_name_path)
        # home/shashi/Sepot 12../xyz.py.log
        file_log = os.path.join(folder_name_path,"{}.log".format(__file__))
        logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename=file_log,
                    filemode='w')

    def create_folder(self,folder_path):
        return os.mkdir(folder_path)

    def get_abs_path(self):
        return os.getcwd()

    def write_log(self,desc):
        logging.info(desc)


if __name__ == '__main__':
    log=GenLog()
    log.write_log("Hi")
    for i in range(10):
        logging.info(str(i))