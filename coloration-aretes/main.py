import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


def load_graph(file_path):
    G = nx.Graph()
    with open(file_path, 'r') as file:
        for line in file:
            u, v = map(int, line.strip().split(' - '))
            G.add_edge(u, v)
    return G


def misra_gries_coloring(G):
    color = {}
    for edge in G.edges():
        color[edge] = 0  # Initialise toutes les couleurs à 0

    for u, v in G.edges():
        used_colors = set()
        # Collecte les couleurs utilisées par les arêtes adjacentes à u et v
        for neighbor in G[u]:
            if (u, neighbor) in color:
                used_colors.add(color[(u, neighbor)])
            if (neighbor, u) in color:
                used_colors.add(color[(neighbor, u)])
        for neighbor in G[v]:
            if (v, neighbor) in color:
                used_colors.add(color[(v, neighbor)])
            if (neighbor, v) in color:
                used_colors.add(color[(neighbor, v)])

        # Trouve la plus petite couleur non utilisée
        new_color = 1
        while new_color in used_colors:
            new_color += 1
        color[(u, v)] = new_color
        color[(v, u)] = new_color

    return color


def plot_graph_with_colors(G, edge_colors):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
    # Liste des couleurs spécifiques pour chaque indice de couleur
    color_map = {
        1: 'yellow',
        2: 'red',
        3: 'green',
        4: 'darkviolet',
        5: 'lightblue',
        6: 'fuchsia'
    }
    max_color = max(edge_colors.values())
    color_list = [color_map.get(edge_colors[edge], 'black') for edge in G.edges()]

    nx.draw_networkx_edges(G, pos, edge_color=color_list, width=2)
    plt.title('Graph with Colored Edges')
    plt.show()


if __name__ == "__main__":
    G = load_graph("reseau_telecom_graphe.txt")
    edge_colors = misra_gries_coloring(G)
    plot_graph_with_colors(G, edge_colors)
