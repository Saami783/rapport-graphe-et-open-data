import networkx as nx
import pulp
import matplotlib.pyplot as plt

# Chargement du graphe à partir de la liste d'arêtes enregistrée
G = nx.read_edgelist('data/sensor_network.edgelist', nodetype=int)

# Récupération des sommets et des arêtes du graphe
nodes = list(G.nodes())
edges = list(G.edges())

# Création d'un problème de programmation linéaire
prob = pulp.LpProblem("Minimum_Dominating_Set", pulp.LpMinimize)

# Création de variables binaires pour chaque sommet
x = pulp.LpVariable.dicts("x", nodes, cat="Binary")

# Fonction objectif : minimiser la somme des \(x_i\) (c'est-à-dire le nombre de sommets dans l'ensemble dominant)
prob += pulp.lpSum(x[i] for i in nodes)

# Contraintes : pour chaque sommet, s'assurer qu'il est dominé (soit en étant dans l'ensemble ou en ayant au moins un
# voisin dans l'ensemble)
for i in nodes:
    prob += (x[i] + pulp.lpSum(x[j] for j in G.neighbors(i)) >= 1), f"Domination_{i}"

# Résolution du problème
prob.solve()

# Extraction de la solution : sommets qui sont dans le minimum dominating set
dominating_set = {i for i in nodes if x[i].varValue == 1}

# Configuration pour la visualisation
rows, cols = 5, 5
pos = {node: (node % cols, node // cols) for node in G.nodes()}

# Préparation de la figure pour la visualisation
plt.figure(figsize=(8, 6))

# Dessin des nœuds, en mettant en évidence ceux dans l'ensemble dominant
nx.draw(G, pos, with_labels=True, node_size=[700 if node in dominating_set else 500 for node in G.nodes()],
        node_color=["yellow" if node in dominating_set else "lightblue" for node in G.nodes()],
        font_size=10, edge_color="gray")

plt.title("Grid Graph with Minimum Dominating Set Highlighted")
plt.show()

# Affichage de la solution
print("Minimum Dominating Set:", dominating_set)
print("Size of the Dominating Set:", len(dominating_set))

# Sauvegarde de la solution dans un fichier
with open("data/dominating_set.txt", "w") as f:
    f.write(f"Minimum Dominating Set: {dominating_set}\\n")
    f.write(f"Size of the Dominating Set: {len(dominating_set)}\\n")