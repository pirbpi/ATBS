from pathlib import Path
import re

p = Path('/Users/rbryan/PycharmProjects/ATBSChapter9/regexFiles/')
textFiles = list(p.glob('*.txt'))
print(textFiles)
userRegex = input('Enter your desired RegEx:\n') # Ask user for regex to search for
compiledRegex = re.compile(userRegex)  # Compile user's regex
matchedRegex = {}

for currentFile in range(len(textFiles)):
    openedFile = open(textFiles[currentFile])
    fileContent = openedFile.read()
    matchedRegex[textFiles[currentFile]] = (compiledRegex.findall(fileContent))
    openedFile.close()
for i in matchedRegex.keys():
    print(matchedRegex[i])
