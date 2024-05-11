import networkx as nx
import matplotlib.pyplot as plt
import random

# Nombre de sommets dans le graphe
nombre_de_sommets = 24

# Créer un graphe vide
G = nx.Graph()

# Ajoute des sommets au graphe
G.add_nodes_from(range(nombre_de_sommets))

# Ajoute des arêtes pour simuler les connexions entre intersections
for i in range(nombre_de_sommets):
    for j in range(i + 1, nombre_de_sommets):
        if random.random() < 0.1:  # Probabilité de créer une arête
            G.add_edge(i, j)

# Sauvegarde le graphe dans un fichier texte
with open("graphe_edge_cover.txt", "w") as f:
    for u, v in G.edges():
        f.write(f"{u} - {v}\n")

# Affiche le graphe pour une vérification visuelle
plt.figure(figsize=(10, 10))
nx.draw(G, with_labels=True, node_color='orange', edge_color='black', node_size=700)
plt.title("Graphe initial pour la couverture d'arêtes")
# plt.show()
plt.savefig("graphe_edge_cover")
