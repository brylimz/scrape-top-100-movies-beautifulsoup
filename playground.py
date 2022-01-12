from bs4 import BeautifulSoup
import requests
import itertools
response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="titlelink")
articles_texts = []
articles_links = []

for article_tag in articles:
    text = article_tag.getText()
    articles_texts.append(text)
    link = article_tag.get("href")
    articles_links.append(link)

articles_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(articles_upvotes)
largest_index = articles_upvotes.index(largest_number)
print(articles_texts[largest_index])
print(articles_links[largest_index])
# print(articles_texts)
# print(articles_links)
# print(articles_upvotes)
















# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.prettify())
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
# #
# # heading = soup.find(name="h1", id="name")
# # print(heading)
# #
# # section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.getText("name"))
# #
# # company_url = soup.select_one(selector="p a")
# # print(company_url)
#
# # name = soup.select_one("#name")
# # print(name)
# headings = soup.select(".heading")
# print(headings)
