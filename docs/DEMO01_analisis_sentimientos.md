\# U02.DEMO01 · Demostración de análisis de sentimientos



Extensión práctica vinculada a LAB05. No genera calificación adicional; documenta el tema de análisis de sentimientos del programa con evidencia reproducible.



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

ajustado únicamente sobre el conjunto de entrenamiento para evitar fuga.



\## Resultados obtenidos



\- F1-macro (validación): 0.641

\- F1-macro (prueba): 0.589

\- Accuracy (prueba): 0.593



| Clase | Precisión | Recall | F1-score | Support |

|---|---|---|---|---|

| negative | 0.556 | 0.676 | 0.610 | 3972 |

| neutral | 0.654 | 0.536 | 0.589 | 5937 |

| positive | 0.546 | 0.594 | 0.569 | 2375 |



Verificaciones mínimas: superadas (predicciones completas, clases válidas, pipeline 

con los pasos esperados).



\## Discusión



\*\*1. Errores relacionados con negación, ironía o falta de contexto:\*\*

Al revisar 20 errores, el patrón dominante no fue negación clásica sino confusión entre 

"tema polémico/negativo" y "tono neutral/informativo". Ejemplos: noticias sobre acusaciones 

Políticas (Maduro, RCMP canadiense) o temas sensibles (marihuana medicinal, crisis de 

opioides) clasificadas como neutral cuando el anotador humano las considero negative, 

o viceversa. El modelo, basado en bolsa de palabras TF-IDF, confunde reportar un hecho 

negativo con expresar una opinión negativa.



\*\*2. Clase con menor recall:\*\*

"neutral" (0.536), confirmado tanto en el reporte de clasificación como en la muestra 

de 20 errores, donde 11 de los 20 casos correspondían a tweets neutrales mal clasificados 

hacia negative o positive.



\*\*3. Decisión si los falsos negativos tuvieran mayor costo:\*\*

La clase "negative" ya tiene el recall más alto (0.676) gracias a class\_weight="balanced", 

a costa de su precisión más baja (0.556). Si el contexto exigiera priorizar aún más la 

Detección de negativos (ej. un sistema de alerta de quejas urgentes), se recomendaría 

ajustar pesos de clase manualmente más allá de "balanced" o usar un umbral de decisión 

basado en predict\_proba en vez de predict directo.



\*\*4. Limitaciones para mensajes dominicanos en español:\*\*

El modelo está entrenado exclusivamente en inglés; el vocabulario aprendido no reconocería 

modismos dominicanos ("chin", "vaina", "tato"), variaciones morfológicas del español, ni 

el contexto pragmático/cultural especifico de República Dominicana. Además, el desempeño 

ya limitado en su propio idioma y dominio (F1-macro 0.589) sugiere que el reto de detectar 

sentimiento con matices no es solo de vocabulario sino de la arquitectura simple del 

modelo (bolsa de palabras sin contexto secuencial).



\## Conexión con LAB05



Este pipeline usa la misma arquitectura (TfidfVectorizer + LogisticRegression) que el clasificador de rol retórico entrenado con PubMed 20k RCT, permitiendo comparar como 

el mismo enfoque metodológico se comporta en dos dominios distintos: texto científico 

estructurado (LAB05, F1-macro 0.758) versus texto social informal y ambiguo (esta 

Demostración, F1-macro 0.589), reforzando que el desempeño de un modelo de texto depende 

fuertemente de la naturaleza del dominio, no solo del algoritmo elegido.

