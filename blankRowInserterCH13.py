#! python3

import sys, openpyxl

rowN = int(sys.argv[1])
blanksM = int(sys.argv[2])
fileName = sys.argv[3]

wb = openpyxl.load_workbook(fileName)
sheet = wb.active

for i in range(0, rowN-1):
    for cellObj in list(sheet.rows)[i]:
        print(cellObj.coordinate)


'''
for rowNum in range(1, rowN):
    for col in range(1, sheet.max_column):
        print(sheet.cell(row=rowNum,column=col).coordinate)
'''
