import requests


def fetch_pokemon_data(limit=50):
    url = f"https://pokeapi.co/api/v2/pokemon?limit={limit}"
    response = requests.get(url)
    results = response.json().get('results', [])
    all_data = []
    for pokemon in results:
        detail = requests.get(pokemon['url']).json()
        types = ",".join([t['type']['name'] for t in detail['types']])
        all_data.append({
            'name': detail['name'],
            'base_experience': detail['base_experience'],
            'height': detail['height'],
            'weight': detail['weight'],
            'types': types
        })
    return all_data

print(fetch_pokemon_data(50))