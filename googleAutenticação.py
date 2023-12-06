from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.auth import load_credentials_from_file
import os
import pickle

# Scopes definem o nível de acesso que você está requisitando ao usuário.
SCOPES = ['https://www.googleapis.com/auth/drive']

def authenticate_drive():
    creds = None
    # O arquivo token.pickle armazena os tokens de acesso e atualização do usuário e é
    # criado automaticamente quando o fluxo de autorização é completado pela primeira vez.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # Se não há credenciais disponíveis, ou se as credenciais estão invalidadas, deixe o usuário fazer o login.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Salva as credenciais para a próxima execução
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds

def build_drive_service():
    creds = authenticate_drive()
    service = build('drive', 'v3', credentials=creds)
    return service

service = build_drive_service()
# Agora você pode chamar métodos na API do Drive, como:
# results = service.files().list(pageSize=10).execute()
