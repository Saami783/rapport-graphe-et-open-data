import networkx as nx


def load_graph(file_path):
    G = nx.read_edgelist(file_path, nodetype=int)
    return G


def greedy_maximum_independent_set(G):
    """
    Trouve un ensemble indépendant maximum en utilisant une approche gloutonne.

    :param G: Graph NetworkX.
    :return: Ensemble indépendant maximum.
    """
    sorted_nodes = sorted(G.nodes(), key=lambda x: G.degree(x))
    independent_set = set()

    while sorted_nodes:
        v = sorted_nodes.pop(0)  # Sélectionner le sommet avec le plus petit degré
        if all(neigh not in independent_set for neigh in G.neighbors(v)):
            independent_set.add(v)
            # Retire les voisins de v et v lui-même de la liste à considérer
            sorted_nodes = [node for node in sorted_nodes if node not in G.neighbors(v) and node != v]

    return independent_set


# Chemin vers le fichier de graphe
file_path = "mnt/data/social_graph.txt"

G = load_graph(file_path)

# Trouve l'ensemble indépendant maximum
independent_set = greedy_maximum_independent_set(G)

# Affiche les résultats
print("Ensemble indépendant maximum trouvé:")
print(independent_set)
print("Nombre de sommets dans l'ensemble:", len(independent_set))
