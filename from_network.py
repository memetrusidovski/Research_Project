import networkx as nx
import random
import dimod

G = nx.generators.complete_graph(4)
for node in G.nodes:
    G.nodes[node]['bias'] = random.choice([1,-1])
for edge in G.edges:
    G.edges[edge]['quadratic'] = random.choice([1,-1])
bqm = dimod.from_networkx_graph(G,
                                vartype='BINARY',
                                edge_attribute_name='quadratic')