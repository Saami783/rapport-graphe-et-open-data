import networkx as nx
import random
import matplotlib.pyplot as plt


def generate_random_graph(num_vertices, num_edges):
    """ Génère un graphe aléatoire avec un nombre spécifié de sommets et d'arêtes. """
    G = nx.gnm_random_graph(num_vertices, num_edges)
    return G


def save_graph_to_file(graph, filename):
    """ Enregistre le graphe dans un fichier sous forme de liste d'adjacence. """
    with open(filename, 'w') as f:
        for line in nx.generate_adjlist(graph):
            f.write(line + '\n')


def save_graph_to_png(graph, filename):
    """ Enregistre le graphe dans un fichier PNG. """
    plt.figure(figsize=(8, 6))
    nx.draw(graph, with_labels=True, node_color='skyblue', node_size=500, edge_color='k', linewidths=1, font_size=15)
    plt.savefig(filename)
    plt.close()


# Paramètres pour la génération de graphe
num_vertices1, num_edges1 = 10, 15
num_vertices2, num_edges2 = 10, 15

# Génére deux graphes aléatoires
G1 = generate_random_graph(num_vertices1, num_edges1)
G2 = generate_random_graph(num_vertices2, num_edges2)

# Enregistre les graphes dans des fichiers txt
save_graph_to_file(G1, 'graph1.txt')
save_graph_to_file(G2, 'graph2.txt')

# Enregistre les graphes dans des fichiers png
save_graph_to_png(G1, 'graph1.png')
save_graph_to_png(G2, 'graph2.png')

print("Les graphes ont été générés et enregistrés dans 'graph1.txt', 'graph2.txt', 'graph1.png', et 'graph2.png'.")
