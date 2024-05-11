import networkx as nx
import matplotlib.pyplot as plt


def charger_graphe(fichier):
    G = nx.Graph()
    with open(fichier, 'r') as file:
        for line in file:
            parts = line.strip().split(' : ')
            nodes = parts[0].split(' - ')
            weight = int(parts[1])
            G.add_edge(int(nodes[0]), int(nodes[1]), weight=weight)
    return G


def prim_mst(G):
    # Initialisation
    start_node = list(G.nodes())[0]
    mst = nx.Graph()
    mst.add_node(start_node)

    # Création d'une liste pour gérer les arêtes candidates, initialisée avec les arêtes du nœud de départ
    candidate_edges = [(weight, u, v) for u, v, weight in G.edges(start_node, data='weight')]
    # Tant que le MST n'a pas inclus tous les nœuds
    while len(mst.nodes) < len(G.nodes()):
        # Tri des arêtes candidates par poids
        candidate_edges.sort()
        # Trouve la plus petite arête qui ajoute un nouveau nœud au MST
        for weight, u, v in candidate_edges:
            if v not in mst.nodes or u not in mst.nodes:
                mst.add_edge(u, v, weight=weight)
                new_node = v if u in mst.nodes else u
                # Ajoute les nouvelles arêtes candidats du nouveau nœud
                candidate_edges.extend((G[v][w]['weight'], v, w) for w in G.neighbors(v) if w not in mst.nodes)
                break

    return mst


# Charge le graphe à partir du fichier
G = charger_graphe("graphe_mst_initial.txt")

# Applique l'algorithme de Prim pour trouver le MST
mst = prim_mst(G)

# Affiche le MST dans le terminal
total_weight = sum(weight for u, v, weight in mst.edges(data='weight'))
print("Edges in the Minimum Spanning Tree:")
for u, v, weight in mst.edges(data='weight'):
    print(f"{u} - {v} : {weight}")
print(f"Total weight of MST: {total_weight}")

# Affiche le MST graphiquement
pos = nx.spring_layout(G)
plt.figure(figsize=(10, 10))
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
nx.draw_networkx_edges(G, pos, edgelist=mst.edges(), width=2, edge_color='red')
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in mst.edges(data=True)})
plt.title("Minimum Spanning Tree (MST) via Prim's Algorithm")
plt.show()
