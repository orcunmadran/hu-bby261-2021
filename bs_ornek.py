import urllib.request
from bs4 import BeautifulSoup
webSite = urllib.request.urlopen("https://bby.hacettepe.edu.tr")
getBytes = webSite.read()
webPage = getBytes.decode("utf8")
webSite.close()
soup = BeautifulSoup(webPage, 'html.parser')
print(soup.title.contents)