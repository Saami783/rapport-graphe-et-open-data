import networkx as nx
import matplotlib.pyplot as plt
import random
from itertools import permutations

# Définit des villes
villes = ["Fontainebleau", "Nanterre", "Poissy", "Mantes-la-Jolie", "Evreux"]

# Créer d'un graphe non orienté complet
G = nx.complete_graph(len(villes))

# Attribue des noms aux sommets du graphe
for idx, ville in enumerate(villes):
    G.nodes[idx]['name'] = ville

# Attribue des poids aléatoires aux arêtes du graphe
for (u, v) in G.edges():
    G.edges[u, v]['weight'] = random.randint(1, 100)

# Sauvegarde du graphe dans un fichier txt
with open("graphe_des_villes_reduit.txt", "w") as f:
    for (u, v, w) in G.edges(data=True):
        f.write(f"{villes[u]} - {villes[v]} : {w['weight']}\n")

# Affiche du graphe initial
pos = nx.spring_layout(G)  # Position des noeuds suivant un layout "spring"
plt.figure(figsize=(8, 8))
nx.draw(G, pos, with_labels=False, node_color='lightblue', node_size=4000, edge_color='gray')
labels = nx.get_node_attributes(G, 'name')
nx.draw_networkx_labels(G, pos, labels=labels)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): w['weight'] for u, v, w in G.edges(data=True)})
plt.title("Graphe initial des villes")
plt.show()

# Calcul toutes les permutations possibles des indices des villes
all_permutations = list(permutations(range(len(villes))))

# Calcul la longueur totale pour chaque permutation et garder la plus courte
min_distance = float('inf')
best_path = None

for perm in all_permutations:
    current_distance = 0
    for i in range(len(perm) - 1):
        current_distance += G.edges[perm[i], perm[i + 1]]['weight']
    # Ajoute le retour à la ville de départ pour compléter le circuit
    current_distance += G.edges[perm[-1], perm[0]]['weight']

    if current_distance < min_distance:
        min_distance = current_distance
        best_path = perm

# Affiche le meilleur chemin et sa distance
print("Itinéraire le plus court: " + " -> ".join(G.nodes[idx]['name'] for idx in best_path) + " -> " +
      G.nodes[best_path[0]]['name'])
print("Distance minimale:", min_distance)

# Affiche graphique du meilleur chemin
plt.figure(figsize=(8, 8))
nx.draw(G, pos, with_labels=False, node_color='lightblue', node_size=4000, edge_color='gray')
nx.draw_networkx_labels(G, pos, labels=labels)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): w['weight'] for u, v, w in G.edges(data=True)})

# Colorie les arêtes du chemin optimal
for i in range(len(best_path)):
    u = best_path[i]
    v = best_path[(i + 1) % len(best_path)]  # modulo pour connecter à la ville de départ à la fin
    nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], width=2, edge_color='red')

plt.title("Meilleur itinéraire TSP")
plt.show()
