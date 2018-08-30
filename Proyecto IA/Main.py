import networkx as nx;
import matplotlib.pyplot as dibuj;
import random;
from MetodosAuxiliares import *;
from AG import *;

g = nx.Graph();

g.add_edge(0, 1);
g.add_edge(1, 2);
g.add_edge(0, 2);
g.add_edge(1, 3);
g.add_edge(0, 3);
g.add_edge(3, 4);
g.add_edge(0, 5);

print("---------------------------------------------------------")

m = nx.greedy_color(g)
for i in m:
    print(m[i])

print("---------------------------------------------------------")

nx.draw(g, with_labels=True);
print(colores(g))

print("---------------------------------------------------------")

#print(numero_colores_usados(crea_individuo(1, colores(g))))

dibuj.show();

#crea_poblacion()
#print(crea_individuo(1, colores(g)))
#print(gc_traducido)
#print(poblacion_inicial)
#print(genera_sucesor())
print(enfriamiento_simulado(100, 0.95, 100, 100))
#print(otro_fitness(crea_individuo(1, colores(g))))