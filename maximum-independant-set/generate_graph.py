import networkx as nx


def generate_social_graph(num_users, connection_prob):
    """
    Génère un graphe d'utilisateurs pour un réseau social.

    :param num_users: Nombre d'utilisateurs (sommets) dans le graphe.
    :param connection_prob: Probabilité qu'une arête (relation) existe entre deux utilisateurs.
    :return: Un graphe NetworkX.
    """
    # Créer un graphe aléatoire avec le modèle Erdős-Rényi
    social_graph = nx.erdos_renyi_graph(n=num_users, p=connection_prob)

    # Dessine le graphe
    # plt.figure(figsize=(14, 10))
    # nx.draw_networkx(social_graph, node_size=20, node_color='blue', with_labels=False)
    # plt.title("Graphe d'utilisateurs dans un réseau social")
    # plt.show()

    # Sauvegarde le graphe dans un fichier texte
    file_path = "mnt/data/social_graph.txt"
    nx.write_edgelist(social_graph, file_path, data=False)

    return social_graph


# Paramètres
num_users = 15000  # Nombre d'utilisateurs dans le graphe
connection_prob = 0.00025  # Probabilité de connexion entre les utilisateur

# Génére et affiche le graphe
social_graph = generate_social_graph(num_users, connection_prob)
