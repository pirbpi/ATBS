#! python3
# From command line, choose row to insert # of blank rows and specify filename to modify.

import sys, openpyxl

rowN = int(sys.argv[1]) # What row to insert Blank rows into
blanksM = int(sys.argv[2]) # How many blank rows to enter
fileName = sys.argv[3] # Filename to read & modify

wb = openpyxl.load_workbook(fileName) # Open the spreadsheet
sheet = wb.active

for row in range(rowN, rowN+blanksM):
    sheet.insert_rows(row)
    
wb.save('editedMultiplyTable.xlsx') # Save the workbook into a new file.
