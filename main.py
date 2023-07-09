from bs4 import BeautifulSoup
import requests

fields = ['Regione', 'Provincia', 'Città metropolitana', 'Sindaco', 'Coordinate', 'Superficie', 'Abitanti', 'Densita']
       # lombardia,  pavia, fabrizio fracassi
def get_html_content(city):
    url = f'https://it.wikipedia.org/wiki/{city}'
    response = requests.get(url)
    return response.content

def scrape_data(html_content):

    soup = BeautifulSoup(html_content, "html.parser")

    info_table = soup.find('table', {'class': 'infobox sinottico'})

    for row in info_table.find_all('tr'):
        # print(row.prettify())
        a_tag = row.find('a')

        if a_tag is not None:
            title = a_tag.get_text()
            if title in fields:
                value = row.td.find('a', recursive=False)
                if value is not None:
                    print(value.get_text())

cities = ['Pavia', 'Roma']

for city in cities:
    html_content = get_html_content(city)
    scrape_data(html_content)