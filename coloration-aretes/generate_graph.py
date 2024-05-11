import networkx as nx
import random
import matplotlib.pyplot as plt

# Nombre de nœuds dans le réseau de télécommunications
nombre_de_noeuds = 15

# Probabilité de créer une arête entre deux nœuds
probabilite_de_lien = 0.2

# Création d'un graphe vide
G = nx.Graph()

# Ajout des nœuds au graphe
G.add_nodes_from(range(nombre_de_noeuds))

# Ajout des arêtes pour simuler les connexions entre nœuds
for i in range(nombre_de_noeuds):
    for j in range(i + 1, nombre_de_noeuds):
        if random.random() < probabilite_de_lien:
            G.add_edge(i, j)

# Sauvegarde du graphe dans un fichier texte
with open("reseau_telecom_graphe.txt", "w") as f:
    for u, v in G.edges():
        f.write(f"{u} - {v}\n")

# Affichage du graphe pour une vérification visuelle

plt.figure(figsize=(10, 10))
pos = nx.spring_layout(G)  # Utilise l'agencement spring pour une meilleure visualisation
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='black', font_weight='bold', node_size=700)
plt.title("Graphe initial du réseau de télécommunications")
plt.savefig("graph_initial")
# plt.show()
