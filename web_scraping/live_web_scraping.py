from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
content = response.text
soup = BeautifulSoup(content, "html.parser")
print(soup.find(class_="titleline").text)
all_elements_score = soup.find_all(class_="score")
maxValue={
    "id": "",
    "value": 0
}
for element in all_elements_score:
    if int(element.text.split(" ")[0]) > maxValue["value"]:
        maxValue["value"]=int(element.text.split(" ")[0])
        maxValue["id"]=element.get("id")
print(maxValue)