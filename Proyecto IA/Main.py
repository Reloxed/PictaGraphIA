import networkx as nx;
import matplotlib.pyplot as dibuj;
from MetodosAuxiliares import *;

g = nx.Graph();
g.add_edge(1, 2);
g.add_edge(2, 3);
g.add_edge(1, 3);
g.add_edge(2, 4);
g.add_edge(1, 4);
g.add_edge(4, 5);
g.add_edge(1, 6);

nx.draw(g, with_labels=True);
print(min_colores(g))

dibuj.show();