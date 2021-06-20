import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()
pos = {
        1: (1, 1),
        2: (1.5, 1.1),
        3: (1.5, 1),
        4: (2.2, 1.1),
        5: (2.4, 1.1)
        }
N=[1,2,3,4,5]
E= [(1,2),(2,3),(3,4),(4,5),(5,3)]
G.add_nodes_from(N)
G.add_edges_from(E)

# nx.draw_networkx(G, pos=pos, node_color='c')
# plt.show()

eigen_centers = nx.eigenvector_centrality_numpy(G)
print(eigen_centers)

