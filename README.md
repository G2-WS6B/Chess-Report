LINK VIDEO: https://www.youtube.com/watch?v=Lz8Pbc5uJGA
<div align="center">
  <h2 style="border-bottom: none;">Universidad Peruana de Ciencias Aplicadas</h2> 

  <div align="center">
  <img src="https://i.postimg.cc/6598BW1v/upc-logo.png" alt="upc-logo" width="250" height="150">
  </div>


  <h2 style="border-bottom: none;">Ingeniería de software</h2> 
  <h2 style="border-bottom: none;">Ciclo VI</h2> 
  <h2 style="border-bottom: none;">Complejidad Algorítmica</h2> 
  <h2 style="border-bottom: none;">Sección: WS6B</h2> 
  <h2 style="border-bottom: none;">Profesor: Canaval Sánchez, Luis Martin</h2> 
  <h2 style="border-bottom: none;">Chess Report</h2> 
  <h2 style="border-bottom: none;">Grupo: 2</h2> 
  <h2 style="border-bottom: none;">Relación de Integrantes:</h2> 
  
  <ul>
    <li style="list-style-type: none">Benedetti Rivas, Lucas Sebastián (u201817461)</li>
    <li style="list-style-type: none">Cancho Corilla, Ángel Antonio    (u201721995)</li>
    <li style="list-style-type: none">Moreno Rosales, Claudio Jesús    (u20191e800)</li>
  </ul>

  <h2 style="border-bottom: none;">Mes y Año: Septiembre - 2023</h2> 
</div>

<br><br>
<hr>

<h3 style="border-bottom: none;">Tabla de contenido</h2>

- [Student Outcome](#student-outcome)
- [Introducción](#introducción)
  - [1.1. Presentación](#11-presentación)
    - [1.1.1. Descripción del Problema](#111-descripción-del-problema)
    - [1.1.2. Descripción del espacio de búsqueda](#112-descripción-del-espacio-de-búsqueda)
- [Propuesta](#propuesta)
  - [2.1. Descripción de la propuesta](#21-descripción-de-la-propuesta)
    - [2.1.1. Algoritmo Minimax](#211-algoritmo-minimax)
    - [Ejemplo de poda alfa-beta](#ejemplo-de-poda-alfa-beta)
      - [2.1.1.1. Optimización con Poda alfa-beta](#2111-optimización-con-poda-alfa-beta)
      - [2.1.1.2. Optimización con programación dinámica](#2112-optimización-con-programación-dinámica)
    - [2.1.2. Justificación del uso de Minimax](#212-justificación-del-uso-de-minimax)
    - [2.1.3. Interfaz gráfica de usuario](#213-interfaz-gráfica-de-usuario)
- [Referencias](#referencias)
<br>

## Student Outcome

**ABET - EAC - Student Outcome 4**

**Criterio:** La capacidad de reconocer responsabilidades éticas y profesionales en situaciones de ingeniería y hacer juicios informados, que deben considerar el impacto de las soluciones de ingeniería en contextos globales, económicos, ambientales y sociales. En el siguiente cuadro se describen las acciones realizadas y enunciados de conclusiones por parte del grupo, que permiten sustentar el haber alcanzado el logro del ABET - EAC - Student Outcome 4.


| Criterio Específico | Acciones Realizadas | Conclusiones                                      |
| ------------------- | ------------------- | ------------------------------------------------- |
|Demuestra ética profesional en el ejercicio de la ingeniería de software.|Lucas Benedetti Rivas, Descripción del espacio de búsqueda<br><br>Ángel Cancho Corilla, Propuesta<br><br>Claudio Jesús Moreno Rosales, Descripción del Problema.|El desarrollo en equipo, mediante pautas, desarrollo Agile, nos ayudó a comprometernos como equipo. La metodología Agile y nuestro trabajo en equipo fueron clave para nuestro éxito. Aprendimos la importancia de la colaboración y la agilidad en la ingeniería de software.|
|Demuestra Responsabilidad profesional para el logro de los objetivos.|Lucas Benedetti Rivas, Descripción del espacio de búsqueda<br><br>Ángel Cancho Corilla, Propuesta<br><br>Claudio Jesús Moreno Rosales, Descripción del Problema. |El compromiso en la elaboración de la propuesta es evidencia de la dedicación para alcanzar metas en mi campo de trabajo. El desarrollo continuo en equipo demostró responsabilidad. |
|Emite juicios considerando el impacto de las soluciones de ingeniería de software en el contexto global, impacto social, ambiental y económico.|Lucas Benedetti Rivas, Descripción del espacio de búsqueda<br><br>Ángel Cancho Corilla, Propuesta<br><br>Claudio Jesús Moreno Rosales, Descripción del Problema. |Se demuestra que el equipo tiene conciencia profesional sólida y un enfoque holístico hacia la ingeniería de software, teniendo en cuenta no sólo los aspectos técnicos, sino también su influencia en un contexto más amplio |

<br><br>

## Introducción
### 1.1. Presentación
#### 1.1.1. Descripción del Problema

**Historia**

Su origen es objeto de debate; sin embargo, la versión más aceptada sugiere que fue inventado en la India en el siglo VI d.C, originalmente llamado como “Chaturanga”. Después de más de mil años, en 1768, empezó a difundirse la idea de crear una máquina capaz de jugar al ajedrez, llamada “El Turco”, y en 1912 se construyó un autómata llamado “Ajedrecista”. Después de estos sucesos, no se mencionó sobre el ajedrez mecánico hasta 1950 con un artículo de Claude Shannon, en el cual explicaba las principales formas de búsqueda, una de ellas, es la llamada Tipo A, que se basaba en fuerza bruta, examinando cada rama del árbol de movimientos. Para ese entonces, Shannon creyó que no sería práctico por la extensión de la profundidad del árbol y sugirió un programa de Tipo B, para analizar exclusivamente las mejores jugadas de cada posición. El problema era que se confía en que la computadora decida qué movimientos son suficientemente buenos para cualquier posición.

En 1973, se crea el programa Chess 4.0, lo innovador de esta versión fue el uso del paradigma Tipo A, mencionado décadas atrás por Shannon, ganando el torneo de Association for Computing Machinery (ACM) durante 5 años seguidos, además de incentivar la creación del World Computer Chess Championship (WCCC) en 1974.

<br>

<div align="center"> Figura 1: Imagen de los Ingenieros en la WCCC de 1974</div>

<div align="center"><a  href = "https://postimg.cc/8F6MnQQ1"><img  src="https://i.postimg.cc/rphjsMft/image1.png"  alt="Engineer"  width="600"  height="350" /></a></div>

<div align="center"> Nota: Se puede apreciar el Campeonato Mundial de Ajedrez por Ordenadores</div> 

<br>

Chess 4.0 estableció un paradigma que continúa utilizando hasta hoy, evitando imitar los procesos de pensamiento humando, confiando en la búsqueda de árbol y optimización selectiva de ramificación y poda. Sin embargo, esta última técnica debe gestionarse de manera cuidadosa, ya que, si se poda demasiado, hay riesgo de cortar jugadas interesantes, y si la técnica se extiende desmesuradamente, el programa puede analizar jugadas sin interés, perdiendo tiempo en ejecución. En 1971, Deep blue, una computadora de Tipo A, derroto al campeón del mundo Garry Kaspárov, siendo la primera vez que una computadora derrotara al campeón del mundo en tiempos de control de torneo. 

En 1990, se empezó a utilizar de manera comercial las computadoras de Tipo B y en 1998 se publico el programa Rebel 10, que derroto a Viswanathan Anand por 5 a 3. Actualmente el programa sigue en constante evolución hasta su versión Rebel 16, lanzada a finales del 2022.

<br>

<div align="center"> Figura 2: GNU Chess 5.07 compitiendo contra sí mismo</div>

<div align="center"><a  href = "https://postimg.cc/K1VtNcWq"><img  src="https://i.postimg.cc/1zRMyfrQ/image2.png"  alt="Chess"  width="300"  height="350" /></a></div>

<div align="center"> Nota: GNU Chess 5.07 un motor de ajedrez de código abierto</div> 

<br>


#### 1.1.2. Descripción del espacio de búsqueda

El árbol de búsqueda en el ajedrez se representa de manera más precisa como un grafo dirigido acíclico, debido a la posibilidad de que múltiples caminos conduzcan a una misma posición en el juego, lo que introduce relaciones cíclicas en la estructura. A pesar de esta distinción técnica, el término "árbol de búsqueda" se utiliza comúnmente en el contexto del ajedrez debido a su conveniencia conceptual y porque muchas técnicas de búsqueda y algoritmos se aplican de manera similar tanto a árboles como a grafos dirigidos acíclicos.

<br>

<div align="center"> Figura 3: Imagen de un árbol binario de factor de ramificación de 2</div>

<div align="center"><a  href = "https://postimg.cc/CZhsx1SR"><img  src="https://i.postimg.cc/1z6CMndr/Arbol-Binario.png"  alt="Tree"  width="600"  height="350" /></a></div>

<div align="center"> Nota: Se muestra un árbol binario</div> 

<br>

El espacio de búsqueda en el ajedrez se deriva principalmente de dos factores:
- **Factor de ramificación:** En cada posición de ajedrez, un jugador tiene múltiples movimientos legales para elegir, el número promedio es de 30 posiciones posibles. Esto significa que, en el primer nivel del árbol de búsqueda, existen 30 posiciones hijas por analizar.
- **Profundidad del árbol:** El ajedrez es un juego que en promedio consta de 80 movimientos, repartido entre los participantes, es decir, el árbol de búsqueda se ramifica en múltiples niveles, y cada nivel representa un turno de juego adicional.

Para calcular el espacio de búsqueda, multiplicaremos el factor de ramificación por la profundidad del árbol. En el siguiente cuadro podrá visualizar las posibles posiciones dependiendo de la profundidad del árbol.

<br>

**Tabla 1:** Soluciones posibles que dependen de la profundidad del árbol

| FR  | PA | Espacio de búsqueda |
|----:|---:|---------------------|
| 30  | 5  | 30^5 = 2.43 × 10^7  |
| 30  | 10 | 30^10 = 5.9049 × 10^14 |
| 30  | 20 | 30^20 = 3.4867844 × 10^29 |
| 30  | 40 | 30^40 = 1.2157665 × 10^59 |
| 30  | 80 | 30^80 = 1.47808829 × 10^118 |

**Nota:** Suponiendo que una computadora pueda generar una posición en el mínimo tiempo Planck (10^(-43)  segundos), tardaríamos en visitar todo el árbol de profundidad (80) en 3,16887676 ×10^69 años. 

<br>

## Propuesta
### 2.1. Descripción de la propuesta

El principal objetivo del proyecto consiste en la creación de un bot para el juego de ajedrez, que emplee algoritmos avanzados con el propósito de tomar decisiones óptimas y eficaces en cada movimiento durante la partida. Para ello, establecimos objetivos bajo el criterio de SMART.

## Desarrollo del Bot de Ajedrez:

| **Específico**                     | Crear un programa de computadora que juegue ajedrez utilizando algoritmo Minimax. |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Medible**                         | Evaluar la efectividad del bot en partidas de ajedrez simuladas y comparar sus movimientos con las jugadas óptimas en diferentes escenarios.      |
| **Alcanzable**                      | Contar con el equipo técnico competente y los recursos necesarios para desarrollar e implementar el algoritmo Minimax.  |
| **Relevante**                       | Contribuir al avance de la inteligencia artificial aplicada a juegos estratégicos y mejorar la experiencia de juego para los amantes del ajedrez.    |
| **Con Tiempo Definido**             | Lograr un prototipo funcional del bot de ajedrez en un plazo de 30 dias a partir de la fecha de inicio del proyecto.                             |

## Optimización y Mejora del Rendimiento del Bot:

| **Específico**                     | Implementar la poda alfa-beta y la programación dinámica para optimizar la eficiencia y la toma de decisiones del bot de ajedrez.                   |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Medible**                         | Reducir el tiempo de cálculo de movimientos en al menos un 30% y mejorar la calidad de las jugadas mediante la optimización implementada.             |
| **Alcanzable**                      | Contar con expertos en algoritmos y optimizaciones para implementar eficazmente estas mejoras en el bot.                                          |
| **Relevante**                       | Asegurar que el bot de ajedrez sea competitivo y viable para su uso en partidas reales al mejorar su eficiencia y precisión.                         |
| **Con Tiempo Definido**             | Implementar las optimizaciones mencionadas en un plazo de 40 dias después de la creación del prototipo inicial del bot.                              |

## Desarrollo de la Interfaz Gráfica de Usuario (GUI):

| **Específico**                     | Diseñar y desarrollar una interfaz gráfica de usuario atractiva y funcional para que los usuarios interactúen con el bot de ajedrez.                   |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Medible**                         | Evaluar la usabilidad y la satisfacción de los usuarios mediante pruebas de usuario y retroalimentación recopilada.                              |
| **Alcanzable**                      | Contar con diseñadores y desarrolladores competentes en la creación de interfaces atractivas y funcionales.                                      |
| **Relevante**                       | Proporcionar a los usuarios una forma intuitiva y cómoda de interactuar con el bot de ajedrez, mejorando así su experiencia de juego.                  |
| **Con Tiempo Definido**             | Finalizar el desarrollo de la interfaz gráfica de usuario en un plazo de 50 dias después de la implementación de las optimizaciones del bot.           |

#### 2.1.1. Algoritmo Minimax

Se implementará el algoritmo Minimax, un algoritmo con un enfoque recursivo, utilizado para la toma de decisiones en juegos de adversario, como el ajedrez. Su objetivo es encontrar la jugada óptima en cada estado del juego, asumiendo que el oponente también juega de forma óptima. Para ello, explora recursivamente el árbol de juego, donde los nodos representan los estados posibles del juego y las aristas representan los movimientos posibles. En cada nivel de profundidad, alterna entre maximizar la ventaja propia (jugador Max) y minimizar la ventaja del oponente (jugador Min), de ahí su nombre "Minimax".

<div align="center"> Figura 4: Ejemplo de poda alfa-beta</div>

<div align="center"><a  href = "https://postimg.cc/8JfCM2Sh"><img  src="https://i.postimg.cc/4dBhkG2F/Imagen2.png"  alt=Poda alfa-beta"  width="600"  /></a></div>

<div align="center"> Nota: Se muestra un arbol con poda alfa-beta</div> 

#### Ejemplo de poda alfa-beta

##### 2.1.1.1. Optimización con Poda alfa-beta

Una optimización del algoritmo Minimax, es la agregación de Poda alfa-beta, una estrategia para reducir la cantidad de nodos que se deben evaluar en el árbol de juego. Para entender cómo funciona, se establecen los siguientes pasos:
- Se realiza una exploración recursiva del árbol de juego, alternando entre los jugadores Max y Min en cada nivel del árbol.
- Se mantiene un rango (alfa, beta) para cada nodo, que representa la mejor opción encontrada hasta ese momento para el jugador Max (alfa) y para el jugador Min (beta).
- Durante la exploración, si se encuentra un nodo donde el jugador Min tiene una opción que es peor que la mejor opción encontrada hasta ahora para el jugador Max en ese nivel (beta <= alfa), entonces se poda la exploración de los hijos de ese nodo para el jugador Max en ese nivel, ya que Min no elegiría esta opción.

##### 2.1.1.2. Optimización con programación dinámica

Además, se implementará programación dinámica para almacenar y reutilizar evaluaciones de posiciones y minimizar el costo de recalcular jugadas previas, utilizando una tabla de transposición y memoización.

El algoritmo Minimax genera y explora el árbol de juego hasta una cierta profundidad. En cada nivel, considera todas las posibles jugadas y evalúa las posiciones utilizando la función de evaluación, luego se utiliza la memoización para almacenar las evaluaciones de posición en una tabla de transposición. Sin embargo, antes de calcular la evaluación de una posición, verifica si ya está almacenada en la tabla de transposición. Si lo está, recupera la evaluación almacenada en lugar de recalcularla, finalmente selecciona la mejor jugada.

#### 2.1.2. Justificación del uso de Minimax

En el contexto del ajedrez, el algoritmo Minimax es preferible sobre el backtracking convencional debido a la naturaleza estratégica y competitiva del juego. El ajedrez implica la toma de decisiones basada en la anticipación de las acciones del oponente, y Minimax está diseñado precisamente para modelar este tipo de interacción. Al considerar las mejores respuestas del oponente en cada jugada, Minimax permite la selección de movimientos que maximizan la ventaja propia y minimizan los riesgos.

#### 2.1.3. Interfaz gráfica de usuario

Se desarrollará una interfaz gráfica de usuario (GUI) intuitiva y atractiva que permitirá a los usuarios interactuar cómodamente con el bot de ajedrez mediante Pygame, una biblioteca de Python de código abierto para crear interfaces y videojuegos en 2D, proporciona gestión de eventos, sprites, sonidos y fuentes de texto.


<br>

<div align="center"> Figura 5: Juego realizado con Pygame</div>

<div align="center"><a href='' target='_blank'><img src='https://i.postimg.cc/26sN5btq/imagen-2023-09-29-223538555.png' border='0' alt='Chess Game' width="600"/></a></div>

<div align="center"> Nota: Se muestra un videojuego de laberintos</div> 

</br>

# Referencias

- Cormen, T., Leiserson, C., Rivest, R., & Stein, C. (2009). [Introduction to Algorithms.](https://acortar.link/V4B47P)

- Leyva-Vázquez, M., & Smarandache, F. (2018). [Inteligencia Artificial: retos, perspectivas y papel de la Neutrosofía.](https://acortar.link/dTKoVr) Infinite Study.

- Russell, S. J. (2010). [Artificial intelligence: A modern approach.](https://acortar.link/P01tJf) Pearson Education, Inc.

- Sanango Peña, J. E. (2019). [Estudio y desarrollo de los algoritmos de visión y de inteligencia artificial aplicados a un robot, para resolver partidas de ajedrez hombre-máquina (Master's thesis, Universitat Politècnica de Catalunya).](https://acortar.link/dWH8KV)

- Trillo, P. (2016). [Centauro, el híbrido entre humano y máquina.](https://acortar.link/DzzuQV) Medium.

