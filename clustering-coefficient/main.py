import networkx as nx


def charger_graphe(fichier):
    G = nx.Graph()
    with open(fichier, 'r') as file:
        for line in file:
            nodes = line.strip().split(' - ')
            G.add_edge(int(nodes[0]), int(nodes[1]))
    return G


def calcul_coefficient_clustering(G):
    C_moyen = 0
    for v in G.nodes():
        voisins = list(G.neighbors(v))
        n_v = len(voisins)
        E_v = 0

        # Compte les arêtes entre les voisins de v
        for i in range(n_v):
            for j in range(i + 1, n_v):
                if G.has_edge(voisins[i], voisins[j]):
                    E_v += 1

        # Calcul le coefficient de clustering pour le sommet v
        if n_v > 1:
            C_v = (2 * E_v) / (n_v * (n_v - 1))
        else:
            C_v = 0
        C_moyen += C_v

    # Calcul le coefficient de clustering moyen
    C_moyen /= len(G.nodes())
    return C_moyen


G = charger_graphe("graphe_coefficient_clustering.txt")
resultat = calcul_coefficient_clustering(G)
print("Coefficient de clustering moyen:", resultat)
