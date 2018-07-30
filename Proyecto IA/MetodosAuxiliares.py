import networkx as nx;
import matplotlib as mpl;

"""
Este método nos devuelve el número de colores mínimo
para colorear el grafo en cuestión, observando cual
es el nodo con mayor número de vecinos y sumando
uno a dicho número.
"""
def min_colores(g):
    v = 0;
    for i in nx.nodes(g):
        if(v<nx.degree(g, i)):
            v = nx.degree(g, i)
    return v+1