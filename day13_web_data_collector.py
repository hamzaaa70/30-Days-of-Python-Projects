import requests
from bs4 import BeautifulSoup

print("================================")
print("      WEB DATA COLLECTOR")
print("================================")

url = "https://books.toscrape.com/"

response = requests.get(url)

print()
print("Status Code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

print("Books found:", len(books))

print()
print(" BOOK REPORT ")

for book in books:

    title = book.find("h3").find("a")["title"]
    price = book.find("p", class_="price_color").text

    print()
    print("Book:", title)
    print("Price:", price)

print()
