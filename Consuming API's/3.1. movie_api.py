# setup virtual environment with requirement file
# requiremen.txt file will specify all th elibraries needed to runn the application
# when the file is packaged and ready to lunch only t h 
from typing import List
import requests
from collections import namedtuple

# define namedtuple with headers for easy access use below json output

# [{'imdb_code': 'tt1790864',
#            'title': 'The Maze Runner',
#            'director': 'Wes Ball',
#            'keywords': ['concrete wall',
#                         'based on novel',
#                         'open ended',
#                         'maze',
#                         'teenage boy'],
#            'duration': 113,
#            'genres': ['action', 'mystery', 'sci-fi', 'thriller'],
#            'rating': 'PG-13',
#            'year': 2014,
#            'imdb_score': 6.8},

Movie = namedtuple('Movie', ['imdb_code', 'title', 
                             'director', 'keywords',
                             'duration', 'genres',
                             'rating', 'year', 'imdb_score'])

# take a string and return search results
# this function will get a string and return a list of movies

def find_movies(SEARCH: str) -> List[Movie]:
    # using f-string
    url = f'http://movie_service.talkpython.fm/api/search/{SEARCH}'
    response = requests.get(url)
    # if anything goes wrong for any reason raise status code
    response.raise_for_status() 
    # convert text from json format to python dictionary
    results = response.json()
    movie_list = []
    #import pdb; pdb.set_trace()
    for i in results.get('hits'):
        # i -- is a dictionary of values obtained from response.get('hits')
        # we can unpack the dictionary into namedtuple values using **i
        ## Example Movie(**i)
            #Movie(imdb_code='tt1790864', title='The Maze Runner', 
            # director='Wes Ball', keywords=['concrete wall', 'based on novel', 'open ended', 'maze', 'teenage boy'], 
            # duration=113, genres=['action', 'mystery', 'sci-fi', 'thriller'], 
            # rating='PG-13', year=2014, imdb_score=6.8)
            movie_list.append(Movie(**i))
        
    return movie_list













