\# U02.LAB06 · Embeddings y análisis responsable de redes



\## Cierre interpretativo



\*\*Resultado de embeddings:\*\* Se entrenó un modelo Word2Vec (vector\_size=60, window=5, 

min\_count=1, epochs=30) sobre las 180,040 oraciones del corpus PubMed 20k RCT, obteniendo 

un vocabulario de 57,996 palabras únicas. Los vecinos semánticos más cercanos a "patients" 

fueron subjects (0.782), individuals (0.732), outpatients (0.726), adults (0.673) y 

persons (0.673) — todos términos que en inglés médico se usan de forma intercambiable 

para referirse a las personas que participan en un estudio clínico.



\*\*Evidencia de cobertura:\*\* La cobertura de tokens fue de 1.0 (100%), esperable dado que 

min\_count=1 incluye cualquier palabra que haya aparecido al menos una vez en el corpus, 

sin filtrar por frecuencia mínima.



\*\*Resultado estructural de la red:\*\* Se analizó la red de demostración del club de karate 

de Zachary (34 nodos, 78 aristas), detectando 3 comunidades con una modularidad de 0.411, 

un valor que indica una partición estructural significativa, no aleatoria.



\*\*Dos métricas comparadas:\*\* El nodo 0 obtuvo la mayor centralidad de intermediación 

(betweenness = 0.438) de toda la red, mientras que el nodo 33 obtuvo el mayor grado 

(0.515) y el mayor PageRank (0.097). Esto sugiere que el nodo 0 actúa estructuralmente 

como puente entre comunidades distintas, mientras que el nodo 33 concentra más conexiones 

directas dentro de su propia comunidad.



\*\*Interpretación permitida:\*\* El nodo 0 participa en una proporción alta de los caminos 

más cortos entre pares de nodos de la red, una propiedad estructural medible objetivamente 

mediante betweenness centrality. El nodo 33 recibe conexiones de otros nodos que también 

son estructuralmente relevantes, según indica su PageRank alto.



\*\*Interpretación que NO puede sostenerse:\*\* Que el nodo 0 o el nodo 33 sean "la persona 

más influyente" o "el líder real" del grupo. La centralidad estructural describe una 

propiedad de conectividad del grafo, no autoridad social, influencia causal ni liderazgo 

verificado; esa información no está contenida en la red tal como fue construida (solo 

nodos y aristas binarias, sin atributos sociales adicionales).



\*\*Siguiente experimento:\*\* Comparar los embeddings entrenados en este corpus científico 

contra embeddings preentrenados en un corpus general (ej. GloVe o Word2Vec de Google News) 

para el mismo término ("patients"), y verificar si el dominio especializado produce vecinos 

Semánticos sustancialmente distintos a los que se obtendrían con un corpus genérico. 

Además, sería valioso experimentar con un valor de min\_count mayor (ej. min\_count=5) para 

evaluar si filtrar palabras muy infrecuentes cambia la calidad de los vecinos, dado que 

con min\_count=1 el vocabulario incluye términos que aparecieron una sola vez y cuyo vector 

aprendido podría ser poco confiable.

