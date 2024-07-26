import os
import pyzipper
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def create_archive(directory, archive_name, password):
    try:
        with pyzipper.AESZipFile(archive_name, 'w', compression=pyzipper.ZIP_DEFLATED) as zf:
            zf.pwd = password.encode('utf-8')
            for foldername, subfolders, filenames in os.walk(directory):
                for filename in filenames:
                    file_path = os.path.join(foldername, filename)
                    arcname = os.path.relpath(file_path, start=directory)
                    print(f"Adding {file_path} as {arcname} to archive")
                    zf.write(file_path, arcname)
        print(f"Archive {archive_name} created successfully with password protection.")
    except Exception as e:
        print(f"Failed to create archive: {e}")

async def upload_files(service_account_file, folder_id, archive_name, chat_id, bot):
    credentials = service_account.Credentials.from_service_account_file(service_account_file, scopes=['https://www.googleapis.com/auth/drive.file'])
    service = build('drive', 'v3', credentials=credentials)
    
    archive_path = archive_name
    file_metadata = {'name': archive_name, 'parents': [folder_id]}
    media = MediaFileUpload(archive_path, resumable=True)
    request = service.files().create(body=file_metadata, media_body=media, fields='id,webViewLink')
    response = None
    
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"Uploaded {int(status.progress() * 100)}%.")

    if response:
        file_id = response.get('id')
        file_link = response.get('webViewLink')
        await bot.send_message(chat_id=chat_id, text=f"File uploaded: {archive_name}\nLink: {file_link}\nPassword: {ARCHIVE_PASSWORD}")
    else:
        print("Failed to upload file.")
