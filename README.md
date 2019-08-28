

 # IA TP 2
Este trabajo practico se realizo respondiendo estas [consignas](https://docs.google.com/document/d/1eP3aCyTWuTCbYMwf3inNHd7AIIpYHyb_PEj-aXYc1xU/edit)

## Implementación 
Para la implementación se creo una clase **Environment** siguiendo las pautas de la interfaz propuesta. Luego se creo una clase padre llamada **Agent** que se utilizo para que las subclases de **AgenteConMemoria, AgenteSinEstado y AgenteAleatorio** heredaran de **Agente** cambiando en cada subclase el método `think()`.

La estrategia de resolución fueron:
- AgenteSinEstado: recorrer la cuadricula realizando un **zig-zag** desde la **posición de inicio** del agente. 
- AgenteAleatorio: realizar movimientos totalmente **aleatorios** a partir de un numero random.
- AgenteConMemoria: Dirigir al agenta a la **posición (0,0)** y luego recorrer en zig-zag, utilizando dos métodos:
  1. Cuando **choca** contra una pared cambiar de dirección.
  2. Teniendo en cuenta el **tamaño** del entorno, cuando llega a un borde cambia de dirección.

## Preguntas
__hola__
1. Considere una versión modificada del entorno de la aspiradora del Ejercicio 2.7, en el que se penalice al agente con un punto en cada movimiento.
    - ¿Puede un agente reactivo simple ser perfectamente racional en este medio? Explíquese. 
      - No seria racional, ya que al no poseer una forma de guardar por donde a pasado el agente y al tener una penalización por movimiento, repetiría infinitamente el camino elegido produciendo un rendimiento negativo.  
    - ¿Qué sucedería con un agente reactivo con estado? Diseñe este agente.
      - Una agente con estado podría recorrer el camino mas eficientemente que el reactivo simple y podría parar en un determinado momento lo que produciría un mejor rendimiento que el reactivo simple     
    - ¿Cómo se responderían las preguntas a y b si las percepciones proporcionan al agente información sobre el nivel de suciedad/limpieza de todas las cuadrículas del entorno? 
      - En el caso del reactivo simple permitiría ir directamente donde se encuentra la suciedad y cuando no se detectara mas suciedad pasar a un estado "Idle". En el caso de el de estados permitiría recorrer mas eficientemente la cuadricula sin la necesidad de pasar por cada uno de los cuadros

2. Considere una versión modificada del entorno de la aspiradora del Ejercicio 2.7, en el que la geografía del entorno (su extensión, límites, y obstáculos) sea desconocida, así como, la disposición inicial de la suciedad. (El agente puede ir hacia arriba, abajo, así como, hacia la derecha y a la izquierda.) 
   - ¿Puede un agente reactivo simple ser perfectamente racional en este medio? Explíquese. 
     - No, porque al no conocer su extensión no podría asegurar que pasara por todos las cuadriculas y por lo tanto no podría asegurar que limpiara todo el entorno
   - ¿Puede un agente reactivo simple con una función de agente aleatoria superar a un agente reactivo simple? Diseñe un agente de este tipo y medir su rendimiento en varios medios. 
       - En el caso de que la cuadricula fuese pequeña o que tuviera una cantidad de iteraciones muy grandes, el agente aleatorio seria más eficiente.
   - ¿Se puede diseñar un entorno en el que el agente con la función aleatoria obtenga una actuación muy pobre? Muestre los resultados.
       - Si, si el entorno es muy grande y tenemos pocas iteraciones, o en el caso de tener muchos obstáculos juntos 
   - ¿Puede un agente reactivo con estado mejorar los resultados de un agente reactivo simple? Diseñe un agente de este tipo y medir su eficiencia en distintos medios. ¿Se puede diseñar un agente racional de este tipo? 
       - Si, porque me permitiría recorrer todo el entorno  y por lo tanto limpiarlo todo. Se puede observar en la implementación de la clase agenteConMemoria y la función think() 
