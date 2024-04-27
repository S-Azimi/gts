# this is graph generation test by Sasan Azimi using "NetworkX"

import networkx as nx  # pip install networkx

import matplotlib.pyplot as plt

G= nx.Graph()

G.add_edge('A','B',weight =13, relation = 'friend')
G.add_edge('B','C',weight =9, relation = 'family')
G.add_edge('B','D',weight =7, relation = 'friend')
G.add_edge('E','B',weight =13, relation = 'friend')
G.add_edge('E','A',weight =13, relation = 'enemy')
G.add_edge('F','B',weight =13, relation = 'family')
G.edges(data=True)
G.add_node('A', role='Trader')
G.add_node('B', role='Analyst')
G.add_node('C', role='Manager')
G.nodes(data=True)

# nx.draw_networkx(G, with_labels=True)

from networkx.algorithms import bipartite
B= nx.Graph()
B.add_nodes_from(['A','B','C','D','E'], bipartite=0)
B.add_nodes_from([1,2,3,4], bipartite=1)
B.add_edges_from([('A',1),('B',1),('C',1),('C',3),('D',4),('E',1),('A',2),('E',2)])
print(bipartite.is_bipartite(B))
edges = B.edges()
# nx.draw_networkx(B, pos=nx.drawing.layout.bipartite_layout(B, ['A','B','C','D','E']), width=2)
nx.draw_networkx(B, width=4)

print(edges)