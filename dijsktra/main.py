import networkx as nx
import heapq
import pandas as pd


def load_graph_from_file(filename='graph.txt'):
    G = nx.DiGraph()
    with open(filename, 'r') as file:
        for line in file:
            u, v, w = line.strip().split()
            G.add_edge(int(u), int(v), weight=int(w))
    return G


def dijkstra(G, source):
    """ Implémente l'algorithme de Dijkstra pour trouver les chemins les plus courts. """
    distances = {vertex: float('infinity') for vertex in G}
    previous_vertices = {vertex: None for vertex in G}
    distances[source] = 0
    pq = [(0, source)]

    steps = []

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue

        for neighbor in G[current_vertex]:
            weight = G[current_vertex][neighbor]['weight']
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))

        # Save current state of distances and predecessors for each vertex
        step = []
        for v in sorted(G.nodes()):
            step.append(previous_vertices[v] if previous_vertices[v] is not None else 'n/a')
            step.append(distances[v] if distances[v] != float('infinity') else "∞")
        steps.append(step)

    # Create DataFrame from the steps
    columns = []
    for v in sorted(G.nodes()):
        columns.append(f'P[{v}]')
        columns.append(f'D[{v}]')
    step_data = pd.DataFrame(steps, columns=columns)
    return step_data


def main():
    G = load_graph_from_file()
    source = 0
    step_data = dijkstra(G, source)
    print(step_data.to_string(index=False))


if __name__ == "__main__":
    main()
