\# U02.DEMO01 · Demostracion de analisis de sentimientos



Extension practica vinculada a LAB05. No genera calificacion adicional; documenta el 

tema de analisis de sentimientos del programa con evidencia reproducible.



\## Corpus utilizado



\- Nombre: TweetEval (subset sentiment)

\- Fuente: Barbieri, F. et al. (2020). TweetEval: Unified Benchmark and Comparative 

&#x20; Evaluation for Tweet Classification. Findings of EMNLP 2020. 

&#x20; DOI: 10.18653/v1/2020.findings-emnlp.148

\- Clases: negative, neutral, positive

\- Ejecutado en Google Colab (no requiere el proyecto uv local)



\## Pipeline



TfidfVectorizer (lowercase, ngram\_range=(1,2), min\_df=3, max\_features=25000) + 

LogisticRegression (max\_iter=1000, class\_weight="balanced", random\_state=42), 

ajustado unicamente sobre el conjunto de entrenamiento para evitar fuga.



\## Resultados obtenidos



\- F1-macro (validacion): 0.641

\- F1-macro (prueba): 0.589

\- Accuracy (prueba): 0.593



| Clase | Precision | Recall | F1-score | Support |

|---|---|---|---|---|

| negative | 0.556 | 0.676 | 0.610 | 3972 |

| neutral | 0.654 | 0.536 | 0.589 | 5937 |

| positive | 0.546 | 0.594 | 0.569 | 2375 |



Verificaciones minimas: superadas (predicciones completas, clases validas, pipeline 

con los pasos esperados).



\## Discusion



\*\*1. Errores relacionados con negacion, ironia o falta de contexto:\*\*

Al revisar 20 errores, el patron dominante no fue negacion clasica sino confusion entre 

"tema polemico/negativo" y "tono neutral/informativo". Ejemplos: noticias sobre acusaciones 

politicas (Maduro, RCMP canadiense) o temas sensibles (marihuana medicinal, crisis de 

opioides) clasificadas como neutral cuando el anotador humano las considero negative, 

o viceversa. El modelo, basado en bolsa de palabras TF-IDF, confunde reportar un hecho 

negativo con expresar una opinion negativa.



\*\*2. Clase con menor recall:\*\*

"neutral" (0.536), confirmado tanto en el reporte de clasificacion como en la muestra 

de 20 errores, donde 11 de los 20 casos correspondian a tweets neutrales mal clasificados 

hacia negative o positive.



\*\*3. Decision si los falsos negativos tuvieran mayor costo:\*\*

La clase "negative" ya tiene el recall mas alto (0.676) gracias a class\_weight="balanced", 

a costa de su precision mas baja (0.556). Si el contexto exigiera priorizar aun mas la 

deteccion de negativos (ej. un sistema de alerta de quejas urgentes), se recomendaria 

ajustar pesos de clase manualmente mas alla de "balanced" o usar un umbral de decision 

basado en predict\_proba en vez de predict directo.



\*\*4. Limitaciones para mensajes dominicanos en espanol:\*\*

El modelo esta entrenado exclusivamente en ingles; el vocabulario aprendido no reconoceria 

modismos dominicanos ("chin", "vaina", "tato"), variaciones morfologicas del espanol, ni 

el contexto pragmatico/cultural especifico de Republica Dominicana. Ademas, el desempeno 

ya limitado en su propio idioma y dominio (F1-macro 0.589) sugiere que el reto de detectar 

sentimiento con matices no es solo de vocabulario sino de la arquitectura simple del 

modelo (bolsa de palabras sin contexto secuencial).



\## Conexion con LAB05



Este pipeline usa la misma arquitectura (TfidfVectorizer + LogisticRegression) que el 

clasificador de rol retorico entrenado con PubMed 20k RCT, permitiendo comparar como 

el mismo enfoque metodologico se comporta en dos dominios distintos: texto cientifico 

estructurado (LAB05, F1-macro 0.758) versus texto social informal y ambiguo (esta 

demostracion, F1-macro 0.589), reforzando que el desempeno de un modelo de texto depende 

fuertemente de la naturaleza del dominio, no solo del algoritmo elegido.

