import networkx as nx
import pulp
import matplotlib.pyplot as plt


def load_graph_from_file(filename):
    """ Charge un graphe à partir d'un fichier de liste d'adjacence. """
    G = nx.Graph()
    with open(filename, 'r') as file:
        for line in file:
            vertices = line.strip().split()
            u = vertices[0]
            for v in vertices[1:]:
                G.add_edge(u, v)
    return G


def generate_isomorphic_graph(G1, mapping):
    """ Génère un graphe isomorphe basé sur un mapping spécifique. """
    G_iso = nx.relabel_nodes(G1, mapping)
    return G_iso


def is_isomorphic(G1, G2):
    """ Vérifie si deux graphes sont isomorphes en utilisant la programmation linéaire et retourne le mapping si
    c'est le cas."""
    if G1.number_of_nodes() != G2.number_of_nodes() or G1.number_of_edges() != G2.number_of_edges():
        return False, {}

    V1 = list(G1.nodes())
    V2 = list(G2.nodes())
    n = len(V1)

    # Créer le problème de programmation linéaire
    prob = pulp.LpProblem("Graph_Isomorphism", pulp.LpMinimize)

    # Création des variables x_{uv}
    x = pulp.LpVariable.dicts("x", (range(n), range(n)), cat=pulp.LpBinary)

    # Objectif minimiser 0
    prob += 0

    # Contraintes de sommet
    for i in range(n):
        prob += pulp.lpSum(x[i][j] for j in range(n)) == 1
        prob += pulp.lpSum(x[j][i] for j in range(n)) == 1

    # Contraintes d'arête
    for i in range(n):
        for j in range(n):
            if i != j and G1.has_edge(V1[i], V1[j]):
                for k in range(n):
                    for l in range(n):
                        if k != l and G2.has_edge(V2[k], V2[l]):
                            prob += x[i][k] + x[j][l] <= 1

    # Résoudre le problème
    result = prob.solve()
    if pulp.LpStatus[prob.status] == 'Optimal':
        mapping = {V1[i]: V2[j] for i in range(n) for j in range(n) if pulp.value(x[i][j]) == 1}
        return True, mapping
    return False, {}


def save_graph_to_png(graph, filename):
    """ Enregistre le graphe dans un fichier PNG. """
    plt.figure(figsize=(8, 6))
    nx.draw(graph, with_labels=True, node_color='skyblue', node_size=500, edge_color='k', linewidths=1, font_size=15)
    plt.savefig(filename)
    plt.close()


# Charge les graphes à partir des fichiers
G1 = load_graph_from_file('graph1.txt')
G2 = load_graph_from_file('graph2.txt')

# Vérifierl'isomorphisme et générer un graphe isomorphe
isomorphic, mapping = is_isomorphic(G1, G2)
if isomorphic:
    print("Les graphes sont isomorphes.")
    G_iso = generate_isomorphic_graph(G1, mapping)
    save_graph_to_png(G_iso, 'isomorphic_graph.png')
    print("Le graphe isomorphe a été sauvegardé en 'isomorphic_graph.png'.")
else:
    print("Les graphes ne sont pas isomorphes.")
