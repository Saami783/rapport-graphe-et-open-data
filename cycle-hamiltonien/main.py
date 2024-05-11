import networkx as nx
import matplotlib.pyplot as plt
import random


def load_graph_from_file(filename):
    G = nx.Graph()
    with open(filename, 'r') as file:
        for line in file:
            u, v, w = line.strip().split()
            G.add_edge(int(u), int(v), weight=int(w))
    return G


def initialize_heuristic_cycle(graph):
    """Initialise un cycle basé sur l'heuristique du plus proche voisin."""
    nodes = list(graph.nodes())
    start = random.choice(nodes)
    cycle = [start]
    unvisited = set(nodes)
    unvisited.remove(start)

    current = start
    while unvisited:
        next_node = min(unvisited, key=lambda x: graph[current][x]['weight'])
        cycle.append(next_node)
        unvisited.remove(next_node)
        current = next_node
    cycle.append(start)  # Revenir au point de départ pour fermer le cycle
    return cycle, start


def two_opt_swap(cycle, i, k):
    """Applique un 2-opt swap sur le cycle."""
    new_cycle = cycle[:i] + cycle[i:k + 1][::-1] + cycle[k + 1:]
    return new_cycle


def improve_cycle_with_two_opt(graph, cycle):
    """Améliore le cycle en utilisant l'échange 2-opt."""
    improved = True
    while improved:
        improved = False
        for i in range(1, len(cycle) - 2):
            for k in range(i + 1, len(cycle) - 1):
                new_cycle = two_opt_swap(cycle, i, k)
                if cycle_cost(graph, new_cycle) < cycle_cost(graph, cycle):
                    cycle = new_cycle
                    improved = True
    return cycle


def cycle_cost(graph, cycle):
    """Calcule le coût total du cycle."""
    cost = sum(graph[cycle[i]][cycle[i + 1]]['weight'] for i in range(len(cycle) - 1))
    return cost


def plot_cycle(graph, cycle):
    """Dessine le cycle sur le graphe en montrant les pondérations de toutes les arêtes."""
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=16)
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    path_edges = list(zip(cycle[:-1], cycle[1:]))
    nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color='r', width=2)
    plt.savefig("graph_solution.png")
    plt.show()


def main():
    G = load_graph_from_file('graph.txt')
    initial_cycle, start_vertex = initialize_heuristic_cycle(G)
    optimized_cycle = improve_cycle_with_two_opt(G, initial_cycle)
    plot_cycle(G, optimized_cycle)
    print("Sommet de départ:", start_vertex)
    print("Cycle initial:", initial_cycle)
    print("Cycle optimisé:", optimized_cycle)


main()
