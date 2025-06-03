import os
from google.oauth2.credentials import Credentials
# Imports the Credentials class, which is used to authenticate a user to the Google API.
from googleapiclient.discovery import build
# Imports the build function, which creates a service to interact with the Google API
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
# Imports the MediaFileUpload class, which allows you to upload files to Google Drive.
from google.auth.transport.requests import Request
# Imports the Request class, which is used to refresh authorization tokens.
from google_auth_oauthlib.flow import InstalledAppFlow
# Imports InstalledAppFlow, which helps to pass OAuth authorization (i.e. login via Google account).


folder_id = '1fAb4raP7rxU3d1-UDDJkQ-e73qXhJBO1' #ID folders in Google Drive
scopes = ['https://www.googleapis.com/auth/drive'] #Access scope — allows full access to Google Drive.


def create_connections():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', scopes)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret_file.json', scopes)

            creds = flow.run_local_server(port=0)

        with open('token.json', 'w')as token:
            token.write(creds.to_json())
    return creds


def upload_file(file_path, file_name, creds):
    service = build('drive', 'v3', credentials=creds)
    try:
        file = MediaFileUpload(file_path, resumable=True)
        file_metadata = {
            'name': file_name,
            'parents': [folder_id]
        }
        file = service.files().create(
            body=file_metadata,
            media_body=file,
            fields='id'
        ).execute()
        print("File uploaded")

    except HttpError as error:
        print("Something went wrong")
        file = None

    return file


def upload_files(directory_path, creds):
    files = os.listdir(directory_path)
    for file_name in files:
        file_path = os.path.join(directory_path, file_name)
        if os.path.isfile(file_path):
            upload_file(file_path, file_name, creds)


creds = create_connections()
directory_path = '/Users/sabrinabilmak/Downloads'
upload_files(directory_path, creds)
