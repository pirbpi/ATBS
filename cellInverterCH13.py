#! python3
# cellInverter.py inverts the row and column of the cells in the spreadsheet

import openpyxl

wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb.active
rowMatrix = []  # Create an empty list

for row in range(sheet.max_row):  # For 'row' in range 0 to the last row with data
    rowMatrix.append([])  # Create an empty sublist inside the list
    for cellObj in list(sheet.rows)[row]:  # For each cell in the current row
        rowMatrix[row].append(cellObj.value)  # Add the cell to the sub-list


print(rowMatrix)
