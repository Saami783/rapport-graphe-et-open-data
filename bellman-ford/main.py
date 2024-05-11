def load_graph_from_file(filename, num_vertices):
    graphe = [[float('Inf')] * num_vertices for _ in range(num_vertices)]
    with open(filename, 'r') as file:
        for line in file:
            u, v, w = map(int, line.strip().split())
            graphe[u][v] = w
            if u == v:  # S'il y a des boucles, mettons 0 pour éviter des problèmes
                graphe[u][v] = 0
    return graphe


def BellmanFord(graphe, origine):
    distances = [float("Inf")] * len(graphe)
    predecesseurs = [None] * len(graphe)
    distances[origine] = 0

    print("Démarrage de l'algorithme de Bellman-Ford depuis le sommet source :", origine)
    print("Les arêtes seront considérées dans l'ordre suivant :")
    edges = [(u, v) for u in range(len(graphe)) for v in range(len(graphe)) if graphe[u][v] != float("Inf")]
    print(f"[{', '.join(f'({u}, {v})' for u, v in edges)}]")
    print(" ".join(f"P[{i}]  D[{i}]" for i in range(len(distances))))

    # Afficher l'état initial
    print(" ".join(
        f"{('n/a' if predecesseurs[i] is None else predecesseurs[i]):<4} {('∞' if distances[i] == float('Inf') else distances[i]):<4}"
        for i in range(len(distances))))

    for _ in range(len(graphe) - 1):
        for u in range(len(graphe)):
            for v in range(len(graphe)):
                if graphe[u][v] != float("Inf") and distances[u] + graphe[u][v] < distances[v]:
                    distances[v] = distances[u] + graphe[u][v]
                    predecesseurs[v] = u
                    print(" ".join(
                        f"{('n/a' if predecesseurs[i] is None else predecesseurs[i]):<4} {('∞' if distances[i] == float('Inf') else distances[i]):<4}"
                        for i in range(len(distances))))

    for u in range(len(graphe)):
        for v in range(len(graphe)):
            if graphe[u][v] != float("Inf") and distances[u] + graphe[u][v] < distances[v]:
                print("Le graphe contient un cycle négatif")
                return None, None

    return distances, predecesseurs


if __name__ == '__main__':
    filename = 'graph.txt'
    num_vertices = 10
    graphe = load_graph_from_file(filename, num_vertices)
    distances, predecesseurs = BellmanFord(graphe, 0)
