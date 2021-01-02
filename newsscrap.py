import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://pulse.zerodha.com/')
# print(response)
soup = BeautifulSoup(response.text,'html.parser')
companys = soup.find_all(class_='box item') 

with open('news.csv', 'w', encoding="utf-8") as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Title', 'News', 'Link', 'FeedType']
    csv_writer.writerow(headers)

    for company in companys:
        title = company.find(class_='title').get_text().split('\n')
        link = company.find('a')['href']
        desc = company.find(class_='desc').get_text()
        Feedtype = company.find(class_='feed').get_text()
        csv_writer.writerow([title, desc, link, Feedtype])
        print(title)
        print(link)
        print(desc)
        print(Feedtype + '\n')
