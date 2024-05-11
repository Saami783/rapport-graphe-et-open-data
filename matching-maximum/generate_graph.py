import networkx as nx
import random
import matplotlib.pyplot as plt

# Création d'un graphe biparti
B = nx.Graph()

# Définition des conducteurs et des passagers
conducteurs = ['Conducteur{}'.format(i) for i in range(5)]
passagers = ['Passager{}'.format(i) for i in range(5)]

# Ajout des conducteurs et des passagers au graphe
B.add_nodes_from(conducteurs, bipartite=0)
B.add_nodes_from(passagers, bipartite=1)

# Ajout des arêtes entre conducteurs et passagers avec des poids aléatoires
for conducteur in conducteurs:
    for passager in passagers:
        if random.random() > 0.5:  # Création d'une arête avec une probabilité de 50%
            B.add_edge(conducteur, passager, weight=random.randint(1, 10))

# Sauvegarde du graphe dans un fichier txt
with open('graphe_covoiturage.txt', 'w') as f:
    for line in nx.generate_adjlist(B, delimiter=' - '):
        f.write(line + '\n')

pos = nx.bipartite_layout(B, conducteurs)
nx.draw(B, pos, with_labels=True, node_color=['skyblue' if node in conducteurs else 'lightgreen' for node in B])
# plt.show()
