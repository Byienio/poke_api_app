import requests
from app.models import db, Pokemon

def fetch_pokemon_data(limit=1000):
    url = f"https://pokeapi.co/api/v2/pokemon?limit={limit}"
    response = requests.get(url)
    results = response.json().get('results', [])
    all_data = []
    for pokemon in results:
        detail = requests.get(pokemon['url']).json()
        stats = {s['stat']['name']: s['base_stat'] for s in detail['stats']}
        types = ",".join([t['type']['name'] for t in detail['types']])
        all_data.append({
            'name': detail['name'],
            'base_experience': detail['base_experience'],
            'height': detail['height'],
            'weight': detail['weight'],
            'types': types,
            'hp': stats.get('hp', 0),
            'attack': stats.get('attack', 0),
            'defense': stats.get('defense', 0)
        })
    return all_data

def save_pokemon_data(pokemons):
    for p in pokemons:
        pokemon = Pokemon(
            name=p['name'],
            base_experience=p['base_experience'],
            height=p['height'],
            weight=p['weight'],
            types=p['types'],
            hp=p['hp'],
            attack=p['attack'],
            defense=p['defense']
        )
        db.session.add(pokemon)
    db.session.commit()
