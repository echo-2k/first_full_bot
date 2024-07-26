import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from config import SERVICE_ACCOUNT_FILE, FOLDER_ID

SCOPES = ['https://www.googleapis.com/auth/drive.file']
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('drive', 'v3', credentials=credentials)

async def upload_file(file_path: str):
    file_metadata = {
        'name': os.path.basename(file_path),
        'parents': [FOLDER_ID]
    }
    media = MediaFileUpload(file_path, resumable=True)
    request = service.files().create(body=file_metadata, media_body=media, fields='id,webViewLink')
    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"Uploaded {int(status.progress() * 100)}%.")

    if response:
        file_id = response.get('id')
        file_link = response.get('webViewLink')
        return file_link
    else:
        raise Exception("Failed to upload file.")
