import networkx as nx;
import matplotlib.pyplot as dibuj;
import random;
from MetodosAuxiliares import *;
from AG import *;

g = nx.Graph();

g.add_edge(1, 2);
g.add_edge(2, 3);
g.add_edge(1, 3);
g.add_edge(2, 4);
g.add_edge(1, 4);
g.add_edge(4, 5);
g.add_edge(1, 6);

print("---------------------------------------------------------")

m = nx.greedy_color(g)
for i in m:
    print(m[i])

print("---------------------------------------------------------")

nx.draw(g, with_labels=True);
print(colores(g))

print("---------------------------------------------------------")



#dibuj.show();

#crea_poblacion()
#print(crea_individuo(1, colores(g)))
print(gc_traducido)
#print(poblacion_inicial)
#print(genera_sucesor())
print(enfriamiento_simulado(4, 0.1, 100, 100))