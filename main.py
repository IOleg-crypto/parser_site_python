import requests as pq
from bs4 import BeautifulSoup


def main():
    url = "https://mate.academy/blog/ru/python-ru/python-web-parser/"
    response = pq.get(url)

    print(response.text)

    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.select("h1.blog-title")

    for title in titles:
        print(title.get_text(strip=True))

    with open("titles.txt", "w") as f:
        for title in titles:
            f.write(title.get_text() + "\n")


if __name__ == "__main__":
    main()
