import networkx as nx


def load_graph_from_file(filename):
    G = nx.Graph()
    with open(filename, 'r') as file:
        for line in file:
            u, v, _ = map(int, line.split())
            G.add_edge(u, v)
    return G


def peut_etendre_clique(current_clique, v, G):
    """ Vérifie si tous les membres de la clique actuelle sont connectés au sommet v """
    return all(G.has_edge(v, u) for u in current_clique)


def DFS_Clique(G, u, current_clique, max_clique):
    """ Explore récursivement pour trouver la plus grande clique """
    current_clique.append(u)
    if len(current_clique) > len(max_clique[0]):
        max_clique[0] = current_clique.copy()
    for v in G.neighbors(u):
        if peut_etendre_clique(current_clique, v, G):
            DFS_Clique(G, v, current_clique, max_clique)
    current_clique.pop()


def recherche_clique_maximale(G):
    max_clique = [[]]
    start_vertex = 4
    if G.has_node(start_vertex):
        DFS_Clique(G, start_vertex, [], max_clique)
    return max_clique[0]


if __name__ == "__main__":
    # Chargement du graphe depuis un fichier
    G = load_graph_from_file('graph.txt')
    max_clique = recherche_clique_maximale(G)
    print("La plus grande clique trouvée a une taille de:", len(max_clique))
    print("Les sommets de la plus grande clique sont:", max_clique)
