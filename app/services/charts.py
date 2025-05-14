from .analysis import (
    analyze_types, top_overall_stat, average_experience_by_type,
    tallest_and_heaviest_by_type, type_distribution, stat_range_by_type
)

def chart_data_from_dict(title, data_dict, value_label, chart_type='bar'):
    return {
        'labels': list(data_dict.keys()),
        'data': list(data_dict.values()),
        'label': value_label,
        'title': title,
        'type': chart_type
    }

def chart_attack_by_type():
    data = analyze_types()
    attack_data = {entry['type']: entry['avg_attack'] for entry in data}
    return chart_data_from_dict("Średni atak według typu", attack_data, "Średni atak")

def chart_hp_by_type():
    data = analyze_types()
    hp_data = {entry['type']: entry['avg_hp'] for entry in data}
    return chart_data_from_dict("Średnie HP według typu", hp_data, "Średnie HP")

def chart_type_distribution():
    data = type_distribution()
    return chart_data_from_dict("Liczba Pokémonów według typu", data, "Liczba Pokémonów")

def chart_average_experience():
    data = average_experience_by_type()
    return chart_data_from_dict("Średnie doświadczenie podstawowe", data, "Doświadczenie", chart_type='line')

def chart_stat_ranges(stat='attack'):
    data = stat_range_by_type()
    stat_data = {t: stats[f'{stat}_range'] for t, stats in data.items()}
    return chart_data_from_dict(f"Zakres {stat.capitalize()} według typu", stat_data, f"Zakres {stat.capitalize()}")

def chart_top_overall_stat():
    data = top_overall_stat()
    name_data = {entry['name']: entry['total'] for entry in data}
    return chart_data_from_dict("Top Pokémony wg sumy statystyk", name_data, "Suma HP+Atak+Obrona", chart_type='line')

def get_chart(chart_type):
    if chart_type == "chart_attack_by_type":
        return chart_attack_by_type()
    elif chart_type == "chart_hp_by_type":
        return chart_hp_by_type()
    elif chart_type == "chart_type_distribution":
        return chart_type_distribution()
    elif chart_type == "chart_average_experience":
        return chart_average_experience()
    elif chart_type == "chart_stat_ranges":
        return chart_stat_ranges()
    elif chart_type == "chart_top_overall_stat":
        return chart_top_overall_stat()
    else:
        return None