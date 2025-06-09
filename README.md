# CamposAguado_Arbol_Parcial_Minimo_de_Prim

# Simulador del Árbol de Expansión Mínima con el Algoritmo de Prim

Este proyecto simula paso a paso el funcionamiento del **algoritmo de Prim** para encontrar el Árbol de Expansión Mínima (MST) en un grafo no dirigido, utilizando Python. Además, cuenta con una visualización gráfica del resultado para facilitar su comprensión.

---------------------------------------------------------------------------------------------------

## Parte Teórica

### ¿Qué es?

El algoritmo de **Prim** es un método voraz (greedy) que permite encontrar el Árbol de Expansión Mínima (MST) de un grafo no dirigido y conectado. Este árbol conecta todos los nodos del grafo con el **menor costo total posible**, sin formar ciclos.

---------------------------------------------------------------------------------------------------

### ¿Para qué sirve?

El MST permite:
- Minimizar el uso de recursos al conectar puntos (como cableado, caminos o tuberías).
- Reducir costos en la instalación de redes.
- Mejorar rutas de distribución.
- Optimizar estructuras en problemas de IA y grafos.

---------------------------------------------------------------------------------------------------

### ¿Cómo se implementa en el mundo?

- **Redes eléctricas y de telecomunicaciones**: minimiza el cable necesario para conectar todas las estaciones.
- **Red de agua o gas**: distribuye recursos sin repetir conexiones innecesarias.
- **Logística**: conecta puntos de distribución sin recorrer caminos duplicados.
- **Agrupamiento en IA (Clustering)**: el MST se usa como base para métodos como el clustering jerárquico.

---------------------------------------------------------------------------------------------------

### ¿Cómo lo implementaría en mi vida?

En mi vida diaria, usaría este algoritmo para optimizar rutas personales, como trayectos entre puntos de entrega, tareas escolares o incluso viajes con múltiples paradas, buscando el recorrido más eficiente.

---------------------------------------------------------------------------------------------------

### ¿Cómo lo implementaría en mi trabajo?

Como estoy en una empresa de suplementos alimenticios, lo usaría para **optimizar las rutas de distribución de productos**, asegurándome de que los pedidos lleguen a todos los puntos de venta o clientes finales con la menor cantidad de kilómetros posibles, minimizando costos de transporte y tiempos de entrega. También se puede aplicar en el diseño de almacenes o redes de transporte interno.

---------------------------------------------------------------------------------------------------

## Funcionamiento del Algoritmo

1. Se inicia desde un nodo arbitrario.
2. Se agregan al MST las **aristas más económicas** que conectan un nodo ya incluido con uno no visitado.
3. El proceso continúa hasta que **todos los nodos están conectados**.
4. Se evita crear ciclos.
5. Se usa una **cola de prioridad** para elegir siempre la siguiente arista más barata disponible.

---------------------------------------------------------------------------------------------------

## Librerías utilizadas

| Librería     | Descripción                                                                                           |
|--------------|-------------------------------------------------------------------------------------------------------|
| `heapq`      | Maneja una **cola de prioridad**, esencial para siempre elegir el nodo con menor distancia acumulada. |
| `networkx`   | Permite construir y manipular grafos en Python, y facilita la visualización de redes.                 |
| `matplotlib` | Librería de gráficos que nos permite **dibujar el grafo y el camino más corto** con nodos y aristas.  |

---------------------------------------------------------------------------------------------------

