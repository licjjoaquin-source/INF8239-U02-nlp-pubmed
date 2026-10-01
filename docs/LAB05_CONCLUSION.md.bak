\## Cierre interpretativo (LAB05)



\*\*Resultado principal:\*\* Se entrenaron y compararon tres clasificadores de texto sobre 

el corpus PubMed 20k RCT: un baseline (dummy), Complement Naive Bayes y regresion 

logistica, todos usando TF-IDF con n-gramas (1,2) dentro de un pipeline que evita fuga 

de informacion. La regresion logistica obtuvo el mejor F1-macro (0.758), superando 

ampliamente al baseline (0.099) y al Naive Bayes (0.689).



\*\*Modelo seleccionado y evidencia:\*\* Se selecciono la regresion logistica como modelo 

final (models/text\_model.joblib, \~52.5 MB), respaldada por su F1-macro de 0.758 y una 

accuracy de 0.82 sobre 44,721 oraciones de prueba, con reporte de clasificacion completo 

guardado en reports/text\_metrics.csv y matriz de confusion en reports/confusion\_text.png.



\*\*Clase con mayor dificultad:\*\* La clase "objective" presento el menor recall (0.63) y 

la menor precision (0.61), consistente con ser la clase minoritaria del corpus (7.7% del 

total). La matriz de confusion revelo que 876 casos reales de "objective" se clasificaron 

erroneamente como "background", superando incluso a sus propios aciertos relativos.



\*\*Tipo de error mas frecuente:\*\* Al categorizar manualmente 20 errores, el 45% correspondio 

a ambiguedad genuina entre resultados y conclusiones (oraciones que combinan un hallazgo 

cuantitativo con su interpretacion en la misma frase) y un 35% adicional a etiquetas 

discutibles, donde incluso un lector humano experto podria razonablemente asignar una 

categoria distinta a la etiquetada originalmente. No se identificaron errores por 

negacion, ironia o dialecto, fenomenos poco relevantes en el registro formal y 

estandarizado de los resumenes cientificos.



\*\*Impacto en el contexto:\*\* Si este modelo se usara para ayudar a investigadores a 

navegar rapidamente la literatura medica (el proposito original del dataset), la 

confusion entre "results" y "conclusions" podria hacer que un usuario se salte 

informacion relevante, asumiendo que ya llego a la interpretacion final del estudio 

cuando en realidad esta leyendo un hallazgo sin contextualizar, o viceversa. Para la 

clase "objective", un recall bajo significa que las herramientas automaticas de resumen 

podrian omitir la pregunta de investigacion explicita de un paper, obligando al lector 

a buscarla manualmente de todas formas.



\*\*Limitacion del dataset:\*\* El corpus cubre unicamente resumenes de ensayos clinicos 

aleatorizados (RCT) en ingles, estructurados segun las convenciones de PubMed hasta 2017. 

Un modelo entrenado aqui no deberia aplicarse a notas clinicas de pacientes reales, 

estudios observacionales, revisiones sistematicas, ni a literatura en otros idiomas, sin 

antes validar su desempeno en ese nuevo dominio. Ademas, la ausencia de licencia explicita 

sobre el texto de los resumenes (documentada desde el LAB04) sigue siendo un riesgo legal 

declarado, no resuelto por este laboratorio.



\*\*Decision antes del despliegue:\*\* Antes de integrar este modelo en una aplicacion real, 

recomendaria: (1) exponer la probabilidad de la prediccion (predict\_proba) en la interfaz 

de Streamlit, en vez de solo la etiqueta final, para que el usuario pueda juzgar cuando 

una prediccion es poco confiable; (2) explorar tecnicas especificas para mejorar el 

recall de la clase minoritaria "objective", como ajustar pesos de clase mas alla de 

'balanced' o aplicar sobremuestreo; y (3) considerar que la tarea original fue disenada 

como clasificacion secuencial (el orden de las oraciones importa), mientras que este 

pipeline trata cada oracion de forma aislada, ignorando el contexto de las oraciones 

vecinas del mismo resumen, lo cual probablemente explica buena parte de la confusion 

observada entre "results" y "conclusions".



\*\*Prueba de robustez de la aplicacion (Streamlit):\*\* Se probo el modelo con dos entradas 

contrastantes: una oracion metodologica en ingles, propia del dominio de entrenamiento, 

que fue correctamente clasificada como "methods"; y una frase en espanol, completamente 

fuera de dominio ("Excelente servicio"), que el modelo clasifico como "background" con 

la misma aparente confianza. La aplicacion muestra una advertencia generica y estatica 

en ambos casos, pero no distingue dinamicamente entre una prediccion confiable y una que 

probablemente no lo es, ya que no expone la probabilidad de la prediccion al usuario. 

Esto confirma que la responsabilidad de interpretar los limites del modelo recae 

completamente en quien lo usa, no en el sistema mismo.

