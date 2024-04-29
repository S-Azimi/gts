# this is graph generation test by Sasan Azimi using "NetworkX"
# in version 0.2 we want to generate a big graph as simulation of GAS network 
# this graph consist of several main paths with several points

import networkx as nx  # pip install networkx

import matplotlib.pyplot as plt




edges=[]
nodeNames=[]
pathNames= [('A',800), ('B',800),('C',800),('D',800),('E',800),('F',800),('G',800),('H',800)]
pathNames= [('A',80), ('B',80),('C',80),('D',80),('E',80),('F',80),('G',80),('H',80)]
pathNames= [('A',8), ('B',8),('C',8),('D',8),('E',8),('F',8),('G',8),('H',8)]

for path in pathNames:
    for i in range(path[1]+1):
        nodeNames.append(path[0]+str(i))


# generate long paths
for path in pathNames:
    for i in range(path[1]):
        edges.append((path[0]+str(i),path[0]+str(i+1)))
            


print(nodeNames)
print(edges)


G = nx.Graph()
G.add_nodes_from(nodeNames)
G.add_edges_from(edges)
print(G)
G.clear()

nx.draw_networkx(G, width=1)


#--------------------------------------------------------------------

# in a bipartite graph, there is no edges between the group members
# from networkx.algorithms import bipartite
# B= nx.Graph()
# B.add_nodes_from(['A','B','C','D','E'], bipartite=0)
# B.add_nodes_from([1,2,3,4], bipartite=1)
# B.add_edges_from([('A',1),('B',1),('C',1),('C',3),('D',4),('E',1),('A',2),('E',2)])
# print(bipartite.is_bipartite(B))
# edges = B.edges()
# nx.draw_networkx(B, pos=nx.drawing.layout.bipartite_layout(B, ['A','B','C','D','E']), width=2)
# nx.draw_networkx(B, width=4)

# print(edges)
# plt.clf()  # clear plot
# -----------------------------------------------------------------------

# import csv
# from operator import itemgetter
# from networkx.algorithms import community #This part of networkx, for community detection, needs to be imported separately.

# with open('quakers_nodelist.csv', 'r') as nodecsv: # Open the file
#     nodereader = csv.reader(nodecsv) # Read the csv
#     # Retrieve the data (using Python list comprehension and list slicing to remove the header row, see footnote 3)
#     nodes = [n for n in nodereader][1:]

# node_names = [n[0] for n in nodes] # Get a list of only the node names

# with open('quakers_edgelist.csv', 'r') as edgecsv: # Open the file
#     edgereader = csv.reader(edgecsv) # Read the csv
#     edges = [tuple(e) for e in edgereader][1:] # Retrieve the data

# G = nx.Graph()
# G.add_nodes_from(node_names)
# G.add_edges_from(edges)


# nx.draw_networkx(G, width= 3, with_labels=True)

# fell_whitehead_path = nx.shortest_path(G, source="Margaret Fell", target="George Whitehead")

# print("Shortest path between Fell and Whitehead:", fell_whitehead_path)

# # If your Graph has more than one component, this will return False:
# print(nx.is_connected(G))

# # Next, use nx.connected_components to get the list of components,
# # then use the max() command to find the largest one:
# components = nx.connected_components(G)
# largest_component = max(components, key=len)

# # Create a "subgraph" of just the largest component
# # Then calculate the diameter of the subgraph, just like you did with density.
# #

# subgraph = G.subgraph(largest_component)
# diameter = nx.diameter(subgraph)
# print("Network diameter of largest component:", diameter)

# for path in nx.all_simple_paths(G, source="Margaret Fell", target="George Whitehead"):
#     print(path)