import os
from bs4 import BeautifulSoup


def main():
    dirr = 'h:/programming/clevelandclinic/health_diseases/'
    symptomscauses_class = 'js-section js-section--symptoms-and-causes'
    file_list = os.listdir(dirr)
    total_items = len(file_list)
    text_to_append = ''
    for i, file in enumerate(file_list):
        if file.endswith('.html'):
            with open(dirr + file, 'r') as f:
                contents = f.read()
            soup = BeautifulSoup(contents, 'html.parser')
            div = soup.find('div', class_=f'{symptomscauses_class}')
            if div is not None:
                ul_tags = div.find_all('ul')
                if ul_tags is not None:

                    for ul in ul_tags:
                        li_tags = ul.find_all('li')
                        if li_tags is not None:
                            for li in li_tags:
                                text_to_append += (str(li.text) + '\n')

                p_tags = div.find_all('p')
                if p_tags is not None:
                    for p in p_tags:
                        text_to_append += (str(p.text) + '\n')

                if text_to_append != '':
                    with open(f'H:\Programming\DOCTOR WHERE\cleveland_\symptomsANDcauses_TEXT/{file[:-5]}.text', 'w') as h:
                        h.write(text_to_append)
                        text_to_append = ''
        print(
            f"Processing item {i+1}/{total_items} ({(i+1)/total_items*100:.2f}%): {file[:-5]}")
    return


if __name__ == '__main__':
    main()
    print('bruh')
