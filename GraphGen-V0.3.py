# This is graph generation test by Sasan Azimi using "NetworkX"
# In version 0.2 I want to generate a big graph as simulation of Gas Dispatching  network
# In version 0.3 I want to add some nodes with so more properties
# This graph consist of several long main paths and there are a few intersection among them

import networkx as nx  # pip install networkx
import matplotlib.pyplot as plt
import time

number_of_str_properties=20
number_of_float_properties=10

let_string_properties=48

plt.rcParams["figure.figsize"] = [120, 120]
edges=[]
nodeNames=[]
pathNames= [('A',800), ('B',800),('C',800),('D',800),('E',800),('F',800),('G',800),('H',800)]
# pathNames= [('A',80), ('B',80),('C',80),('D',80),('E',80),('F',80),('G',80),('H',80)]


def gen_rand_properties():
    properties="p1='test1', p2='test2', p3=12.1, p4=14.23"
    return properties

for path in pathNames:
    for i in range(path[1]+1):
        rand_properties= gen_rand_properties()
        nodeNames.append(path[0]+str(i) +", " +rand_properties)

# generate long paths
for path in pathNames:
    for i in range(path[1]):
        edges.append((path[0]+str(i),path[0]+str(i+1)))
            
intersection_nodes=[
    ('A100','B50'),('A300','B500'),('A400','B700'),
    ('B50','C100'),('B600','C500'),('B700','D600'),
    ('C200','D400'),('C500','D700'),
    ('D50','E100'),('D200','E300'),
    ('E100','F250'),('E400','F300'),('E600','G700'),
    ('F250','G50'),('F400','G550'),
    ('G400','H500'),]

edges.extend(intersection_nodes)

print("len edges:  ", len(edges))

print("\nNodes",nodeNames[-5:])
print("\nEdges",edges[-5:])



start_time = time.time()
G = nx.Graph()
G.add_nodes_from(nodeNames)
G.add_edges_from(edges)
print(G)

# nx.draw_networkx(G, width=1, with_labels=False)

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

start_of_path = 'A0'
end_of_path = 'C800'
sh_path = nx.shortest_path(G, source=start_of_path, target=end_of_path)

print(f"Shortest path between {start_of_path} and {end_of_path}:", sh_path)
print("\n [  %2f seconds  ]\n" % (time.time() - start_time))

# # If the Graph has more than one component, this will return False:
# print(nx.is_connected(G))

# # use nx.connected_components to get the list of components,
# # then use the max() command to find the largest one:
# components = nx.connected_components(G)
# largest_component = max(components, key=len)

# # Create a "subgraph" of just the largest component
# # Then calculate the diameter of the subgraph, just like you did with density.
# #

# subgraph = G.subgraph(largest_component)
# diameter = nx.diameter(subgraph)
# print("Network diameter of largest component:", diameter)

# for path in nx.all_simple_paths(G, source=start_of_path, target=end_of_path):
#     print(len(path))


