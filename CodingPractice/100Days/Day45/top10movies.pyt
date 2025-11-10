from bs4 import BeautifulSoup
import requests


#-------- Core Objects ----------#
response = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(response.text, "html.parser")
#-------- ------------ ----------#

#-------- Selection of major tree (quote class branch) u would like to acces things ----- #
quote_text = soup.find_all(class_="quote")


for items in quote_text: 
  quotes = items.find("span", class_="text").get_text()
  author = items.find("small", class_="author").get_text()
  tags = []
  for t in items.find_all("a", class_="tag"):
    tags.append(t.get_text())
  
  print(f"Quotes: {quotes}")
  print(f"Author: {author}")
  print(f"Tags: {', '.join(tags)}")
  print("-------------------------------------------------------")