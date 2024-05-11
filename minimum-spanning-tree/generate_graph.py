import networkx as nx
import matplotlib.pyplot as plt
import random

# Nombre de points (zones/carrefours) dans le graphe
nombre_de_points = 20

# Créer un graphe complet (chaque point est connecté à chaque autre point)
G = nx.complete_graph(nombre_de_points)

# Attribue un poids aléatoire à chaque arête pour simuler les coûts d'installation
for (u, v) in G.edges():
    G.edges[u, v]['weight'] = random.randint(1, 100)

# Sauvegarde le graphe dans un fichier texte
with open("graphe_mst_initial.txt", "w") as f:
    for (u, v, w) in G.edges(data=True):
        f.write(f"{u} - {v} : {w['weight']}\n")

# Affichage du graphe pour vérification visuelle
pos = nx.spring_layout(G)
plt.figure(figsize=(10, 10))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): w['weight'] for u, v, w in G.edges(data=True)})
plt.title("Graphe initial pour MST")
plt.savefig("graphe_initial_mst.png")
plt.show()
