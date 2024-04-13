from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
content = response.text
soup = BeautifulSoup(content, "html.parser")
articles = soup.find_all(class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.find("a").get("href")
    article_links.append(article_link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(class_="score")]
max_value_index = article_upvotes.index(max(article_upvotes))
print(max_value_index)
print(article_texts[max_value_index])
print(article_links[max_value_index])
print(article_upvotes[max_value_index])
