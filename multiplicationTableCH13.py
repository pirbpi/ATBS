#! python3
# multiplicationTable - take a cmd line argument and create a multiplication table

import openpyxl, sys
userMultiplication = int(input('Enter number for multiplication table: '))

wb = openpyxl.Workbook()
sheet = wb.active

for i in range(1, userMultiplication + 1):
    sheet.cell(row=1,column=i + 1).value = i
    sheet.cell(row=i + 1, column = 1).value = i
    for j in range(i):
        sheet.cell(row=j+1, column = i+1).value = i * i

wb.save('multiplicationTable.xlsx')
