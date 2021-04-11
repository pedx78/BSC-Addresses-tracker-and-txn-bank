from bs4 import BeautifulSoup
from urllib.request import urlopen

print("RUNNIGN ------------------")
with urlopen('http://www.rottentomatoes.com') as homepage:
    soup = BeautifulSoup(homepage)
    print("saved")

for link in soup.find_all('a'):
    print(link.get('href'))