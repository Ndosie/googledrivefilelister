
# Google Drive File Lister

This Python script is a handy tool designed to help you quickly get a list of all the files in a specific Google Drive folder, complete with their names and direct links. It's super useful if you want to export your file inventory to an Excel spreadsheet for things like data analysis, uploading to a database, or just keeping a clean record.

---

## Prerequisites

Before you can get started, make sure you have the following:

* **Python 3.x** installed on your system.
* The following Python packages. You can install them using `pip`:
    ```bash
    pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib pandas xlsxwriter
    ```
* **Google API Credentials:** You'll need to set up a project in the Google Cloud Console, enable the Google Drive API, and download your `credentials.json` file. Make sure this file is in the same directory as your script. If you need help with this step, Google's official documentation on "Enabling the Drive API" is a great resource!

---

## How to Use It

1.  **Place your `credentials.json` file** in the same directory as the Python script.
2.  **Run the script:**
    ```bash
    python your_script_name.py
    ```
    (Replace `your_script_name.py` with the actual name of your Python file.)
3.  **Authentication:** The first time you run the script, a browser window will open, prompting you to authenticate your Google account. Follow the on-screen instructions to grant the necessary permissions. This creates a `token.json` file, so you won't have to re-authenticate every time you run it.
4.  **Enter your Google Drive Folder ID:** The script will then ask you to input the ID of the Google Drive folder you want to scan. You can find this ID in the URL when you're viewing the folder in your web browser (it's the long string of characters after `/folders/`).
5.  **Get your Excel file!** Once the script finishes, it will generate an Excel file (e.g., `google_drive_files.xlsx`) in the same directory. This file will contain two columns: "File Name" and "File Link," ready for all your data adventures!

---

## What's Next?

This script provides a solid foundation for managing your Google Drive files programmatically. From here, you could:

* **Filter files** based on type, date, or other metadata.
* **Automate uploads or downloads** to and from specific folders.
* **Integrate this data** into larger data analysis pipelines or dashboards.

Have any questions or ideas for improvements? Feel free to reach out!