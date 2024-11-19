import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '84617442112fc12c605639647434b950'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
body_create = {
    "name": "generate",
    "photo_id": -1
}
body_rename = {
    "pokemon_id": "139155",
    "name": "generate",
    "photo_id": -1
}
body_add_pokeball = {
    "pokemon_id": "139155"
}

'''respons = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)

print(respons.text)'''

'''respons_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)

print(respons_rename.text)'''

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)

print(response_add_pokeball.text)




