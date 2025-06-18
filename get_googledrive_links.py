import os
import pickle
import pandas as pd
import xlsxwriter

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

def get_file_info(folder_name):
    """Lists the names and links of files in specified folders in Google Drive and writes to an Excel file.
    Args:
        folder_names: A list of folder names to search within.
    Returns:
        None. Writes the file information to an Excel file named 'drive_files.xlsx'.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no valid credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    try:
        service = build('drive', 'v3', credentials=creds)
        file_info_list = []

        folder_result = service.files().list(q=f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder'",
                                            fields="files(id)").execute()
        folder = folder_result.get('files', [])

        if not folder:
            print(f"No folder found with name: {folder_name}")

        folder_id = folder[0]['id']

        # Call the Drive v3 API to get files in the folder
        results = service.files().list(q=f"'{folder_id}' in parents",
                                        fields="files(name, webViewLink)").execute()
        files = results.get('files', [])

        if not files:
            print(f"No files found in folder: {folder_name}")
        else:
            print(f"Files in folder: {folder_name}")
            for file in files:
                file_info_list.append({'folder': folder_name, 'name': file['name'], 'link': file['webViewLink']})

        if not file_info_list:
            print('No files found in the specified folders.')
            return

        # Create a Pandas DataFrame from the file information list
        df = pd.DataFrame(file_info_list)

        # Write the DataFrame to an Excel file
        excel_file = 'drive_files.xlsx'
        df.to_excel(excel_file, index=False)
        print(f"File information written to {excel_file}")

    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')

if __name__ == '__main__':
    folder_name = input("Enter folder name: ")
    get_file_info(folder_name)