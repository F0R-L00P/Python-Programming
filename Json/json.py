# JSON file has data similar to a nested dictionary or nested list
import json
import requests
from pprint import  pprint #(pretty print, undrestands json format and prints accordingly)

# parse json file to a string
file1 = requests.get('https://www.sba.gov/sites/default/files/data.json').text
file2 = requests.get('https://raw.githubusercontent.com/F0R-L00P/100daysofcode-with-python-course/master/days/40-42-json-data/code/mount-data.json').text

# allows decoding the json file and making it readable jdon dictionary
data = json.loads(file2)

pprint(data)

# How to access a sub dictionary in the jason file
# lets acces 'mounts'

# this will provide all the keys in teh dictionary
for value in data['mounts']:
    print(value)

# to access the values under mounts dictionary use second key
# use name of key in subdictionary for the values printed
for value in data['mounts']['collected']:
    pprint(value['name'])

# lets get name of all creatures that can fly
# recall python assumes True aargument as default
# no need to compare value to boolean expression value['isFlying'] == True
# the appended list is a list of dictionaries with flying creatures 
flying_creatures = []
for value in data['mounts']['collected']:
    if value['isFlying']:
        flying_creatures.append(value)
# using boolean expression 
for value in data['mounts']['collected']:
    if value['isFlying'] == True:
        pprint(value['name'])