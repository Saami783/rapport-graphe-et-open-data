import networkx as nx
from collections import deque


def load_graph(file_path):
    G = nx.Graph()
    with open(file_path, 'r') as file:
        for line in file:
            # Conversion des identifiants de nœuds en entiers et ajout d'une arête
            u, v = map(int, line.strip().split(' - '))
            G.add_edge(u, v)
    return G


# Fonction pour appliquer le parcours en largeur
def bfs(G, start_node):
    # Initialiser les couleurs, distances et parents
    color = {node: 'white' for node in G.nodes()}
    distance = {node: float('inf') for node in G.nodes()}
    parent = {node: None for node in G.nodes()}
    queue = deque([start_node])  # Utiliser une queue pour gérer les nœuds à explorer

    # Initialisation du nœud de départ
    color[start_node] = 'gray'
    distance[start_node] = 0

    # Tant qu'il y a des nœuds à explorer
    while queue:
        u = queue.popleft()
        for v in G.neighbors(u):
            if color[v] == 'white':  # Si le nœud n'a pas encore été exploré
                color[v] = 'gray'
                distance[v] = distance[u] + 1
                parent[v] = u
                queue.append(v)
        color[u] = 'black'  # Marque le nœud comme complètement exploré

    return parent, distance


# Trouve le chemin en utilisant le tableau des parents
def find_path(parents, start, end):
    path = []
    step = end
    while step is not None:
        path.append(step)
        step = parents[step]
    path.reverse()  # Pour obtenir le chemin dans l'ordre correct du début à la fin
    return path


# Affiche les résultats du BFS
def print_final_results(parent, distance, start_node):
    print(f"Résultats du BFS à partir du nœud {start_node}:\n")

    nodes_str = "Sommet    : "
    parents_str = "Parent  : "
    distances_str = "Distance: "

    for node in sorted(parent.keys()):
        nodes_str += str(node) + ", "
        parent_value = "None" if parent[node] is None else str(parent[node])
        parents_str += parent_value + ", "
        distances_str += str(distance[node]) + ", "

    nodes_str = nodes_str.rstrip(", ")
    parents_str = parents_str.rstrip(", ")
    distances_str = distances_str.rstrip(", ")

    print(nodes_str)
    print(parents_str)
    print(distances_str)


if __name__ == "__main__":
    G = load_graph("labyrinthe_graphe.txt")  # Charge le graphe
    start_node = 1
    parent, distance = bfs(G, start_node)  # Exécute BFS
    print_final_results(parent, distance, start_node)
    path = find_path(parent, start_node, 29)  # Trouve un chemin spécifique

    print("Chemin le plus court du sommet", start_node, "au sommet 29:", path)
