\## Cierre interpretativo (LAB05)



\*\*Resultado principal:\*\* Se entrenaron y compararon tres clasificadores de texto sobre 

el corpus PubMed 20k RCT: un baseline (dummy), Complement Naive Bayes y regresión 

Logística, todos usando TF-IDF con n-gramas (1,2) dentro de un pipeline que evita fuga 

de información. La regresión logística obtuvo el mejor F1-macro (0.758), superando 

ampliamente al baseline (0.099) y al Naive Bayes (0.689).



\*\*Modelo seleccionado y evidencia:\*\* Se seleccionó la regresión logística como modelo 

final (models/text\_model.joblib, \~52.5 MB), respaldada por su F1-macro de 0.758 y una 

accuracy de 0.82 sobre 44,721 oraciones de prueba, con reporte de clasificación completo 

guardado en reports/text\_metrics.csv y matriz de confusión en reports/confusión\_text.png.



\*\*Clase con mayor dificultad:\*\* La clase "objective" presento el menor recall (0.63) y 

la menor precisión (0.61), consistente con ser la clase minoritaria del corpus (7.7% del 

total). La matriz de confusión revelo que 876 casos reales de "objective" se clasificaron 

Erróneamente como "background", superando incluso a sus propios aciertos relativos.



\*\*Tipo de error más frecuente:\*\* Al categorizar manualmente 20 errores, el 45% correspondió 

a ambigüedad genuina entre resultados y conclusiones (oraciones que combinan un hallazgo 

cuantitativo con su interpretación en la misma frase) y un 35% adicional a etiquetas 

discutibles, donde incluso un lector humano experto podría razonablemente asignar una 

Categoría distinta a la etiquetada originalmente. No se identificaron errores por 

Negación, ironía o dialecto, fenómenos poco relevantes en el registro formal y 

estandarizado de los resúmenes científicos.



\*\*Impacto en el contexto:\*\* Si este modelo se usara para ayudar a investigadores a 

navegar rápidamente la literatura médica (el propósito original del dataset), la 

Confusión entre "results" y "conclusions" podría hacer que un usuario se salte 

información relevante, asumiendo que ya llego a la interpretación final del estudio 

cuando en realidad está leyendo un hallazgo sin contextualizar, o viceversa. Para la 

clase "objective", un recall bajo significa que las herramientas automáticas de resumen 

Podrían omitir la pregunta de investigación explicita de un paper, obligando al lector 

a buscarla manualmente de todas formas.



\*\*Limitación del dataset:\*\* El corpus cubre únicamente resúmenes de ensayos clínicos 

aleatorizados (RCT) en inglés, estructurados según las convenciones de PubMed hasta 2017. 

Un modelo entrenado aquí no debería aplicarse a notas clínicas de pacientes reales, 

estudios observacionales, revisiones sistemáticas, ni a literatura en otros idiomas, sin 

antes validar su desempeño en ese nuevo dominio. Además, la ausencia de licencia explicita 

sobre el texto de los resúmenes (documentada desde el LAB04) sigue siendo un riesgo legal 

declarado, no resuelto por este laboratorio.



\*\*Decisión antes del despliegue:\*\* Antes de integrar este modelo en una aplicación real, 

Recomendaría: (1) exponer la probabilidad de la predicción (predict\_proba) en la interfaz 

de Streamlit, en vez de solo la etiqueta final, para que el usuario pueda juzgar cuando 

una predicción es poco confiable; (2) explorar técnicas específicas para mejorar él 

recall de la clase minoritaria "objective", como ajustar pesos de clase más allá de 

'balanced' o aplicar sobremuestreo; y (3) considerar que la tarea original fue diseñada 

como clasificación secuencial (el orden de las oraciones importa), mientras que este 

pipeline trata cada oración de forma aislada, ignorando el contexto de las oraciones 

vecinas del mismo resumen, lo cual probablemente explica buena parte de la confusión 

observada entre "results" y "conclusions".



\*\*Prueba de robustez de la aplicación (Streamlit):\*\* Se probo el modelo con dos entradas 

contrastantes: una oración metodológica en inglés, propia del dominio de entrenamiento, 

que fue correctamente clasificada como "methods"; y una frase en español, completamente 

fuera de dominio ("Excelente servicio"), que el modelo clasifico como "background" con 

la misma aparente confianza. La aplicación muestra una advertencia genérica y estática 

en ambos casos, pero no distingue dinámicamente entre una predicción confiable y una que 

probablemente no lo es, ya que no expone la probabilidad de la predicción al usuario. 

Esto confirma que la responsabilidad de interpretar los límites del modelo recae 

completamente en quien lo usa, no en el sistema mismo.

