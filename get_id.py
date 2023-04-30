import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
for i in range(1000, 30001, 1):
    try:
        response = requests.get(
            f"https://my.clevelandclinic.org/health/diseases/{i}", headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            h1_text = soup.find('h1').text.replace('\n', '')
            with open('cleveland_200.text', 'a') as h:
                h.write(f'{i}\n')

       	        print(i)
        else:
            print()

    except requests.exceptions.Timeout:
        print()
    except requests.exceptions.RequestException as e:
        print()
