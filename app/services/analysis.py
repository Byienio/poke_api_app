from app.models import Pokemon
from collections import defaultdict

def analyze_types():
    pokemons = Pokemon.query.all()
    type_data = defaultdict(list)
    for p in pokemons:
        for t in p.types.split(','):
            if p.hp is not None and p.attack is not None and p.defense is not None:
                type_data[t].append(p)

    summary = []
    for t, group in type_data.items():
        count = len(group)
        if count == 0:
            continue
        avg_hp =round(sum(p.hp for p in group) / count,2)
        avg_attack = round(sum(p.attack for p in group) / count,2)
        avg_defense = round(sum(p.defense for p in group) / count,2)
        top_attack = max(group, key=lambda p: p.attack)
        lowest_hp = min(group, key=lambda p: p.hp)
        summary.append({
            'type': t,
            'count': count,
            'avg_hp': avg_hp,
            'avg_attack': avg_attack,
            'avg_defense': avg_defense,
            'top_attack': top_attack.name,
            'lowest_hp': lowest_hp.name
        })
    return summary

def top_overall_stat(limit=10):
    pokemons = Pokemon.query.all()
    ranked = sorted(pokemons, key=lambda p: (p.hp or 0) + (p.attack or 0) + (p.defense or 0), reverse=True)
    return [{'name': p.name, 'total': (p.hp or 0) + (p.attack or 0) + (p.defense or 0)} for p in ranked[:limit]]

def average_experience_by_type():
    pokemons = Pokemon.query.all()
    type_exp = defaultdict(list)
    for p in pokemons:
        for t in p.types.split(','):
            if p.base_experience is not None:
                type_exp[t].append(p.base_experience)
    return {t: round(sum(v) / len(v),2) for t, v in type_exp.items() if v}

def tallest_and_heaviest_by_type():
    pokemons = Pokemon.query.all()
    type_groups = defaultdict(list)
    for p in pokemons:
        for t in p.types.split(','):
            type_groups[t].append(p)
    result = {}
    for t, group in type_groups.items():
        tallest = max(group, key=lambda p: p.height or 0)
        heaviest = max(group, key=lambda p: p.weight or 0)
        result[t] = {
            'tallest': tallest.name,
            'heaviest': heaviest.name
        }
    return result

def type_distribution():
    pokemons = Pokemon.query.all()
    counter = defaultdict(int)
    for p in pokemons:
        for t in p.types.split(','):
            counter[t] += 1
    return dict(counter)

def stat_range_by_type():
    pokemons = Pokemon.query.all()
    type_groups = defaultdict(list)

    for p in pokemons:
        for t in p.types.split(','):
            type_groups[t].append(p)
    result = {}

    for t, group in type_groups.items():
        attack_vals = [p.attack for p in group if p.attack is not None]
        defense_vals = [p.defense for p in group if p.defense is not None]
        hp_vals = [p.hp for p in group if p.hp is not None]

        result[t] = {
            'attack_min': min(attack_vals) if attack_vals else None,
            'attack_max': max(attack_vals) if attack_vals else None,
            'defense_min': min(defense_vals) if defense_vals else None,
            'defense_max': max(defense_vals) if defense_vals else None,
            'hp_min': min(hp_vals) if hp_vals else None,
            'hp_max': max(hp_vals) if hp_vals else None,
        }
    return result

def get_analysis_data(analysis_type):
    if analysis_type == 'avg_stats_by_type':
        return {
            'title': 'Average stats by type',
            'data': analyze_types()
        }
    elif analysis_type == 'top_overall_stats':
        return {
            'title': 'Top Pokémon (overall stats)',
            'data': top_overall_stat()
        }
    elif analysis_type == 'avg_experience_by_type':
        return {
            'title': 'Average experience by type',
            'data': average_experience_by_type()
        }
    elif analysis_type == 'tallest_heaviest_by_type':
        return {
            'title': 'Tallest and heaviest Pokémon by type',
            'data': tallest_and_heaviest_by_type()
        }
    elif analysis_type == 'type_distribution':
        return {
            'title': 'Pokémon type distribution',
            'data': type_distribution()
        }
    elif analysis_type == 'stat_range_by_type':
        return {
            'title': 'Stat ranges by type',
            'data': stat_range_by_type()
        }
    return None
