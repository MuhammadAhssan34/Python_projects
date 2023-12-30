import requests
from bs4 import BeautifulSoup
from urllib import *
from urllib.parse import urljoin


visited_url = set()


def urls(url, keyword):
    try :
        response = requests.get(url)
        



    except :
        print(f'an error occured on url {url}')
        return 

    if response.status_code == 200:
        soup = BeautifulSoup(response.content , 'html.parser')
        a_tag = soup.find_all("a")

        url_list = []

        for t in a_tag:
            href = t.get("href")
            
            if href is not None and href != '':
                url_list.append(href)

        # print(url_list)
        for i in url_list:
            if i not in visited_url:
                visited_url.add(url)
                url_join = urljoin(url, i)  # it's a bug 

                if keyword in url_join :
                    print(url_join)
                    urls(url_join, keyword)
                else : 
                    pass







keyword = input("Please enter keyword")
url = input("Please enter url : ")
urls(url, keyword)