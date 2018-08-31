import warnings
import matplotlib.pyplot as dibuj;
from AG import *;

warnings.filterwarnings(action='ignore')

colores_nodos = enfriamiento_simulado(100, 0.95, 100, 100000)

nx.draw(g, with_labels=True, node_color=colores_nodos)

print('Para el grafo representado en pantalla, se ha llegado a la conclusión que un coloreado óptimo es el siguiente:\n' + str(colores_nodos) + '\ndonde el valor indica el color en la lista y el índice indica el vértice correspondiene en el grafo, utilizando ' + str(len(set(colores_nodos))) + ' colores')

dibuj.show();
