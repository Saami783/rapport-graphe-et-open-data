import networkx as nx
import matplotlib.pyplot as plt


def generate_graph(num_employees, connection_probability):
    """Génère un graphe aléatoire pour simuler un réseau de collaboration entre employés."""
    # Crée un graphe complet
    G = nx.erdos_renyi_graph(n=num_employees, p=connection_probability)
    for (u, v) in G.edges():
        G[u][v]['weight'] = 1  # Assigne un poids pour symboliser une interaction significative
    return G


def save_graph_to_file(graph, filename):
    """Sauvegarde le graphe dans un fichier texte."""
    with open(filename, 'w') as file:
        for u, v, data in graph.edges(data=True):
            file.write(f'{u} {v} {data["weight"]}\n')  # Sauvegarde chaque arête et son poids


def save_graph_to_png(graph, filename):
    """Dessine le graphe et le sauvegarde en format PNG."""
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(graph)  # Utilise le layout Spring pour une meilleure visualisation
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_weight='bold', font_size=9)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=nx.get_edge_attributes(graph, 'weight'))
    plt.title("Network of Employee Collaboration")
    plt.savefig(filename)
    plt.close()


def main():
    num_employees = 10  # Nombre d'employés dans l'entreprise
    connection_probability = 0.5  # Probabilité qu'une interaction significative existe entre deux employés

    # Génère le graphe
    G = generate_graph(num_employees, connection_probability)

    # Sauvegarde le graphe dans un fichier
    text_filename = 'graph.txt'
    save_graph_to_file(G, text_filename)
    print(f"Le graphe a été généré et sauvegardé dans '{text_filename}'.")

    # Sauvegarde le graphe en PNG
    png_filename = 'graph.png'
    save_graph_to_png(G, png_filename)
    print(f"Le graphe a été également sauvegardé en format PNG sous '{png_filename}'.")


main()
