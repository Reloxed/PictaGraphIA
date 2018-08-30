import random
import networkx as nx
from MetodosAuxiliares import *
#from Main import *

g = nx.Graph();

g.add_edge(0, 1);
g.add_edge(1, 2);
g.add_edge(0, 2);
g.add_edge(1, 3);
g.add_edge(0, 3);
g.add_edge(3, 4);
g.add_edge(0, 5);

tam = 100000 # Número de individuos por población
largo = nx.number_of_nodes(g) # Longitud de la lista
presion = 3 # Número de individuos que se seleccionan para la evolución

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

poblacion_inicial = crea_poblacion();

"""
Calcula el fitness para un individuo
"""
def calcula_fitness(individuo):
    fitness = 0
    for i in range(len(gc_modelo)):
        individuocreado = poblacion_inicial[i]
        if individuocreado[i] != gc_traducido:
            fitness += 1000
    return fitness


def fitness_nuevo(individuo):
    fitness = 0
    coloresusados = []
    for i in range(len(individuo)):
        for j in individuo:
            if not(coloresusados.__contains__(individuo[j])):
                coloresusados.append(individuo[j])
    print(coloresusados)
    if len(coloresusados) > 3:
        fitness += 10000
    return fitness


def otro_fitness(individuo):
    fitness = 0
    #print(individuo)
    #print(numero_colores_usados(individuo))
    for i in range(0, len(individuo)):
        if numero_colores_usados(individuo) > 3:
           fitness += 10000
        #print('Iteración ' + str(i) + ':')
        vecinos = list(nx.neighbors(g, i))
        #print('Los vecinos de ' + str(i) + ' son ' + str(vecinos) + '\n')
        for j in range(len(vecinos)):
            #print('La posición ' + str(j) + ' de la lista de vecinos de ' + str(i) + ' es ' + str(vecinos[j]) + '\ny se compara con la posición ' + str(i) + ' para comprobar\nque sus colores sean distintos\n')
            if individuo[i] == individuo[vecinos[j]]:
                fitness += 10000
                #print('Como ' + str(i) + ' tiene el mismo color que su nodo vecino ' + str(vecinos[j]) + ', se suma 1000 al fitness, que actualmente es ' + str(fitness) + '\n')
    #print('Se obtiene un fitness resultante igua a:')
    return fitness

'''
Se puntúan todos los elementos de la población y nos quedamos con los mejores (se guardan en 'seleccionados').
'''
def seleccion(poblacion):
    puntuados = [(otro_fitness(i), i) for i in poblacion]
    puntuados = [i[1] for i in sorted(puntuados)]

    seleccionados = puntuados[(len(puntuados) - presion)]

    return seleccionados

def genera_sucesor():
    #poblacion = poblacion_inicial;
    individuo = random.choice(poblacion_inicial)
    elegido = random.choice(individuo)
    numero = random.randint(0, len(individuo)-1)
    individuo_cambiado = individuo
    individuo_cambiado[elegido] = numero;
    #return ', '.join(str(e) for e in individuo) + " de los cuales la posicion " + str(elegido) + " cambia a " + str(numero) + " que pasa a ser " + str(individuo_cambiado)
    return individuo_cambiado;


def enfriamiento_simulado(t_inicial, factor_descenso, n_enfriamientos, n_iteraciones):
    temperatura = t_inicial;
    actual = seleccion(poblacion_inicial);
    valor_actual = otro_fitness(actual);
    mejor = actual;
    valor_mejor = valor_actual;

    for i in range (0, n_enfriamientos):
        for j in range (0, n_iteraciones):
            candidata = genera_sucesor()
            valor_candidata = otro_fitness(candidata)
            incremento = valor_candidata - valor_actual
            if(incremento < 0):
                actual = candidata
                valor_actual = valor_candidata
            if(valor_actual < valor_mejor):
                mejor = actual
                valor_mejor = valor_actual
        temperatura -= factor_descenso

    return 'Un coloreado optimo del grafo es ' + str(mejor) + ', siendo el color el valor de la lista y los índices de la misma los nodos del grafo & un fitness de ' + str(valor_mejor)

