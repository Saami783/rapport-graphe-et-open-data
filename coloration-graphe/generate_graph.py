import networkx as nx
import random

from matplotlib import pyplot as plt

# Définition des événements
evenements = ["Event " + str(i) for i in range(1, 11)]

# Création d'un graphe non orienté
G = nx.Graph()

# Ajout des événements comme sommets
G.add_nodes_from(evenements)

# Ajout des arêtes aléatoires pour simuler les conflits de ressources
for i in range(len(evenements)):
    for j in range(i + 1, len(evenements)):
        # Ajouter une arête avec une probabilité de 0.3
        if random.random() < 0.3:
            G.add_edge(evenements[i], evenements[j])

# Sauvegarde du graphe dans un fichier txt
with open("graphe_des_evenements.txt", "w") as f:
    for (u, v) in G.edges():
        f.write(f"{u} - {v}\n")

# Affichage du graphe
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
nx.draw_networkx_edges(G, pos, edge_color='gray')
plt.title("Graphe initial des conflits entre événements")
# plt.show()
