from bs4 import BeautifulSoup
import lxml

with open("website.html",errors="ignore") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
# print(soup.prettify())
# print(soup.a)
# print(soup.li)

all_anchor_elements = soup.find_all(name="a")
print(all_anchor_elements)

for tag in all_anchor_elements:
    #print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.text )

headings = soup.select(".heading")#or "#" sign for id search
#similar to css selector, use "a p" for selecting p tag under a
print(headings)

print(soup.find("input").get("maxLength"))