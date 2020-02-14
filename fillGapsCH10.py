#! python3

import os,re

folder = '/users/rbryan/PycharmProjects/ATBSChapter10/gapFolder/'
fileRegex = re.compile('((0|0)?\d\d\d)(.txt)')

# TODO: Create the files to play with:
def createFiles():
    for i in range(1, 50):
        if i < 10:
            newFile = os.open(folder + 'spam00' + str(i) + '.txt', 'w')
        elif i > 9 and i < 100:
            os.open(folder + 'spam0' + str(i) + '.txt', 'w')
        newFile.write('Some text here....')
        newFile.close()

# TODO: Find all files with a given prefix in a single folder(00)
fileList = []
for currentFile in os.listdir(folder):
    mo = fileRegex.search(currentFile)
    if mo == None:
        continue
    fileList.append(currentFile)
    fileList.sort()
print(fileList)

# TODO: Locate any gaps in the numbering
for i in fileList:
    currentFileRegex = re.compile('((0|0)?\d\d\d)(.txt)')
    currentNumber = currentFileRegex.search(i)
    currentNumber.group(1)
    print(currentNumber)
    if currentNumber == '001':
        print('FOUND IT')

# TODO: Rename all the later files to close the gap

