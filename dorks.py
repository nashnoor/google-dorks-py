import os
from googlesearch import search
import requests

# Define the search query
query = 'site:example.com filetype:pdf Example'

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

# Define the directory path to save the PDF files
download_dir = 'path/to/dorks/downloads'

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
    #print(f'{filename} downloaded to {download_dir}')
print("Done")


