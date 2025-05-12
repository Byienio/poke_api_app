from flask import Response
from app.models import Pokemon
import json

def export_pokemon_json():
    records = Pokemon.query.all()
    result = [
    {
    "name": r.name,
    "pokemon_type": r.pokemon_type,
    "hp": r.hp,
    "attack": r.attack,
    "defense": r.defense,
    "speed": r.speed,
    "special_attack": r.special_attack,
    "special_defense": r.special_defense,
    } for r in records
    ]
    return Response(json.dumps(result, indent=4), mimetype='application/json')