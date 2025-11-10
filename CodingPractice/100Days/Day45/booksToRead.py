import requests
from bs4 import BeautifulSoup


# Write your code below this line 👇
response = requests.get("https://books.toscrape.com/catalogue/category/books/travel_2/index.html")
soup = BeautifulSoup(response.text, "html.parser")



ol = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
for titles in ol:
  book_title = titles.find("h3")
  book_titles = book_title.find("a").get("title") #used to print attribute names instead of content 
  print(book_titles)