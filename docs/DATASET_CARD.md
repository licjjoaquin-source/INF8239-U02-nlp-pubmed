# Dataset Card

## Identificación
- Nombre: PubMed 20k RCT
- Fuente original: https://github.com/Franck-Dernoncourt/pubmed-rct (subconjunto PubMed_20k_RCT)
- Responsable: Franck Dernoncourt y Ji Young Lee (IJCNLP 2017)
- Versión o fecha: 2017
- Licencia: sin licencia explicita declarada por los autores. El repositorio indica que los datos derivan de PubMed/MEDLINE y que es responsabilidad del usuario determinar restricciones de copyright sobre resúmenes específicos. Uso académico ampliamente aceptado (cientos de citas).
- Idioma: inglés

## Propósito y variable objetivo
Clasificar el rol retórico de cada oración dentro de un resumen de ensayo clínico aleatorizado (RCT). La variable objetivo (label) tiene 5 clases: background, objective, methods, results, conclusions. Esto apoya herramientas que ayuden a investigadores a leer literatura médica estructurada más eficientemente.

## Diccionario de datos

| Columna | Tipo | Descripción | Valores o unidad |
|---|---|---|---|
| text | texto | Oración individual extraída de un resumen de RCT | Cadena de texto en inglés, 2 a 1454 caracteres |
| label | categórica | Rol retórico de la oración dentro del resumen | background, objective, methods, results, conclusions |

## Procedimiento de obtención
Descarga automatizada vía scripts/prepare_pubmed_rct.py, que obtiene el archivo train.txt del subconjunto PubMed_20k_RCT (formato de texto con marcadores ###ID y líneas ETIQUETA-tab-oración), y lo convierte a data/raw/dataset.csv con columnas text y label. Hash SHA-256 registrado para trazabilidad.

## Calidad observada
- 180,040 filas, 0 valores nulos en text o label.
- 1,158 textos duplicados detectados (0.64% del total). Se decidió CONSERVARLOS, ya que representan frases genéricas y repetitivas naturales del lenguaje científico (ej. frases estándar de resultados estadísticos), no errores de carga. Riesgo declarado: si no se controla el split train/test, estos duplicados podrían aparecer en ambos conjuntos e inflar artificialmente el desempeño reportado. Mitigación prevista para LAB05: verificar que la division train/test no genere fuga por duplicados exactos.
- Distribución de clases desbalanceada: methods (33.0%), results (32.2%), conclusions (15.1%), background (12.1%), objective (7.7%). Se recomienda usar F1-macro como métrica principal, no accuracy.
- Longitud de texto: mediana 139 caracteres, percentil 90 en 252, percentil 99 en 404, máximo 1454 (cola larga de oraciones inusualmente extensas).

## Población cubierta y excluida
Cubre únicamente resúmenes de ensayos clínicos aleatorizados (RCT) estructurados, escritos en inglés, indexados en PubMed/MEDLINE hasta el corte de recolección del dataset (2017). Excluye estudios observacionales, revisiones sistemáticas, casos clínicos individuales, y cualquier literatura en otro idioma. No representa investigación médica más reciente ni de otras bases de datos bibliográficas.

## Riesgos, sesgos y usos prohibidos
- Riesgo de licencia: ausencia de licencia explicita; no debe asumirse libertad total de redistribución del texto completo de los resúmenes.
- Sesgo de idioma: cubre exclusivamente literatura en inglés, no representativo de investigación publicada en español u otros idiomas.
- Sesgo de dominio: limitado a RCTs estructurados; un modelo entrenado aquí no generalizaría bien a notas clínicas de pacientes reales, historias clínicas, o texto conversacional médico (dominios lingueisticamente distintos).
- Uso prohibido: no debe usarse para inferir o validar afirmaciones clínicas sobre pacientes reales; es un dataset de clasificación de ESTRUCTURA de texto, no de contenido médico verificado.

## Cierre interpretativo

**Resultado principal:** Se seleccionó y válido el dataset PubMed 20k RCT (180,040 oraciones etiquetadas en 5 clases retóricas) como corpus aprobado para la Unidad 02, descartando el candidato Drug Reviews (UCI) por sus restricciones de licencia más severas (prohibición explicita de uso comercial y redistribución).

**Evidencia de calidad y procedencia:** Descarga reproducible mediante script propio (scripts/prepare_pubmed_rct.py) con hash SHA-256 registrado. Auditoria automatizada confirmo 0 valores nulos, 1,158 duplicados (0.64%, documentados y conservados), y distribución de clases desbalanceada (methods 33%, objective 7.7% como minoritaria).

**Riesgo o sesgo identificado:** Ausencia de licencia explicita sobre el texto de los resúmenes (riesgo legal declarado por los propios autores del dataset); cobertura limitada a literatura en inglés sobre ensayos clínicos aleatorizados estructurados, sin representar notas clínicas reales de pacientes ni otros idiomas.

**Decisión de aprobación o rechazo:** Aprobado con riesgo de licencia declarado, dado el uso académico ampliamente aceptado en la comunidad científica (cientos de citas y trabajos derivados publicados).

**Limitación que debe comunicarse:** Un modelo entrenado en este corpus clasifica ESTRUCTURA retórica de resúmenes científicos, no el contenido médico en sí; no debe interpretarse como validación de afirmaciones clínicas ni aplicarse directamente a notas clínicas de pacientes reales sin reentrenamiento.

**Siguiente verificación:** Confirmar en LAB05 que la division train/test controle el riesgo de fuga por los 1,158 textos duplicados identificados en la auditoria.
