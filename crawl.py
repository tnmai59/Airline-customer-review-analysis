from bs4 import BeautifulSoup
import requests
import urllib.request
from urllib.request import Request, urlopen
import json
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import numpy as np

#Function to parse to web
def web_parser(link, headers = {'User-Agent': 'Mozilla/5.0'}):
    req = Request(
    url= link, 
    headers=headers
    )
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    return soup

def get_link(soup):
    links = soup.find('article', class_='comp comp_reviews-pagination querylist-pagination position-').find('ul').find_all('a')
    new_url = 'https://www.airlinequality.com' + links[-1].get('href')
    return new_url

def convert(lst):
   res_dict = {}
   for i in range(0, len(lst), 2):
       res_dict[lst[i]] = lst[i + 1]
   return res_dict

def crawl(soup):
    dataset = []
    count = 1
    while True:
        # Vòng while True này ứng với mỗi page 
        rvs = soup.find_all('article', itemprop='review')
        for i in range(len(rvs)):
            tlist = []
            # Mỗi vòng for ứng với mỗi review trong một page
            rv_id = rvs[i].find('div', class_='body').get('id')
            rv_date = rvs[i].find('meta', itemprop='datePublished').get("content")
            rv_header = rvs[i].find('h2', class_='text_header').get_text()
            rv_text = rvs[i].find('div', class_='text_content', itemprop='reviewBody').get_text()
            rating_element = rvs[i].find('span', itemprop='ratingValue')
            if rating_element is not None:
                # Extract the text of the rating element and convert it to an integer
                overall_rating = int(rating_element.text)
            else:
                overall_rating = np.nan
            # Crawl stats data
            table = rvs[i].find_all('td')
            for j in range(len(table)):
                if table[j].get('class') == ['review-rating-stars', 'stars']:
                    if len(table[j].find_all('span', class_ ="star fill")) != 0:
                        value = table[j].find_all('span', class_ ="star fill")[-1].get_text()
                else:
                    value = table[j].get_text()
                tlist.append(value)
            tdict = convert(tlist)
            tdict['Review id'] = rv_id
            tdict['Review date'] = rv_date
            tdict['Review header'] = rv_header
            tdict['Review'] = rv_text
            tdict['Overall rating'] = overall_rating
            dataset.append(tdict)
        link = get_link(soup)
        new_soup = web_parser(link)
        if new_soup == soup:
            print("Last page")
            break
        else:
            soup = new_soup
            print(f'Finish page {count}')
        count += 1
    return dataset


            
if __name__ == '__main__':
    airline_name = 'frontier-airlines'
    airline_url = 'https://www.airlinequality.com/airline-reviews/' + airline_name + '/'
    req = Request(
        url= airline_url, 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    data = crawl(soup)
    df = pd.DataFrame(data)
    save_path = 'D:/Đề án/Data2/' + airline_name + '.csv'
    df.to_csv(save_path, index=False, encoding='utf-8-sig')
    print(f'Finish {airline_name}')
                