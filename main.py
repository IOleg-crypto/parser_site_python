import requests as pq
from bs4 import BeautifulSoup


def main():
    url = "https://mate.academy/blog/ru/python-ru/python-web-parser/"
    response = pq.get(url)

    print(response.text)

    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.select("h2.blog-title")

    for title in titles:
        print(title.get_text(strip=True))


if __name__ == "__main__":
    main()
