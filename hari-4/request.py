import requests

my_req = requests.get('https://swapi.co/api/starships/10/')

print(my_req.json())