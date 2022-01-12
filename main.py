import json
import requests
from bs4 import BeautifulSoup

url = "https://www.empireonline.com/movies/features/best-movies-2/"

soup = BeautifulSoup(requests.get(url).content, "html.parser")
data = json.loads(soup.select_one("#__NEXT_DATA__").contents[0])


def find_article(data):
    if isinstance(data, dict):
        for k, v in data.items():
            if k.startswith("ImageMeta:"):
                yield v["titleText"]
            else:
                yield from find_article(v)
    elif isinstance(data, list):
        for i in data:
            yield from find_article(i)


    # print(a)

with open("movies.txt", mode="w") as File:
    for a in find_article(data):
        File.write(f"{a}\n")

#
# title_movies_tag = soup.find_all(name="h3", class_="jsx-4245974604")

# title_movies = []
#
# for title_movie in title_movies_tag:
#     title = title_movie.getText()
#     title_movies.append(title)
#
# print(title_movies)
