import py7zr
import os


def create7zipArchive(outputFileName, paths):

    print(f"Starting compression: {outputFileName}...")
    with py7zr.SevenZipFile(outputFileName, 'w') as archive:
        for path in paths:
            if os.path.exists:
                archive.writeall(path, arcname=os.path.basename(path))
                print(f" - Added: {path}")
            else:
                print(f" ! Warning: Path not found: {path}")
    print("Compression complete.\n")



