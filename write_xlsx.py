import xlsxwriter
from datetime import datetime

class WriteXlsx:
    list = []

    def __init__(self, list):
        self.list = list
        pass

    def unique_filename(self):
        return str(datetime.now().date()) + '_' + str(datetime.now().time()).replace(':', '.')

    def write_file(self):
        # Create a new workbook

        workbook = xlsxwriter.Workbook('Data_' + self.unique_filename() +'.xlsx')
        # Add a new sheet to the workbook
        worksheet = workbook.add_worksheet('Sheet1')

        col_num = 0
        for key in self.list[0].keys():
            print(key)
            worksheet.write(0, col_num, key)
            col_num += 1

        list_len = len(self.list)
        row_num = 0
        while(True):
            if(list_len <= row_num):
                break
            else:
                col_num = 0
                for value in self.list[row_num].values():
                    if(col_num == 2):
                        value = ', '.join(map(str,value))
                        print(value)
                    else:
                        print(value)
                    worksheet.write(row_num + 1, col_num, value)
                    col_num += 1
            row_num += 1
        workbook.close()
        pass
