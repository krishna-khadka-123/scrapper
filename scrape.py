
#python -m pip install request
#=> git data from web (html,json,xml)
# python-m pip install beautifulsoup4
#=> parse html

#install git
#git config --global user.name "krishna khadka"
#git config --global user.email"chhetrikrishna7475@gmail.com"
import json
import csv
import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

def scrape_books(url):
    response = requests.get(url)
    if response.status_code != 200:
        return
    response.encoding = response.apparent_encoding

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    all_books = []
    for book in books:
        title = book.h3.a["title"]
        price_text = book.find("p", class_="price_color").text
        currency = price_text[0]
        price = float(price_text[1:])

        bookss = {
            "title": title,
            "currency": currency,
            "price": price
        }
        all_books.append(bookss)

    
    with open('bookss.json', 'w', encoding='utf-8') as f:
        json.dump(all_books, f, indent=2, ensure_ascii=False)
 
    with open("bookss.json", "r", encoding="utf-8") as f:
        data = json.load(f)

  
    with open("bookss.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

scrape_books(url)
