from bs4 import BeautifulSoup
from urllib.request import urlopen
url =  input("Please enter the url you wish to open: ")
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
print(soup.find("script"))
soup.find_all("img")