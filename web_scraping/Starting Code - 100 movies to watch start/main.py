import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url=URL)
content = response.text

soup = BeautifulSoup(content, "html.parser")
titles=soup.find_all(class_="title")
file = open('movies.txt','w')
for i in range(1,len(titles)-9):
    myTitle=titles[-i].getText()
    file.write(f"{myTitle.encode('utf-8')}\n")
    print(myTitle.encode("utf8"))
file.close()
    

