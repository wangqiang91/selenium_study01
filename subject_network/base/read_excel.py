import xlrd
import os

subpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
filepath = os.path.join(subpath,'data','datas.xls')

class Get_Excel_Data():
    def __init__(self,path=filepath):
        self.path = path
    def get_excel_sheet(self):
        data = xlrd.open_workbook(self.path).sheet_by_index(0)
        rows = data.nrows
        cols = data.ncols
        list1 = []
        key = data.row_values(0)
        for x in range(1,rows):
            dict1 = {}
            values = data.row_values(x)
            for y in range(cols):
                dict1[key[y]] = values[y]
            list1.append(dict1)
        return list1


if __name__ == '__main__':
    data = Get_Excel_Data()
    res = data.get_excel_sheet()
    print(res)



