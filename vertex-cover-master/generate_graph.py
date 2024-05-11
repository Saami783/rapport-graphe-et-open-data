import networkx as nx
import matplotlib.pyplot as plt
import random

# Nombre de sommets dans le graphe
nombre_de_sommets = 100
probabilite_de_lien = 0.1

# Créer un graphe aléatoire pour représenter toutes les zones possibles à couvrir
G = nx.erdos_renyi_graph(nombre_de_sommets, probabilite_de_lien)

# Sauvegarde du graphe dans un fichier texte
with open("graphe_vertex_cover_modifie.txt", "w") as f:
    for (u, v) in G.edges():
        f.write(f"{u} - {v}\n")

plt.figure(figsize=(10, 10))
nx.draw(G, with_labels=True, node_color='orange', edge_color='black', font_weight='bold', node_size=700)
plt.title("Graphe initial modifié pour Vertex Cover")
plt.show()
