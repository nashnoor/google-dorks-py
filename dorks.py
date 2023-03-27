import os
import time
import ftplib
from googlesearch import search
import requests
import logging

logging.basicConfig(filename='dorks.log', level=logging.INFO)

# Define the search query
query = 'site:example.com filetype:pdf example'

# Set the number of search results to retrieve
num_results = 10

# Perform the Google search and retrieve the URLs of the search results
urls = list(search(query, stop=num_results))

# Save the URLs to a text file
with open('results.txt', 'w') as f:
    for url in urls:
        f.write(url + '\n')

# Print a confirmation message
print(f'Search results saved to results.txt')
logging.info(f'Search results saved to results.txt')

# Define the directory path to save the PDF files
download_dir = 'path/to/downloads' #change based on generated path in install.sh

# Open the text file containing the URLs
with open('results.txt', 'r') as f:
    urls = f.readlines()

# Loop through the URLs and download the PDF files
for url in urls:
    url = url.strip()  # Remove any leading/trailing whitespace
    response = requests.get(url)
    filename = url.split('/')[-1]  # Extract the filename from the URL
    filepath = os.path.join(download_dir, filename)  # Join the download directory and filename
    with open(filepath, 'wb') as f:
        f.write(response.content)

print("Files downloaded")
logging.info('Files downloaded')

# FTP login credentials
ftp_host = 'ftp.example.com'
ftp_user = 'username'
ftp_password = 'password'

# Local directory path
local_dir_path = download_dir

# Connect to the FTP server
with ftplib.FTP(ftp_host, ftp_user, ftp_password) as ftp:
    # Switch to the target directory on the FTP server
    ftp.cwd('uploads')

    # Loop through the local directory
    for filename in os.listdir(local_dir_path):
        # Create the full local file path
        local_file_path = os.path.join(local_dir_path, filename)

        # Open the local file for reading in binary mode
        with open(local_file_path, 'rb') as f:
            # Upload the file to the FTP server
            ftp.storbinary(f'STOR {filename}', f)

print("File uploaded to server")
logging.info(f'File uploaded to server')
time.sleep(5)
print("All of the process completed successfully")
logging.info('All of the process completed successfullyr')
