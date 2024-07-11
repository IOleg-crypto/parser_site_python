import requests as pq
from bs4 import BeautifulSoup


def set_url(link_site: str) -> str:
    url = link_site
    return url


def main():
    link = str(input("Write the url site : "))
    response = pq.get(set_url(link))

    print(response.text)

    soup = BeautifulSoup(response.text, "html.parser")
    print(soup.prettify())

    for link in soup.find_all('a'):
        print(link.get('href'))
    """""" """
    titles = soup.select("h2.blog-title")

    for title in titles:
        print(title.get_text(strip=True))

    with open("titles.txt", "w") as f:
        for title in titles:
            f.write(title.get_text() + "\n")
    """ """"""


if __name__ == "__main__":
    main()
