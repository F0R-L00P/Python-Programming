# Accessing HTTP API's
# can check API interaction using postman, which gives overview, body, header access 
# and check response time and status of the target site

# lets check sample url
# url = r'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?view=data&acc=GSM2886523&id=46221&db=GeoDb_blob158'

# import requests
# response = requests.get(url)
# response.status_code

# response.headers['keep-Alive']
# print('Encoding: ', response.encoding)


# =============================================================================
# Lets build a program that can communicate with an API
# =============================================================================
## NOTE ##
## Steps in consuming the movie API
## 1- use postman app to interact with API to view before coding 
## 2- break code in (a) user interaction code (b) API access code
## 3- use requests to get data and interact using code
   # 3.1. download content using GET
   # 3.2. check status
## 4- convert obtained data to JSON and its pure python coding after!
## 5- add typings to make user interface clear whne putting inputs in code

## to consume API's the goal is to break them arapt and extract information required 
## from the API then build the desired user interface to interact with it



# import python file api.py holding api access
import api


def main():
    # use input in variable to allow user to search for titles
    keyword = input('keyword of title search: ')
    results = api.find_movies(keyword)
    print(f'There are {len(results)} movies found.')
    for i in results:
        # since all data is in movie list, you can get each section that we're interested in
        print(f"{i.title} with code {i.imdb_code} has score {i.imdb_score}")
        
        
        
        
if __name__ == '__main__':
    main()