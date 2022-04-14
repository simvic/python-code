import requests
from bs4 import BeautifulSoup
from csv import writer

url = "http://127.0.0.1:8000/blog"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'lxml')

lists = soup.find_all('div', class_="blog-post")

with open('file.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Author', 'Date', 'Comment', 'Contents']
    thewriter.writerow(header)

    for list in lists:
        title = list.find('h3').text
        author = list.find('a', class_="author").text
        date = list.find('a', class_="date").text
        comment = list.find('a', class_="comments").text
        text = list.find('p', class_="contents").text

        info = [title, author, date, comment, text]
        thewriter.writerow(info)
