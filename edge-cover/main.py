import networkx as nx
import matplotlib.pyplot as plt


def load_graph(file_path):
    G = nx.Graph()
    with open(file_path, 'r') as file:
        for line in file:
            u, v = map(int, line.strip().split(' - '))
            G.add_edge(u, v)
    return G


def edge_cover(G):
    uncovered_nodes = set(G.nodes())
    edge_cover_set = []

    while uncovered_nodes:
        max_cover = 0
        selected_edge = None
        for u, v in G.edges():
            current_cover = len({u, v} & uncovered_nodes)
            if current_cover > max_cover:
                selected_edge = (u, v)
                max_cover = current_cover

        if selected_edge:
            edge_cover_set.append(selected_edge)
            uncovered_nodes.difference_update([selected_edge[0], selected_edge[1]])

    return edge_cover_set


def plot_graph(G, edge_set, file_path):
    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))
    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='gray', width=1)
    nx.draw_networkx_edges(G, pos, edgelist=edge_set, edge_color='red', width=2)
    labels = {node: node for node in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels, font_size=12)
    plt.axis('off')
    plt.title("Edge Cover Visualization")
    plt.savefig(file_path)
    # plt.show()


if __name__ == "__main__":
    G = load_graph("graphe_edge_cover.txt")
    edge_set = edge_cover(G)
    print("Arêtes formant la couverture:")
    for edge in edge_set:
        print(f"{edge[0]} - {edge[1]}")
    print("Nombre total d'arêtes utilisées:", len(edge_set))
    plot_graph(G, edge_set, "edge_cover_solution.png")
