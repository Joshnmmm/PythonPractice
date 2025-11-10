from bs4 import BeautifulSoup



with open("website.html") as file:
  contents = file.read()


soup = BeautifulSoup(contents, "html.parser")
'''
print(soup.title)
print(soup.title.string)
'''


#print(soup.find_all("p"))

'''

all_anchor_tags = soup.find_all("a")

for tags in all_anchor_tags:
  print(tags.getText())
print("")
for tags in all_anchor_tags:
  print(tags.get("href"))
print("")

heading = soup.find(name="h1", id="name")
print(heading.getText())

print("")
company_url = soup.select_one(selector="p a")
print(company_url) 
'''

#name = soup.select_one("#name")
#print(name.getText())

list = soup.find_all("li")
for lists in list:
  print(lists.getText())
