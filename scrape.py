import os
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

dir = 'cleveland_data/'

with open('cleveland_200.text', 'r') as f:
    texts = f.readlines()
texts = [text.replace('\n', '') for text in texts]
for num in texts:
    while True:
        try:
            response = requests.get(
                f'https://my.clevelandclinic.org/health/diseases/{num}', headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(
                    response.content, 'html.parser')
                h1 = soup.find('h1').text.replace(
                    '\n', '').replace(' / ', 'or').replace(':', ' -').replace('?', '').replace('/', ' or ').replace(', ', ' and ').replace('\r', '')
                print(h1, num)
                with open(dir + '/' + str(h1) + '.html', 'w') as w:
                    w.write((str(soup)))
                break

        except:
            continue
