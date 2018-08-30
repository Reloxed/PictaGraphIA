import networkx as nx

"""
Este método nos devuelve el número máximo de colores a utilizar
en el algoritmo, observando cual es el nodo con mayor número de
vecinos y sumando uno a dicho número.
"""
def colores(g):
    v = 0
    for i in nx.nodes(g):
        if(v < nx.degree(g, i)):
            v = nx.degree(g, i)
    return v + 1

def numero_colores_usados(individuo):
    colores = set(individuo)
    return len(colores)