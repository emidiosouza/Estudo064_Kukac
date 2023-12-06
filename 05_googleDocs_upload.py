from googleapiclient.discovery import build

def create_google_docs(summary, folder_id):
    service = authenticate_drive()
    title = 'Meeting Summary'
    body = {
        'title': title
    }
    doc = service.documents().create(body=body).execute()
    document_id = doc.get('documentId')

    # Mais código aqui para escrever o conteúdo (summary) no documento.
    
    # Mover o documento para a pasta desejada
    file = service.files().get(fileId=document_id, fields='parents').execute()
    previous_parents = ",".join(file.get('parents'))
    file = service.files().update(
        fileId=document_id,
        addParents=folder_id,
        removeParents=previous_parents,
        fields='id, parents').execute()

def delete_video_file(service, file_id):
    service.files().delete(fileId=file_id).execute()
