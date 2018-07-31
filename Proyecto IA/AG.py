import random
import networkx as nx
from MetodosAuxiliares import *
from Main import *

tam = 10 # Número de individuos por población
largo = nx.number_of_nodes(g) # Longitud de la lista
gc_modelo = nx.greedy_color(g) # Coloreado óptimo del grafo
presion = 3 # Número de individuos que se seleccionan para la evolución
posibilidad_mutacion = 0.2 # Probabilidad de que un individuo mute

"""
Crea un individuo
"""
def crea_individuo(min, max):
    return[random.randint(min, max) for i in range(largo)]

"""
Crea una población
"""
def crea_poblacion():
    return [crea_individuo(1, colores(g)) for i in range(tam)]

"""
Calcula el fitness para un individuo
"""
def calcula_fitness(individuo):
    fitness = 0
    for i in range(len(gc_modelo)):
        if crea_individuo[i] != gc_modelo[i]:
            fitness += 1
    return fitness

'''
1. Se puntúan todos los elementos de la población y nos quedamos con los mejores (se guardan en 'seleccionados').
2. Se mezclan los elegidos para crear nuevos individuos
'''
def seleccion(poblacion):
    puntuados = [(calcula_fitness(i), i) for i in poblacion]
    puntuados = [i[1] for i in sorted(puntuados)]

    seleccionados = puntuados[(len(puntuados) - presion)]

    return seleccionados
