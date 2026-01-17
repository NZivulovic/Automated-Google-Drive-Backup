# Automated Google Drive Backup

## Install
Py7zr 1.1.0:
```
$ pip install py7zr
```
Google:
```
$ pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

## How To Use 
1. Read Quickstart:
  - https://developers.google.com/workspace/drive/labels/quickstart/python
2. File to Edit:
  - [main.py](main.py)

 **<h3>3. edit main.py</h3>** 
  - Own Folders / Files you want to Compile to 7zip.
  ###
  ```
   BACKUP_FILES = [
      r'C:\Users\nikol\Desktop\bewerbungsUnterlagen',
      r'C:\Users\nikol\Desktop\Excel Sheets',
      r'C:\Users\nikol\Desktop\Notizen'
  ]
  ```
  - Target Folder ID to Upload to in Google Drive > right click Folder in Google Drive
  ###
  ```
  TARGET_FOLDER_ID = '1vN5kTW8FX8F_cOl6BjqmuFbbRhUeCR9a'
  ```
  
## APIs / Libraries Used

- Google Drive API
  - https://developers.google.com/workspace/drive/api/guides/about-sdk

7zip compiler:
- py7zr 1.1.0  
  - https://pypi.org/project/py7zr/
  - https://github.com/miurahr/py7zr
