from .analysis import (
    analyze_types, top_overall_stat, average_experience_by_type, type_distribution, stat_range_by_type
)

def chart_data_from_dict(title, data_dict, value_label, chart_type='bar',datasets=None):
    if datasets:
        return {
            'labels': list(data_dict.keys()),
            'datasets': datasets,
            'title': title,
            'type': chart_type
        }
    else:
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
    return chart_data_from_dict("Average Attack by Type", attack_data, "Average Attack")

def chart_hp_by_type():
    data = analyze_types()
    hp_data = {entry['type']: entry['avg_hp'] for entry in data}
    return chart_data_from_dict("Average HP by Type", hp_data, "Average HP")

def chart_type_distribution():
    data = type_distribution()
    return chart_data_from_dict("Number of Pokémon by Type", data, "Number of Pokémon")

def chart_average_experience():
    data = average_experience_by_type()
    return chart_data_from_dict("Average Base Experience", data, "Experience", chart_type='line')

def chart_stat_ranges(stat='attack'):
    data = stat_range_by_type()
    labels = list(data.keys())

    min_values = [stats.get(f'{stat}_min') for stats in data.values()]
    max_values = [stats.get(f'{stat}_max') for stats in data.values()]

    datasets = [
        {
            'label': f'{stat.capitalize()} Min',
            'data': min_values,
            'backgroundColor': 'rgba(54, 162, 235, 0.6)'
        },
        {
            'label': f'{stat.capitalize()} Max',
            'data': max_values,
            'backgroundColor': 'rgba(255, 99, 132, 0.6)'
        }
    ]

    return chart_data_from_dict(f'{stat.capitalize()} Min/Max by Type',{label: None for label in labels},f'{stat.capitalize()}',chart_type='bar',datasets=datasets)

def chart_top_overall_stat():
    data = top_overall_stat()
    name_data = {entry['name']: entry['total'] for entry in data}
    return chart_data_from_dict("Top Pokémon by Total Stats", name_data, "Total HP+Attack+Defense", chart_type='line')


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