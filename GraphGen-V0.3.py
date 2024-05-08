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
# pathNames= [('A',800), ('B',800),('C',800),('D',800),('E',800),('F',800),('G',800),('H',800)]
# pathNames= [('A',80), ('B',80),('C',80),('D',80),('E',80),('F',80),('G',80),('H',80)]
pathNames= [('A',8), ('B',8),('C',8),('D',8),('E',8),('F',8),('G',8),('H',8)]


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

print("\nNodes",nodeNames[-5:])
print("\nEdges\n",edges[-5:])



start_time = time.time()
G = nx.Graph()
G.add_nodes_from(nodeNames)
G.add_edges_from(edges)
print("\n",G)

# print(G.nodes(data=True)[0]) 
print(G.nodes(data=True)) 

