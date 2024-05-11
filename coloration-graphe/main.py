import networkx as nx
import matplotlib.pyplot as plt


def load_graph(file_path):
    G = nx.Graph()
    with open(file_path, "r") as file:
        for line in file:
            nodes = line.strip().split(" - ")
            G.add_edge(nodes[0], nodes[1])
    return G


# Fonction pour appliquer l'algorithme de coloration gloutonne
def greedy_coloring(graph):
    # Initialise la couleur des sommets
    colors = {node: -1 for node in graph.nodes()}  # Aucune couleur n'est assignée initialement
    available = [True] * len(graph.nodes())  # Liste des couleurs disponibles

    # Ordonne les sommets par degré décroissant
    nodes = sorted(graph.nodes(), key=lambda x: -graph.degree(x))

    # Assigne des couleurs
    for node in nodes:
        # Réinitialise la liste des couleurs disponibles
        available = [True] * len(graph.nodes())

        # Vérifie les couleurs des voisins
        for neighbor in graph.neighbors(node):
            if colors[neighbor] != -1:
                available[colors[neighbor]] = False

        # Trouve la première couleur disponible
        color = next(c for c, available in enumerate(available) if available)
        colors[node] = color

    return colors


# Affiche le graphe coloré
def plot_colored_graph(graph, colors):
    pos = nx.spring_layout(graph)
    color_values = [colors[node] for node in graph.nodes()]
    nx.draw(graph, pos, with_labels=True, node_color=color_values, cmap=plt.get_cmap('viridis'), node_size=800)
    plt.show()


# Fonction pour lister les sommets inclus dans chaque couleur
def list_nodes_by_color(colors):
    color_nodes = {}
    for node, color in colors.items():
        if color not in color_nodes:
            color_nodes[color] = []
        color_nodes[color].append(node)
    return color_nodes


# Chemin vers le fichier texte contenant le graphe
file_path = 'graphe_des_evenements.txt'

# Charge et colorie le graphe
G = load_graph(file_path)
colors = greedy_coloring(G)
plot_colored_graph(G, colors)

# Liste les sommets inclus dans chaque couleur
color_nodes = list_nodes_by_color(colors)
for color, nodes in color_nodes.items():
    print(f"Couleur {color}: {nodes}")
