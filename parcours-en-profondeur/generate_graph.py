import networkx as nx
import matplotlib.pyplot as plt
import random

# Définit le nombre de sommets (entrepôts) dans le graphe
nombre_de_sommets = 20

# Créer un graphe aléatoire pour simuler le réseau de distribution
G = nx.erdos_renyi_graph(nombre_de_sommets, 0.3)  # La probabilité de lien contrôle la densité du graphe

# Sauvegarde le graphe dans un fichier texte
with open("graphe_dfs_initial.txt", "w") as f:
    for (u, v) in G.edges():
        f.write(f"{u} - {v}\n")

# Affiche du graphe pour une vérification visuelle
plt.figure(figsize=(10, 10))
nx.draw(G, with_labels=True, node_color='orange', edge_color='black', font_weight='bold', node_size=700)
plt.title("Graphe initial pour l'analyse de la logistique")
plt.savefig("graphe_initial.png")
plt.show()
