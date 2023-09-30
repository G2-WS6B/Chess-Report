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
  <h2 style="border-bottom: none;">Mes y Año: Setiembre - 2023</h2> 
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

**Objetivos**

El presente proyecto tiene como objetivo el desarrollo de un desafío estratégico basado en el ajedrez, uno de los juegos de mesa más antiguos. 

**Historia**

Su origen es objeto de debate; sin embargo, la versión más aceptada sugiere que fue inventado en la India en el siglo VI d.C, originalmente llamado como “Chaturanga”. Después de más de mil años, en *1768, empezó a difundirse la idea de crear una máquina capaz de jugar al ajedrez, llamada “El Turco”, y en **1912* se construyó un autómata llamado “Ajedrecista”. Después de estos sucesos, no se mencionó sobre el ajedrez mecánico hasta *1950* con un artículo de Claude Shannon, en el cual explicaba las principales formas de búsqueda, una de ellas, es la llamada *Tipo A, que se basaba en fuerza bruta, examinando cada rama del árbol de movimientos. Para ese entonces, Shannon creyó que no sería práctico por la extensión de la profundidad del árbol y sugirió un programa de **Tipo B*, para analizar exclusivamente las mejores jugadas de cada posición. El problema era que se confía en que la computadora decida qué movimientos son suficientemente buenos para cualquier posición.

En *1973*, se crea el programa Chess 4.0, lo innovador de esta versión fue el uso del paradigma Tipo A, mencionado décadas atrás por Shannon, ganando el torneo de Association for Computing Machinery (ACM) durante 5 años seguidos, además de incentivar la creación del World Computer Chess Championship (WCCC) en 1974.

<br>

<div align="center"> Figura 1: Imagen de los Ingenieros en la WCCC de 1974</div>

<div align="center"><a  href = "https://postimg.cc/8F6MnQQ1"><img  src="https://i.postimg.cc/rphjsMft/image1.png"  alt="Engineer"  width="600"  height="350" /></a></div>

<div align="center"> Nota: Se puede apreciar el Campeonato Mundial de Ajedrez por Ordenadores</div> 

<br>

*Chess 4.0* estableció un paradigma que continúa utilizando hasta hoy, evitando imitar los procesos de pensamiento humando, confiando en la búsqueda de árbol y optimización selectiva de ramificación y poda. Sin embargo, esta última técnica debe gestionarse de manera cuidadosa, ya que, si se poda demasiado, hay riesgo de cortar jugadas interesantes, y si la técnica se extiende desmesuradamente, el programa puede analizar jugadas sin interés, perdiendo tiempo en ejecución. En *1971*, Deep blue, una computadora de Tipo A, derroto al campeón del mundo Garry Kaspárov, siendo la primera vez que una computadora derrotara al campeón del mundo en tiempos de control de torneo. 

En *1990*, se empezó a utilizar de manera comercial las computadoras de Tipo B y en 1998 se publico el programa Rebel 10, que derroto a Viswanathan Anand por 5 a 3. Actualmente el programa sigue en constante evolución hasta su versión Rebel 16, lanzada a finales del 2022.

<br>

<div align="center"> Figura 2: GNU Chess 5.07 compitiendo contra sí mismo</div>

<div align="center"><a  href = "https://postimg.cc/K1VtNcWq"><img  src="https://i.postimg.cc/1zRMyfrQ/image2.png"  alt="Chess"  width="300"  height="350" /></a></div>

<div align="center"> Nota: GNU Chess 5.07 un motor de ajedrez de código abierto</div> 

<br>


#### 1.1.2. Descripción del espacio de búsqueda

El árbol de búsqueda en el ajedrez se representa de manera más precisa como un grafo dirigido acíclico, debido a la posibilidad de que múltiples caminos conduzcan a una misma posición en el juego, lo que introduce relaciones cíclicas en la estructura. A pesar de esta distinción técnica, el término "árbol de búsqueda" se utiliza comúnmente en el contexto del ajedrez debido a su conveniencia conceptual y porque muchas técnicas de búsqueda y algoritmos se aplican de manera similar tanto a árboles como a grafos dirigidos acíclicos.


<br>

<div align="center"> Figura 3: Imagen de un árbol binario de factor de ramificación de 2</div>

<div align="center"><a  href = "https://postimg.cc/CZhsx1SR"><img  src="https://i.postimg.cc/1z6CMndr/Arbol-Binario.png"  alt="Chess"  width="600"  height="350" /></a></div>

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

