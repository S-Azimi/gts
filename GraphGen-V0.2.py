# this is graph generation test by Sasan Azimi using "NetworkX"
# in version 0.2 we want to generate a big graph as simulation of GAS network 
# this graph consist of several main paths with several points

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

#--------------------------------------------------------------------

# in a bipartite graph, there is no edges between the group members
from networkx.algorithms import bipartite
B= nx.Graph()
B.add_nodes_from(['A','B','C','D','E'], bipartite=0)
B.add_nodes_from([1,2,3,4], bipartite=1)
B.add_edges_from([('A',1),('B',1),('C',1),('C',3),('D',4),('E',1),('A',2),('E',2)])
print(bipartite.is_bipartite(B))
edges = B.edges()
nx.draw_networkx(B, pos=nx.drawing.layout.bipartite_layout(B, ['A','B','C','D','E']), width=2)
# nx.draw_networkx(B, width=4)

print(edges)
plt.clf()  # clear plot
# -----------------------------------------------------------------------

import csv
from operator import itemgetter
from networkx.algorithms import community #This part of networkx, for community detection, needs to be imported separately.

with open('quakers_nodelist.csv', 'r') as nodecsv: # Open the file
    nodereader = csv.reader(nodecsv) # Read the csv
    # Retrieve the data (using Python list comprehension and list slicing to remove the header row, see footnote 3)
    nodes = [n for n in nodereader][1:]

node_names = [n[0] for n in nodes] # Get a list of only the node names

with open('quakers_edgelist.csv', 'r') as edgecsv: # Open the file
    edgereader = csv.reader(edgecsv) # Read the csv
    edges = [tuple(e) for e in edgereader][1:] # Retrieve the data

G = nx.Graph()
G.add_nodes_from(node_names)
G.add_edges_from(edges)


nx.draw_networkx(G, width= 3, with_labels=True)

fell_whitehead_path = nx.shortest_path(G, source="Margaret Fell", target="George Whitehead")

print("Shortest path between Fell and Whitehead:", fell_whitehead_path)

# If your Graph has more than one component, this will return False:
print(nx.is_connected(G))

# Next, use nx.connected_components to get the list of components,
# then use the max() command to find the largest one:
components = nx.connected_components(G)
largest_component = max(components, key=len)

# Create a "subgraph" of just the largest component
# Then calculate the diameter of the subgraph, just like you did with density.
#

subgraph = G.subgraph(largest_component)
diameter = nx.diameter(subgraph)
print("Network diameter of largest component:", diameter)

for path in nx.all_simple_paths(G, source="Margaret Fell", target="George Whitehead"):
    print(path)