#! python3

import shutil, os
from pathlib import Path

# TODO: Walk through a folder
def walkFolder(folder):
    folder = os.path.abspath(folder) # Make sure folder is absolute
    backupFolder = '/home/rich/Desktop/backupImages'
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')

        for filename in filenames:
            if filename.endswith('.jpg'):
                if foldername == backupFolder:
                    continue
                shutil.copy(os.path.join(Path(foldername) / filename), backupFolder)



walkFolder('/home/rich/Desktop')
