\# U02.DEMO02 · Microejemplo de OCR



Demostración sin puntuación independiente. Flujo completo de reconocimiento óptico de 

caracteres (OCR): de la imagen al texto procesable.



\## Flujo del sistema OCR



Adquisición -> Preprocesamiento -> Detección -> Reconocimiento -> Posprocesamiento -> 

Validación. Cada etapa introduce riesgos distintos (resolución/inclinación, perdida de 

trazos utiles, mezcla de bloques, confusión de símbolos, correcciones indebidas, 

Aceptación automática de errores críticos).



\## Ejecución



Se generó una imagen sintética reproducible con tres líneas de texto ("Solicitud: 

INF-8239", "Estado: Pendiente de revisión", "Prioridad: Alta"), se preproceso con escala 

de grises y umbralizacion Otsu (OpenCV), y se reconoció con Tesseract OCR.



\*\*Nota de reproducibilidad:\*\* el paquete de idioma español (tesseract-ocr-spa) no estuvo 

disponible en el entorno de ejecución por restricción de conectividad; se usó el paquete 

de inglés (lang="eng") como sustituto. Esto es relevante para el análisis, no un error a 

ocultar.



\## Texto extraído





\## Inspección de confianza por palabra



| Palabra | Confianza |

|---------|-----------|

| Solicitud: | 93.3% |

| INF-8239 | 92.4% |

| Estado: | 93.3% |

| Pendiente | 92.8% |

| de | 92.4% |

| revisi6n | \*\*44.8%\*\* |

| Prioridad: | 92.2% |

| Alta | 96.1% |



\## Interpretación responsable



\*\*Error identificado:\*\* la palabra "revisión" se reconoció incorrectamente como 

"revisi6n" (la "o" con tilde se confundió con el número "6"). Esto ocurrió precisamente 

por usar el paquete de idioma inglés sobre texto en español: el modelo de reconocimiento 

no está entrenado para las formas tipográficas de caracteres acentuados del español.



\*\*La confianza es una señal útil, no una garantía:\*\* la palabra mal reconocida obtuvo una 

confianza de 44.8%, dramáticamente más baja que el resto de palabras (92-96%). Esto 

demuestra que el propio sistema "sabe" que ese resultado es menos confiable, aunque igual 

entrega una predicción. Un pipeline responsable debería usar un umbral de confianza (por 

ejemplo, marcar para revisión humana cualquier palabra por debajo de 70%) en vez de 

aceptar todo el texto extraído sin distinción.



\*\*OCR extrae texto, no verifica veracidad:\*\* el sistema no tiene forma de saber si 

"revisi6n" es un error tipográfico o un código legítimo; solo un proceso de validación 

posterior (humano o basado en reglas del dominio) puede hacer esa distinción.



\*\*Conexión con la práctica:\*\* este mismo principio aplica directamente a la idea de un 

DSS de radiología discutida anteriormente en este curso: si un informe médico escaneado 

se procesará con OCR antes de aplicar clasificación de texto (como en el LAB05), un error 

similar en una palabra clínica crítica (dosis, fecha, resultado) podría propagarse 

silenciosamente hacia el modelo de clasificación posterior, sin que nada en el pipeline 

lo detecte automáticamente a menos que se implemente un umbral de confianza explicito.



\## Riesgos declarados (documentos reales)



Documentos reales (a diferencia de esta imagen sintética) requieren además: autorización 

explicita para su procesamiento, protección de datos personales/sensibles, y reglas de 

Retención definidas. La calidad del OCR debe evaluarse por campo específico, tipo 

documental e idioma, no con una sola métrica global.



\## Fuente

Material de la Unidad 02, INF-8239 Ciencia de Datos II (Edwin Ramón Jose Nolasco).

