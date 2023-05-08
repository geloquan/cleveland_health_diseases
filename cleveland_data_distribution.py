import os
from bs4 import BeautifulSoup, Tag
from drwsql import remote1_connection


def query_title(title: str, url: str, category: str, type: str, text: str):
    querytitle = f"INSERT INTO content_drw.content_title (title,url,category,web_source) VALUES ('{title}','{url}','{category}','clevelandclinic');"
    querycontent = f"INSERT INTO content_drw.content (title,url,type,text) VALUES ('{title}','{url}','{type}','{text}');"
    cnx = remote1_connection()
    cursor = cnx.cursor()
    
    return


def main():
    data_dir = "H:\Programming\clevelandclinic\health_diseases"

    for file in os.listdir(data_dir):
        filename = file[:-5]
        print(filename)
        with open(f'{data_dir}/{file}', 'r') as f:
            raw_html = f.read()
            soup = BeautifulSoup(raw_html, 'html.parser')

            overview_section = soup.find(
                class_='js-section js-section--overview')
            sympcause_section = soup.find(
                class_='js-section js-section--symptoms-and-causes')

            if overview_section:
                h3 = overview_section.find('h3')
                if h3 and 'What is' in h3.text:
                    siblings = h3.find_all_next()
                    for sibling in siblings:
                        if sibling.name in {'h1', 'h2', 'h3', 'h4', 'h5', 'h6'}:
                            break
                        else:
                            if isinstance(sibling, Tag) and sibling.name in {'p', 'li'} and sibling.find_parent(class_='js-section js-section--overview'):
                                for a in sibling.find_all('a'):
                                    a.unwrap()
                                final_ly = sibling

            if sympcause_section:
                h3s = sympcause_section.find_all('h3')
                for h3 in h3s:
                    if h3 and 'ymptoms' in h3.text:
                        siblings = h3.find_all_next()
                        for sibling in siblings:
                            if sibling.name in {'h1', 'h2', 'h3', 'h4', 'h5', 'h6'}:
                                break
                            else:
                                if isinstance(sibling, Tag) and sibling.name in {'p', 'li'} and sibling.find_parent(class_='js-section js-section--symptoms-and-causes'):
                                    for a in sibling.find_all('a'):
                                        a.unwrap()
                                    final_ly = sibling
                                    print(final_ly)

    return


if __name__ == '__main__':
    main()
