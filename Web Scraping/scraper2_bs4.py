import requests
import bs4

# get url
url = requests.get('https://pybit.es/pages/articles.html')

# raise error, if any
url.raise_for_status()

# get url text
soup = bs4.BeautifulSoup(url.text, 'html.parser')

# search for the unordered list (ul)
# you can search using tag names
# this search will go in sequence and will return the first "ul" tag that it finds
soup.ul

# alternative otion is to search for all ul tags, using find_all()
soup.find_all('ul')

# you can drill further if search for specific tags within page
# if target uls were under <main> we can search:
#### soup.main.ul
soup.article.ul

# can also search for the lists directly as we don't need all tags
# this will only obtain the desired headers/links
soup.article.find_all('li')

# svae all in a object
all_li = soup.article.find_all('li')

# lets get the titles
# you can either use getText OR string to string out the junk!
for i in all_li:
    print(i.string)


