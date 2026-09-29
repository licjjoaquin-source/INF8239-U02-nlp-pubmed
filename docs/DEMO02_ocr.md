\# U02.DEMO02 · Microejemplo de OCR



Demostracion sin puntuacion independiente. Flujo completo de reconocimiento optico de 

caracteres (OCR): de la imagen al texto procesable.



\## Flujo del sistema OCR



Adquisicion -> Preprocesamiento -> Deteccion -> Reconocimiento -> Posprocesamiento -> 

Validacion. Cada etapa introduce riesgos distintos (resolucion/inclinacion, perdida de 

trazos utiles, mezcla de bloques, confusion de simbolos, correcciones indebidas, 

aceptacion automatica de errores criticos).



\## Ejecucion



Se genero una imagen sintetica reproducible con tres lineas de texto ("Solicitud: 

INF-8239", "Estado: Pendiente de revision", "Prioridad: Alta"), se preproceso con escala 

de grises y umbralizacion Otsu (OpenCV), y se reconocio con Tesseract OCR.



\*\*Nota de reproducibilidad:\*\* el paquete de idioma espanol (tesseract-ocr-spa) no estuvo 

disponible en el entorno de ejecucion por restriccion de conectividad; se uso el paquete 

de ingles (lang="eng") como sustituto. Esto es relevante para el analisis, no un error a 

ocultar.



\## Texto extraido





\## Inspeccion de confianza por palabra



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



\## Interpretacion responsable



\*\*Error identificado:\*\* la palabra "revision" se reconocio incorrectamente como 

"revisi6n" (la "o" con tilde se confundio con el numero "6"). Esto ocurrio precisamente 

por usar el paquete de idioma ingles sobre texto en espanol: el modelo de reconocimiento 

no esta entrenado para las formas tipograficas de caracteres acentuados del espanol.



\*\*La confianza es una senal util, no una garantia:\*\* la palabra mal reconocida obtuvo una 

confianza de 44.8%, dramaticamente mas baja que el resto de palabras (92-96%). Esto 

demuestra que el propio sistema "sabe" que ese resultado es menos confiable, aunque igual 

entrega una prediccion. Un pipeline responsable deberia usar un umbral de confianza (por 

ejemplo, marcar para revision humana cualquier palabra por debajo de 70%) en vez de 

aceptar todo el texto extraido sin distincion.



\*\*OCR extrae texto, no verifica veracidad:\*\* el sistema no tiene forma de saber si 

"revisi6n" es un error tipografico o un codigo legitimo; solo un proceso de validacion 

posterior (humano o basado en reglas del dominio) puede hacer esa distincion.



\*\*Conexion con la practica:\*\* este mismo principio aplica directamente a la idea de un 

DSS de radiologia discutida anteriormente en este curso: si un informe medico escaneado 

se procesara con OCR antes de aplicar clasificacion de texto (como en el LAB05), un error 

similar en una palabra clinica critica (dosis, fecha, resultado) podria propagarse 

silenciosamente hacia el modelo de clasificacion posterior, sin que nada en el pipeline 

lo detecte automaticamente a menos que se implemente un umbral de confianza explicito.



\## Riesgos declarados (documentos reales)



Documentos reales (a diferencia de esta imagen sintetica) requieren ademas: autorizacion 

explicita para su procesamiento, proteccion de datos personales/sensibles, y reglas de 

retencion definidas. La calidad del OCR debe evaluarse por campo especifico, tipo 

documental e idioma, no con una sola metrica global.



\## Fuente

Material de la Unidad 02, INF-8239 Ciencia de Datos II (Edwin Ramon Jose Nolasco).

