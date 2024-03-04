import requests
import os
from bs4 import BeautifulSoup

# URL of the directory you want to start from
base_url = "http://10.10.110.100:65000/wordpress/wp-includes/js/"

# Output folder to save the downloaded files
output_folder = "downloaded_js_files"

# Function to download a file
def download_file(url, folder):
    response = requests.get(url)
    if response.status_code == 200:
        filename = os.path.join(folder, url.split("/")[-1])
        with open(filename, 'wb') as f:
            f.write(response.content)

# Function to download all .js files from a directory
def download_js_files_from_directory(directory_url, output_folder):
    response = requests.get(directory_url)

    if response.status_code == 200:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)

        for link in links:
            file_url = directory_url + link['href']
            if file_url.endswith('.js'):
                download_file(file_url, output_folder)

            # Check if the link is a directory (ends with '/')
            if link['href'].endswith('/'):
                subdir_url = directory_url + link['href']
                download_js_files_from_directory(subdir_url, output_folder)

# Call the function to start downloading .js files from the base directory
download_js_files_from_directory(base_url, output_folder)

