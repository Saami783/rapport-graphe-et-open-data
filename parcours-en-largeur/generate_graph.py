import networkx as nx
import matplotlib.pyplot as plt
import random

# Nombre de points de passage (sommets) dans le labyrinthe
nombre_de_points = 30

# Création d'un graphe vide
G = nx.Graph()

# Ajout des sommets au graphe
G.add_nodes_from(range(nombre_de_points))

# Ajout des arêtes pour simuler un labyrinthe complexe
for i in range(nombre_de_points):
    for j in range(i + 1, nombre_de_points):
        if random.random() < 0.1:  # Probabilité de créer une arête
            G.add_edge(i, j)

# Sauvegarde du graphe dans un fichier texte sans pondération
with open("labyrinthe_graphe.txt", "w") as f:
    for (u, v) in G.edges():
        f.write(f"{u} - {v}\n")

# Affichage du graphe pour une vérification visuelle
plt.figure(figsize=(10, 10))
pos = nx.spring_layout(G)  # Positionnement des noeuds suivant un layout "spring"
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='black', font_weight='bold', node_size=700)
plt.title("Graphe initial du labyrinthe sans pondération")
plt.savefig("graphe_initial.png")
plt.show()
