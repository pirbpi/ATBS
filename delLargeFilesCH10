#! python3

import os, pprint

def findLargeFiles(folder):
    largeFileList = []
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            fileSize = os.path.getsize(os.path.join(folder, filename))
            if fileSize > 100000:
                p = os.path.join(foldername,filename)
                largeFileList.append(p)
            else:
                continue
    pprint.pprint(largeFileList)

findLargeFiles('/home/rich/Desktop/backupImages/')
