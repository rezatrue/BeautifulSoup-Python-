import xlwt
from datetime import datetime

class WriteXls:
    list = []

    def __init__(self, list):
        self.list = list
        pass

    def write_file(self):
        # Create a new workbook
        workbook = xlwt.Workbook()
        # Add a new sheet to the workbook
        sheet = workbook.add_sheet('Sheet1')

        col_num = 0
        for key in self.list[0].keys():
            print(key)
            sheet.write(0, col_num, key)
            col_num += 1

        list_len = len(self.list)
        row_num = 0
        while(True):
            if(list_len < row_num):
                break
            else:
                col_num = 0
                for value in self.list[row_num].values():
                    print(value)
                    sheet.write(row_num + 1, col_num, value)
                    col_num += 1
                row_num += 1
        workbook.save('data.xls')
        pass
