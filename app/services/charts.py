import matplotlib.pyplot as plt
import io
import base64
from app.models import Pokemon
from collections import defaultdict


def generate_type_attack_chart():
    pokemons = Pokemon.query.all()
    type_data = defaultdict(list)

    for p in pokemons:
        for t in p.types.split(','):
            if p.attack is not None:
                type_data[t].append(p.attack)

    avg_attack_by_type = {t: sum(vals) / len(vals) for t, vals in type_data.items()}

    types = list(avg_attack_by_type.keys())
    avg_attacks = list(avg_attack_by_type.values())

    fig, ax = plt.subplots()
    ax.barh(types, avg_attacks, color='skyblue')
    ax.set_xlabel('Średni Atak')
    ax.set_title('Średni Atak według Typu Pokémonów')

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    img_base64 = base64.b64encode(img.getvalue()).decode('utf-8')

    return img_base64
