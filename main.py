import os
import datetime
import time

from bundler7zip import create7zipArchive
from uploader import uploadFile

timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

BACKUP_FILES = [
    r'C:\Users\nikol\Desktop\bewerbungsUnterlagen',
    r'C:\Users\nikol\Desktop\Excel Sheets',
    r'C:\Users\nikol\Desktop\Notizen'
]

ZIP_NAME = 'daily_backup_' + timestamp + '.7z'

TARGET_FOLDER_ID = '1vN5kTW8FX8F_cOl6BjqmuFbbRhUeCR9a'

create7zipArchive(ZIP_NAME, BACKUP_FILES)

if os.path.exists(ZIP_NAME):
    uploadFile(ZIP_NAME, TARGET_FOLDER_ID)
    print('Backup finished')

    time.sleep(1)

    os.remove(ZIP_NAME)
    print('Local Backup Deleted')

else:
    print('ZIP Creation failed, skipping upload')