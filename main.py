import requests
from bs4 import BeautifulSoup
import time
from  mangas import urls
from os import system, name 

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
  
    else: 
        _ = system('clear') 

while True:

    for url in urls:
        response = requests.get(url)
        data = response.content
        soup = BeautifulSoup(data, "html.parser")
        for i in soup.find_all('div',{'class':'addto'}):
            link = i.find('a',href=True)
            if link is None:
                continue
        funciona = soup.find('span', {'class': 'price-sales'})
        title = soup.find('title')
        print("Nome do manga: " +str(title.string) + "Preco = " + str(funciona.string) + "\nlink de compra -> " + str(link['href'] + "\n"))
    time.sleep(60)
    clear()






