import imp
import requests
import json

poke_list=[1,2,3,4,5,6]
with open('pokemon.txt','w') as p:
    for num in poke_list:
        url=f"https://pokeapi.co/api/v2/pokemon/{num}"
        response=requests.get(url).json()
        for item in response['forms']:
            p.write(item['name']+'\n')

