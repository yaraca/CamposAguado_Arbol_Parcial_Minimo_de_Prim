#Algoritmo de Prim
#Es un algoritmo que encuentra el árbol de expansión minima (MST) de un grafo ponderado (con pesos en sus aristas).
#El MST es un subconjunto de las aristas que conecta todos los vértices con el costo total mínimo, sin formar ciclos. 
#Para qué sirve: 
#Reducción de costos en redes de cables, tuberias, carreteras, etc.
#optimización de la planificación de redes de distribución 
#Funcionamiento:
# Paso 1: Determine un vértice arbitrario como vértice inicial del MST. En el diagrama a continuación, elija 0.
# Paso 2: Siga los pasos 3 a 5 hasta que haya vértices no incluidos en el MST (conocidos como vértices marginales).
# Paso 3: Encuentre las aristas que conectan cualquier vértice del árbol con los vértices marginales.
# Paso 4: Encuentre el mínimo entre estas aristas.
# Paso 5: Agregue la arista elegida al MST. Dado que solo consideramos las aristas que conectan los vértices marginales con el resto, nunca se produce un ciclo.
#Aplicaciones:
#diseño de redes electricas, agua o de gas, redes de telecomunicaciones, planificación de carreteras y ferrocarriles, diseño de circuitos electrónicos, optimización de redes de transporte, etc.

#Simulador de Árbol Parcial mínimo de Prim 

#Librerias necesarias
import heapq #para manejar la cola de prioridad y realizar la selección de aristas de menor peso
import matplotlib.pyplot as plt #para graficar el árbol de expansión mínima
import networkx as nx #para crear y manipular grafos de manera eficiente y visualizarlos

#función que implementa el algoritmo de Prim
def prim(grafo, inicio): #parametros: grafo (diccionario de adyacencia) e inicio (nodo inicial)
    visitados = set() #conjunto para rastrear los nodos visitados
    mst = []  # Lista para guardar las aristas del MST
    total_costo = 0 # Variable para acumular el costo total del MST

    #Cola de prioridad: (peso, nodo_origen, nodo_destino)
    cola = [(0, None, inicio)]

    print(f"\nIniciando Prim desde el nodo '{inicio}\n'")

    while cola: #mientras haya aristas en la cola
        peso, origen, destino = heapq.heappop(cola) #sacar la arista de menor peso y sus nodos asociados

        if destino in visitados: #si el nodo destino ya fue visitado, saltar a la siguiente iteración
            continue

        visitados.add(destino) #marcar el nodo destino como visitado

        if origen is not None: #si hay un nodo origen (no es el primer nodo)
            mst.append((origen, destino, peso)) #agregar la arista al MST con su peso
            total_costo += peso #acumular el costo total del MST
            print(f"\n->Agregada arista ({origen} - {destino}) con peso {peso}\n") #imprimir información de la arista agregada

        for vecino, costo in grafo[destino].items(): #para cada vecino del nodo destino y su costo
            if vecino not in visitados: #si el vecino no ha sido visitado
                heapq.heappush(cola, (costo, destino, vecino)) #agregar la arista a la cola de prioridad
                print(f"Considerando arista ({destino} - {vecino}) con peso {costo}") #imprimir información de la arista considerada

    print("\nÁrbol de Expansión Mínima construido:") #imprimir el resultado final del MST
    for u, v, w in mst: #recorrer las aristas del MST con sus pesos. u es el nodo origen, v es el nodo destino y w es el peso de la arista
        print(f"({u} - {v}) peso {w}") 
    print(f"\nCosto total: {total_costo}") #imprimir el costo total del MST

    return mst, total_costo #retornar el MST y su costo total

#función para graficar el árbol de expansión mínima
def graficar_prim(grafo, mst):
    G = nx.Graph() #crear un grafo vacío usando NetworkX
    
    # Añadir todos los nodos y aristas originales
    for nodo in grafo: #para cada nodo en el grafo
        for vecino, peso in grafo[nodo].items(): #para cada vecino y su peso asociado
            G.add_edge(nodo, vecino, weight=round(peso, 2)) #agregar la arista al grafo con su peso redondeado a 2 decimales
    
    pos = nx.spring_layout(G, seed=42) #posiciones de los nodos para la visualización
    #.spring_layout() genera una disposición de los nodos en el plano, utilizando un algoritmo de fuerza para evitar superposiciones
    # y distribuirlos de manera uniforme. El parámetro seed asegura que la disposición sea reproducible.

    # Dibujar nodos y todas las aristas
    nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=700) # Dibujar los nodos con color y tamaño especificados
    nx.draw_networkx_labels(G, pos) # Dibujar las etiquetas de los nodos

    # Aristas normales (no MST)
    aristas_mst = {(u, v) if u < v else (v, u) for u, v, _ in mst} # Crear un conjunto de aristas del MST para evitar duplicados 
    #u y v son los nodos de la arista, y el orden se normaliza para evitar duplicados
    # (por ejemplo, (A, B) es lo mismo que (B, A)).
    aristas_normales = [#crear una lista de aristas normales que no están en el MST
        (u, v) for u, v in G.edges() if ((u, v) if u < v else (v, u)) not in aristas_mst #comprobar si la arista no está en el MST
    ] #u y v son los nodos de la arista, y el orden se normaliza para evitar duplicados
    nx.draw_networkx_edges(G, pos, edgelist=aristas_normales, edge_color='gray') #dibujar las aristas normales en color gris

    # Aristas del MST
    nx.draw_networkx_edges(G, pos, edgelist=[(u, v) for u, v, _ in mst],
                           edge_color='red', width=2) # Dibujar las aristas del MST en rojo y con mayor grosor
    
    # Etiquetas de peso
    etiquetas = nx.get_edge_attributes(G, 'weight') #obtener los atributos de peso de las aristas del grafo
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas) #dibujar las etiquetas de peso en las aristas

    plt.title("Árbol de Expansión Mínima (Algoritmo de Prim)")
    plt.axis('off')
    plt.show()

# Definición del grafo como diccionario
grafo = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'D': 3, 'E': 1},
    'C': {'A': 3, 'F': 5},
    'D': {'B': 3, 'E': 4},
    'E': {'B': 1, 'D': 4, 'F': 2},
    'F': {'C': 5, 'E': 2}
}

# Ejecutar el algoritmo
mst, costo = prim(grafo, 'D')  

# Mostrar graficación
graficar_prim(grafo, mst)
