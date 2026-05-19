from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from pathlib import Path

# Authenticate and create the PyDrive client.
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

# Specify the folder path.
folder_path = Path('C:\\Users\\Willi\\Desktop\\CODE\\Python\\Youtube Music Scraper\\music')

# Loop through each file in the folder and upload it to Google Drive.
for file_path in folder_path.iterdir():
    if file_path.is_file():
        # Create a GoogleDrive file object with the desired parent folder ID.
        file_to_upload = drive.CreateFile({'parents': [{'id': '1YPUOZR01CqbM0tv3sMiDb4MCYg8Wk-jI'}], 'title': file_path.name})
        
        # Set the content of the file.
        file_to_upload.SetContentFile(str(file_path))
        
        # Upload the file to Google Drive.
        file_to_upload.Upload()
