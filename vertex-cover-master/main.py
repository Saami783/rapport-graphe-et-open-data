import networkx as nx
import matplotlib.pyplot as plt


def load_graph_from_file(file_path):
    G = nx.Graph()
    with open(file_path, 'r') as file:
        for line in file:
            nodes = line.strip().split(' - ')
            G.add_edge(int(nodes[0]), int(nodes[1]))
    return G


# Fonction pour calculer la couverture de sommets en utilisant l'algorithme LISTRIGHT
def listright_vertex_cover(G):
    # Suppose que L est la liste des nœuds dans l'ordre décroissant pour la démonstration
    L = sorted(G.nodes(), reverse=True)
    C = set()
    # Parcours la liste L de droite à gauche
    for u in reversed(L):
        # Vérifie si 'u' a au moins un voisin à droite qui n'est pas dans 'C'
        right_neighbors = [v for v in G.neighbors(u) if v > u]
        if any(neighbor not in C for neighbor in right_neighbors):
            C.add(u)
    return C


# Charge le graphe
G = load_graph_from_file("graphe_vertex_cover_modifie.txt")

# Calcule la couverture de sommets
vertex_cover_set = listright_vertex_cover(G)

# Affichee les résultats
print("Sommets sélectionnés pour la couverture de sommets :")
print(vertex_cover_set)
print(f"Nombre de sommets dans la couverture : {len(vertex_cover_set)}")

# Visualiser le graphe avec la couverture de sommets mise en évidence
plt.figure(figsize=(10, 10))
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color='orange', node_size=700)
nx.draw_networkx_edges(G, pos, width=1.5)
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
nx.draw_networkx_nodes(G, pos, nodelist=vertex_cover_set, node_color='red', node_size=700)
plt.title('Solution de Couverture de Sommets utilisant LISTRIGHT')
plt.show()
