import networkx as nx
import random
import matplotlib.pyplot as plt


def generate_complete_graph(num_vertices):
    """Génère un graphe complet avec des poids aléatoires sur les arêtes."""
    G = nx.complete_graph(num_vertices)
    for u, v in G.edges():
        G[u][v]['weight'] = random.randint(1, 100)  # Poids aléatoires entre 1 et 100
    return G


def save_graph_to_file(graph, filename):
    """Sauvegarde le graphe dans un fichier texte."""
    with open(filename, 'w') as f:
        for u, v, data in graph.edges(data=True):
            f.write(f'{u} {v} {data["weight"]}\n')


def save_graph_to_png(graph, filename):
    """Dessine et sauvegarde le graphe dans un fichier PNG."""
    pos = nx.spring_layout(graph)  # Utilise layout pour une meilleure visualisation
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw(graph, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=15, font_color='darkred')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.savefig(filename)
    plt.close()


def main():
    num_vertices = 5  # Nombre de destinations
    graph = generate_complete_graph(num_vertices)
    save_graph_to_file(graph, 'graph.txt')
    save_graph_to_png(graph, 'graph.png')
    print("Le graphe a été généré et enregistré dans 'graph.txt' et 'graph.png'.")


main()
