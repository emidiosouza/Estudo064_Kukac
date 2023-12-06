from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io
import os

def authenticate_drive():
    # Autenticação usando o  google-auth
    # Aqui você deverá usar suas credenciais e código de autenticação. Função disponível em googleAutenticação.py

def watch_folder(folder_id):
    service = authenticate_drive()
    results = service.files().list(
        q=f"'{folder_id}' in parents and mimeType='video/mp4'",
        spaces='drive',
        fields='nextPageToken, files(id, name)',
        pageToken=None).execute()
    return results.get('files', [])


def download_video(service, file_id, file_name):
    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print(f'Download {int(status.progress() * 100)}%.')
    fh.seek(0)

    with open(os.path.join('./videos', file_name), 'wb') as f:
        f.write(fh.read())
        f.close()
