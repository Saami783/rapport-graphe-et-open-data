import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Fixe la graine aléatoire pour la reproductibilité
np.random.seed(42)

# Crée un graphe grille aléatoire (5x5 pour simplifier)
rows, cols = 5, 5
G = nx.grid_2d_graph(rows, cols)

# Converti les coordonnées des nœuds en étiquettes
mapping = {(i, j): i * cols + j for i, j in G.nodes()}
G = nx.relabel_nodes(G, mapping)

# Sauvegarde la liste des arêtes du graphe dans un fichier
edge_file_path = 'data/sensor_network.edgelist'
nx.write_edgelist(G, edge_file_path, data=False)

# Visualiser le graphe
plt.figure(figsize=(8, 6))

# Dessine le graphe avec les nœuds positionnés selon un agencement en grille
pos = {node: (node % cols, node // cols) for node in G.nodes()}
nx.draw(G, pos, with_labels=True, node_size=500, node_color="lightblue", font_size=10, edge_color="gray")

plt.title("Visualisation du graphe grille")
plt.show()
