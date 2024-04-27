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


