import requests
from bs4 import BeautifulSoup
from proxy_auth import proxies
import json

headers = {
    'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

count = 0
#  собираем ссылки
fests_urls_list = []
fests_list_results = []

for i in range(0, 192, 24):
    
    url = f'https://www.skiddle.com/festivals/search/?ajaxing=1&sort=0&fest_name=&from_date=11%20Sep%202022&to_date=&maxprice=500&o={i}&bannertitle=September'
    
    # вариант с прокси
    # req = requests.get(url=url, headers=headers, proxies=proxies)
    req = requests.get(url=url, headers=headers)
    json_data = json.loads(req.text)
    html_response = json_data['html']

    with open(f'data_lesson4/index_{i}.html', 'w') as file:
        file.write(html_response)

    with open(f'data_lesson4/index_{i}.html') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    cards = soup.find_all('a', class_='card-img-link')

    for item in cards:
        fest_url = 'https://www.skiddle.com' + item.get('href')
        fests_urls_list.append(fest_url)

for url in fests_urls_list:
    count += 1
    print(f'Обрабатывается фестиваль №{count}: {url}')

    req = requests.get(url=url, headers=headers)
    try:
        soup = BeautifulSoup(req.text, 'lxml')

        fest_card = soup.find(class_='MuiPaper-elevation1')
        all_spans = fest_card.find_all('span')

        fest_name = soup.find('h1').text.strip()
        fest_date = all_spans[0].text + all_spans[1].text
        fest_location = all_spans[2].text

        # поиск внутри вложенных в контейнер тегов <p>
        # contact_details = soup.find("h2", string="Venue contact details and info").find_next()
        # items = [item.text for item in contact_details.find_all("p")]

        fests_list_results.append(
            {
                'Fest name': fest_name,
                'Fest date': fest_date,
                'Fest place': fest_location
            }
        )

    except Exception as e:
        print(e)

with open('data_lesson4/fest_list.json', 'a', encoding='utf-8') as file:
    json.dump(fests_list_results, file, indent=4, ensure_ascii=False)
