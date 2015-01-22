# Short manga downloading script
# Currently hardcoded to be used with mangahere.co

# github.com/spokenlore

import urllib2
from bs4 import BeautifulSoup

shorturl = "http://www.mangahere.co/manga/shokugeki_no_soma/"
manganame = shorturl.lstrip("http://www.mangahere.co/manga/")
manganame = manganame.rstrip("/")

if shorturl[len(shorturl)-1] != "/":
	shorturl = shorturl + "/"

for x in xrange(102,103):
	if x < 10:
		chapstart = "c00"
	elif x < 100:
		chapstart = "c0"
	else:
		chapstart = "c"

	url = shorturl + chapstart + str(x) + "/"

	y = 1
	while url != "javascript:void(0);":

		html = urllib2.urlopen(url)
		soup = BeautifulSoup(html)

		imgurl = ""

		for a in soup.findAll('img'):
			if imgurl == "":
				imgurl = a["src"]

		image=urllib2.urlopen(imgurl)

		pagename = manganame + "_ch" + str(x) + "_pg" + str(y) + ".jpg"

		with open(pagename,'wb') as localFile:
			localFile.write(image.read())

		for b in soup.findAll('a', {'class' : 'next_page'}):
			link = b["href"]
			url = link
		
		y += 1