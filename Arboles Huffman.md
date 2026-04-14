# Árboles de Huffman

## Introducción

La compresión de datos es uno de los problemas clásicos de la informática, y el algoritmo de Huffman ha dejado un impacto grande en el campo de las soluciones que se han propuesto a lo largo del tiempo. Desarrollado en 1952 por David A. Huffman mientras era estudiante de doctorado en MIT, este método de codificación sigue siendo relevante hoy en día y forma parte de varios estándares de compresión modernos como DEFLATE, que es la base de formatos como ZIP y PNG.

## Fundamento del algoritmo

Su principal objetivo es asignar códigos más cortos a los símbolos que aparecen con mayor frecuencia en un conjunto de datos, y a los que aparecen con menos frecuencia, códigos más largos, a diferencia de la codificación de longitud fija (como ASCII, donde cada carácter ocupa exactamente 8 bits), dado que todos los símbolos reciben el mismo espacio independientemente de cuánto se usen.

Para construir el árbol, el algoritmo sigue estos pasos:

- Calcular la frecuencia de aparición de cada símbolo en el mensaje o archivo a comprimir.
- Crear un nodo hoja por cada símbolo y se insertan en una cola de prioridad ordenada por frecuencia (menor frecuencia, mayor prioridad).
- Repetidamente se extraen los dos nodos de menor frecuencia, se crea un nuevo nodo interno cuya frecuencia es la suma de ambos, y se reinserta en la cola. Este proceso continúa hasta que solo queda un nodo: la raíz del árbol.
- Finalmente, se recorre el árbol asignando 0 a cada rama izquierda y 1 a cada rama derecha (o viceversa), lo que genera los códigos de cada símbolo.

## Ejemplo

Considerando la cadena "AABBBCCDDDDEE". Las frecuencias serían: D=4, B=3, A=2, C=2, E=2. Al aplicar el algoritmo, D recibiría el código más corto, mientras que símbolos como A, C o E recibirían códigos más largos, así se logra una representación del mensaje que ocupa menos bits que su equivalente en codificación fija.

## Propiedades importantes

El árbol de Huffman genera siempre un código prefijo, ningún código asignado es prefijo de otro. Esto garantiza que la decodificación sea unívoca: al recorrer el árbol desde la raíz siguiendo los bits del mensaje, cada vez que se llega a una hoja se sabe exactamente qué símbolo se encontró, sin necesidad de delimitadores.

Asimismo, se puede demostrar que la codificación de Huffman es óptima entre todos los códigos de longitud variable cuando los símbolos se codifican de manera independiente. No hay otro esquema de este tipo que produzca una representación más corta en promedio para una distribución de frecuencias dada.

## Aplicaciones y limitaciones

Aparte de la compresión de archivos, los árboles de Huffman aparecen en telecomunicaciones, procesamiento de imágenes y transmisión de datos; no obstante, tienen una limitación práctica: para decodificar un mensaje comprimido, el receptor necesita conocer el árbol utilizado, lo que implica transmitirlo junto con los datos o acordarlo de antemano, si el archivo es muy pequeño, este overhead puede hacer que el resultado comprimido sea más grande que el original.

Variantes como la codificación de Huffman adaptativa resuelven en parte este problema, reconstruyendo el árbol de manera dinámica a medida que se procesan los datos, sin necesidad de un paso previo de análisis de frecuencias.
