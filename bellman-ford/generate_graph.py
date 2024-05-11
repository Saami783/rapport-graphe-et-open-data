import networkx as nx
import random


def generate_directed_graph_with_negative_weights(num_vertices, num_edges, num_negative_edges):
    G = nx.gnm_random_graph(num_vertices, num_edges, directed=True)
    for (u, v) in G.edges():
        G[u][v]['weight'] = 1  # Assigne par défaut un poids positif

    # Choisi une arête aléatoirement pour assigner un pods négatif
    sampled_edges = random.sample(list(G.edges()), num_negative_edges)
    for (u, v) in sampled_edges:
        G[u][v]['weight'] = -1 * G[u][v]['weight']  # Assigne un poids négatif

    return G


def save_graph_to_txt_file(graph, filename):
    with open(filename, 'w') as f:
        for u, v, data in graph.edges(data=True):
            f.write(f'{u} {v} {data["weight"]}\n')


num_vertices = 10
num_edges = 20
num_negative_edges = 2

# Créer le graphe
G = generate_directed_graph_with_negative_weights(num_vertices, num_edges, num_negative_edges)

# Sauvegarde le graphe au format txt
txt_filename = 'graph.txt'
save_graph_to_txt_file(G, txt_filename)
print(f"The graph has been saved in '{txt_filename}'.")