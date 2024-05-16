import json
import matplotlib.pyplot as plt
import numpy as np
from llama_cpp import Llama





def categorize_results(data):
    results = {}
    for model, queries in data.items():
        results[model] = {'full_match': 0, 'semi_match': 0, 'no_match': 0, 'unparseable': 0}
        for query in queries:
            if query["unparseableJSON"]:
                results[model]['unparseable'] += 1
            elif query["matchingFields"] == query["numberOfFields"]:
                results[model]['full_match'] += 1
            elif query["matchingFields"] == 0:
                results[model]['no_match'] += 1
            else:
                results[model]['semi_match'] += 1
    return results

def plot_stacked_bar_chart(results):
    models = list(results.keys())

    models.sort(key=lambda model: (
        results[model]['full_match'],
        results[model]['semi_match'],
        results[model]['no_match'],
        results[model]['unparseable']
    ), reverse=True)

    full_match = [results[model]['full_match'] for model in models]
    semi_match = [results[model]['semi_match'] for model in models]
    no_match = [results[model]['no_match'] for model in models]
    unparseable = [results[model]['unparseable'] for model in models]

    bar_width = 0.6
    indices = np.arange(len(models))

    plt.figure(figsize=(12, 8))

    plt.bar(indices, full_match, bar_width, label='Potpuno podudaranje', color='blue')
    plt.bar(indices, semi_match, bar_width, bottom=full_match, label='Djelomično podudaranje', color='lightblue')
    plt.bar(indices, no_match, bar_width, bottom=np.array(full_match) + np.array(semi_match), label='Nema podudaranja',
            color='lightcoral')
    plt.bar(indices, unparseable, bar_width, bottom=np.array(full_match) + np.array(semi_match) + np.array(no_match),
            label='JSON nije parsibilan', color='red')

    plt.xlabel('Modeli')
    plt.ylabel('Broj upita')
    plt.title('Rezultati parsiranja upita po modelima')
    plt.xticks(indices, models, rotation=45, ha='right')

    plt.legend(bbox_to_anchor=(-0.1, 1), loc='upper right')

    plt.subplots_adjust(top=0.85)

    plt.tight_layout()
    plt.show()


with open('results_2024-05-16_02-37-55.json') as file:
    json_data = json.load(file)

results = categorize_results(json_data)
plot_stacked_bar_chart(results)
