# This is graph generation test by Sasan Azimi using "NetworkX"
# In version 0.2 I want to generate a big graph as simulation of Gas Dispatching  network
# In version 0.3 I want to add some nodes with so more properties
# This graph consist of several long main paths and there are a few intersection among them

import networkx as nx  # pip install networkx
import matplotlib.pyplot as plt
import random
import string
import time

number_of_str_properties=20
number_of_float_properties=10

len_string_properties=48

plt.rcParams["figure.figsize"] = [120, 120]
edges=[]
nodeNames=[]
pathNames= [('A',800), ('B',800),('C',800),('D',800),('E',800),('F',800),('G',800),('H',800)]
# pathNames= [('A',80), ('B',80),('C',80),('D',80),('E',80),('F',80),('G',80),('H',80)]
# pathNames= [('A',8), ('B',8),('C',8),('D',8),('E',8),('F',8),('G',8),('H',8)]


def gen_rand_properties(name):

    properties={"name": name}
    # add random string properties
    for i in range(number_of_str_properties):
        properties['StrProp_'+ str(i)]= ''.join(random.choices(string.ascii_lowercase, k=len_string_properties))
    
    # add random float properties
    for i in range(number_of_float_properties):
        properties['FloatProp_'+ str(i)]= random.random()
    
    
    return properties

for path in pathNames:
    for i in range(path[1]+1):
        rand_properties= gen_rand_properties(path[0]+str(i))
        # print(rand_properties)
        nodeNames.append(rand_properties)

# generate long paths
for path in pathNames:
    for i in range(path[1]):
        edges.append((path[0]+str(i),path[0]+str(i+1)))
            
# intersection_nodes=[
#     ('A100','B50'),('A300','B500'),('A400','B700'),
#     ('B50','C100'),('B600','C500'),('B700','D600'),
#     ('C200','D400'),('C500','D700'),
#     ('D50','E100'),('D200','E300'),
#     ('E100','F250'),('E400','F300'),('E600','G700'),
#     ('F250','G50'),('F400','G550'),
#     ('G400','H500'),]

# edges.extend(intersection_nodes)

print("len Nodes:  ", len(nodeNames))
print("len edges:  ", len(edges))

# print("\nNodes:  ",nodeNames[-5:])
# print("\nEdges:",edges[-5:])


start_time = time.time()
G = nx.Graph()
# G.add_nodes_from(nodeNames)


for node_info in nodeNames:
    G.add_node(node_info["name"], **node_info)   # use ** to unpack the dictionary


G.add_edges_from(edges)
print("\n\033[93m", G, "\n\033[0m")


# get one node's info
print(G.nodes['A0']) 



# Saving the graph
nx.write_edgelist(G, "graph.edgelist")
nx.write_gml(G, "graph.gml")

print("\n [  %2f seconds  ]\n" % (time.time() - start_time))

# load a graph from gml file
print("\n", "load a graph from gml file...")
H = nx.read_gml('graph.gml')
print("\n\033[93m", H, "\n\033[0m")

print(H.nodes['A0']) 

print("\n [  %2f seconds  ]\n" % (time.time() - start_time))


