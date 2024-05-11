import networkx as nx
import matplotlib.pyplot as plt

# Nombre de zones (sommets) dans le graphe
nombre_de_zones = 30

# Créer un graphe aléatoire pour simuler les connexions directes entre les zones
G = nx.erdos_renyi_graph(nombre_de_zones, 0.1)  # La probabilité de lien contrôle la densité du graphe

# Sauvegarde du graphe dans un fichier texte
with open("graphe_coefficient_clustering.txt", "w") as f:
    for (u, v) in G.edges():
        f.write(f"{u} - {v}\n")

# Affichage du graphe pour une vérification visuelle
plt.figure(figsize=(10, 10))
nx.draw(G, with_labels=True, node_color='orange', edge_color='black', font_weight='bold', node_size=700)
plt.title("Graphe initial pour le Coefficient de Clustering")
plt.savefig("graphe_initial.png")
