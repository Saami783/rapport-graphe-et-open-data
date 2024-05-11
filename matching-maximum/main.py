import networkx as nx

# Chargement du graphe à partir du fichier txt
B = nx.read_adjlist('graphe_covoiturage.txt', nodetype=str, delimiter=' - ')

# Calcul du maximum matching en utilisant l'algorithme de Hopcroft-Karp
matching = nx.bipartite.maximum_matching(B)

# Affichage du résultat du matching
print("Matching maximum trouvé :")
for key, value in matching.items():
    print(f"{key} -> {value}")

# Affichage graphique du résultat avec les arêtes du matching colorées
import matplotlib.pyplot as plt

# Préparation des positions et des couleurs pour le graphe
pos = nx.bipartite_layout(B, [node for node in B.nodes() if node.startswith('Conducteur')])
colors = ['green' if (u, v) in matching.items() or (v, u) in matching.items() else 'red' for u, v in B.edges()]

# Dessin du graphe
nx.draw(B, pos, with_labels=True, edge_color=colors, node_color=['skyblue' if 'Conducteur' in node else 'lightgreen' for node in B])
plt.title("Graphe avec Matching Maximum Visualisé")
plt.show()
