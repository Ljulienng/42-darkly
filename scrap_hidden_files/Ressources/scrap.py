import requests
from bs4 import BeautifulSoup
import os

def traverse_directory(base_directory):
    print(base_directory)
    html_page = requests.get(base_directory).text

    soup = BeautifulSoup(html_page, 'html.parser')

    links_to_directories_to_traverse = []

    for link in soup.find_all('a'):
        href = link.get('href')

        if not href.startswith('..') and href != 'README':
            links_to_directories_to_traverse.append(href)

    try:
        current_directory_readme = requests.get(f'{base_directory}README').text
        yield current_directory_readme
    except requests.exceptions.RequestException:
        pass

    for directory_to_traverse in links_to_directories_to_traverse:
        yield from traverse_directory(base_directory + directory_to_traverse)

readme_files_content = []

for readme_file_content in traverse_directory('http://192.168.56.101/.hidden/'):
    readme_files_content.append(readme_file_content)

with open('results.txt', 'w') as results_file:
    results_file.write('\n'.join(readme_files_content))
