import requests

url = r'https://store.steampowered.com/feeds/news.xml'

# xml file will be generated in the directory

if __name__ == '__main__':
    # assign response to variable object
    response = requests.get(url)
    # write content of xml feed to a xml file
    # will write it bianary 'wb'
    with open('newrelease.xml', 'wb') as file:
        file.write(response.content)