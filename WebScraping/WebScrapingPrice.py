from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://lista.mercadolivre.com.br/placas-de-v%C3%ADdeo#D[A:placas%20de%20v%C3%ADdeo]"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

container = page_soup.find_all("section", {"class": "ui-search-results"})
i = 0
for item in container:
    item_price = item.find_all("span", {"class": "price-tag-fraction"})

    for price in item_price:
        print(price.text)
        shipping_prince = item.find_all("p", {"class": "ui-search-item__shipping ui-search-item__shipping--free"})
        print(shipping_prince[i].text)




