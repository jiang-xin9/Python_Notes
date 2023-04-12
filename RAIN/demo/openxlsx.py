import os

import pytest
import xlrd
from openpyxl import load_workbook


class open:
    def openxlsx(self,row=1,col=0):
        wb= xlrd.open_workbook('testcases.xlsx')
        ws = wb.active
        wa=ws.rows
        list=[]
        for i in wa:
            row=row+1
            for j in range(10):
                 col=col+1
                 wk = ws.cell(row, col).value
                 list.append(wk)
        return list

    @pytest.mark.parametrize('args',openxlsx())
    def test_1(self,args):
        print(args)

if __name__ == '__main__':
    pytest.main(['-vs'])