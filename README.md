# Chess-Report
Reporte del Trabajo de Complejidad Algorítmica.
##PARTE DE DESCRIPCION

## 1.1.2. Descripción del espacio de búsqueda

El árbol de búsqueda en el ajedrez se representa de manera más precisa como un grafo dirigido acíclico, debido a la posibilidad de que múltiples caminos conduzcan a una misma posición en el juego, lo que introduce relaciones cíclicas en la estructura. A pesar de esta distinción técnica, el término "árbol de búsqueda" se utiliza comúnmente en el contexto del ajedrez debido a su conveniencia conceptual y porque muchas técnicas de búsqueda y algoritmos se aplican de manera similar tanto a árboles como a grafos dirigidos acíclicos.

El espacio de búsqueda en el ajedrez se deriva principalmente de dos factores:
- **Factor de ramificación:** En cada posición de ajedrez, un jugador tiene múltiples movimientos legales para elegir, el número promedio es de 30 posiciones posibles. Esto significa que, en el primer nivel del árbol de búsqueda, existen 30 posiciones hijas por analizar.
- **Profundidad del árbol:** El ajedrez es un juego que en promedio consta de 80 movimientos, repartido entre los participantes, es decir, el árbol de búsqueda se ramifica en múltiples niveles, y cada nivel representa un turno de juego adicional.

| FR  | PA | Espacio de búsqueda |
|----:|---:|---------------------|
| 30  | 5  | 30^5 = 2.43 × 10^7  |
| 30  | 10 | 30^10 = 5.9049 × 10^14 |
| 30  | 20 | 30^20 = 3.4867844 × 10^29 |
| 30  | 40 | 30^40 = 1.2157665 × 10^59 |
| 30  | 80 | 30^80 = 1.47808829 × 10^118 |

##PARTE DE PROPUESTA
