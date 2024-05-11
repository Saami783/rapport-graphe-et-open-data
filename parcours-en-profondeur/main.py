import networkx as nx


def charger_graphe(fichier):
    G = nx.Graph()
    with open(fichier, 'r') as file:
        for line in file:
            # Sépare les nœuds par le délimiteur ' - ' et ajoute une arête entre eux
            nodes = line.strip().split(' - ')
            G.add_edge(int(nodes[0]), int(nodes[1]))
    return G


# Visite un nœud dans l'ordre DFS
def dfs_visit(G, u, couleur, pere, debut, fin, temps):
    temps[0] += 1
    debut[u] = temps[0]
    couleur[u] = 'Gris'  # Marquer le nœud comme en cours de visite
    # Parcours tous les voisins du nœud
    for v in G.neighbors(u):
        if couleur[v] == 'Blanc':  # Si le voisin n'a pas été visité
            pere[v] = u  # Définit le nœud courant comme parent du voisin
            dfs_visit(G, v, couleur, pere, debut, fin, temps)  # Visite récursive du voisin
    couleur[u] = 'Noir'  # Marque le nœud comme complètement visité
    temps[0] += 1  # Incrémente le temps à la fin de la visite
    fin[u] = temps[0]  # Marque le temps de fin pour le nœud


# Fonction principale pour appliquer le DFS sur tout le graphe
def dfs(G):
    # Initialisation des couleurs, parents, temps de début et fin pour chaque nœud
    couleur = {u: 'Blanc' for u in G.nodes()}
    pere = {u: None for u in G.nodes()}
    debut = {}
    fin = {}
    temps = [0]

    # Parcours tous les nœuds du graphe
    for u in G.nodes():
        if couleur[u] == 'Blanc':  # Si le nœud n'a pas été visité
            dfs_visit(G, u, couleur, pere, debut, fin, temps)  # Effectuer DFS à partir de ce nœud

    return pere, debut, fin  # pour chaque nœud


G = charger_graphe("graphe_dfs_initial.txt")

pere, debut, fin = dfs(G)

print("Père:", pere)
print("Début:", debut)
print("Fin:", fin)
