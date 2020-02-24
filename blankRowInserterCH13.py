#! python3

import sys, openpyxl

rowN = int(sys.argv[1])
blanksM = int(sys.argv[2])
fileName = sys.argv[3]

wb = openpyxl.load_workbook(fileName)
nwb = openpyxl.Workbook()
nwbSheet = wb.active
sheet = wb.active
cellValues = []

for i in range(0, rowN-1):
    for cellObj in list(sheet.rows)[i]:
        nwbSheet[cellObj.coordinate] = cellObj.value
        print(nwbSheet[cellObj.coordinate].value)
        cellValues.append(cellObj.value)

nwb.save('editedMultiplyTable.xlsx')

'''
for rowNum in range(1, rowN):
    for col in range(1, sheet.max_column):
        print(sheet.cell(row=rowNum,column=col).coordinate)
'''
