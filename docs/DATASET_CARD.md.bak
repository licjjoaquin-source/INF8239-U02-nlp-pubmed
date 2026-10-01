# Dataset Card

## Identificacion
- Nombre: PubMed 20k RCT
- Fuente original: https://github.com/Franck-Dernoncourt/pubmed-rct (subconjunto PubMed_20k_RCT)
- Responsable: Franck Dernoncourt y Ji Young Lee (IJCNLP 2017)
- Version o fecha: 2017
- Licencia: sin licencia explicita declarada por los autores. El repositorio indica que los datos derivan de PubMed/MEDLINE y que es responsabilidad del usuario determinar restricciones de copyright sobre resumenes especificos. Uso academico ampliamente aceptado (cientos de citas).
- Idioma: ingles

## Proposito y variable objetivo
Clasificar el rol retorico de cada oracion dentro de un resumen de ensayo clinico aleatorizado (RCT). La variable objetivo (label) tiene 5 clases: background, objective, methods, results, conclusions. Esto apoya herramientas que ayuden a investigadores a leer literatura medica estructurada mas eficientemente.

## Diccionario de datos

| Columna | Tipo | Descripcion | Valores o unidad |
|---|---|---|---|
| text | texto | Oracion individual extraida de un resumen de RCT | Cadena de texto en ingles, 2 a 1454 caracteres |
| label | categorica | Rol retorico de la oracion dentro del resumen | background, objective, methods, results, conclusions |

## Procedimiento de obtencion
Descarga automatizada via scripts/prepare_pubmed_rct.py, que obtiene el archivo train.txt del subconjunto PubMed_20k_RCT (formato de texto con marcadores ###ID y lineas ETIQUETA-tab-oracion), y lo convierte a data/raw/dataset.csv con columnas text y label. Hash SHA-256 registrado para trazabilidad.

## Calidad observada
- 180,040 filas, 0 valores nulos en text o label.
- 1,158 textos duplicados detectados (0.64% del total). Se decidio CONSERVARLOS, ya que representan frases genericas y repetitivas naturales del lenguaje cientifico (ej. frases estandar de resultados estadisticos), no errores de carga. Riesgo declarado: si no se controla el split train/test, estos duplicados podrian aparecer en ambos conjuntos e inflar artificialmente el desempeno reportado. Mitigacion prevista para LAB05: verificar que la division train/test no genere fuga por duplicados exactos.
- Distribucion de clases desbalanceada: methods (33.0%), results (32.2%), conclusions (15.1%), background (12.1%), objective (7.7%). Se recomienda usar F1-macro como metrica principal, no accuracy.
- Longitud de texto: mediana 139 caracteres, percentil 90 en 252, percentil 99 en 404, maximo 1454 (cola larga de oraciones inusualmente extensas).

## Poblacion cubierta y excluida
Cubre unicamente resumenes de ensayos clinicos aleatorizados (RCT) estructurados, escritos en ingles, indexados en PubMed/MEDLINE hasta el corte de recoleccion del dataset (2017). Excluye estudios observacionales, revisiones sistematicas, casos clinicos individuales, y cualquier literatura en otro idioma. No representa investigacion medica mas reciente ni de otras bases de datos bibliograficas.

## Riesgos, sesgos y usos prohibidos
- Riesgo de licencia: ausencia de licencia explicita; no debe asumirse libertad total de redistribucion del texto completo de los resumenes.
- Sesgo de idioma: cubre exclusivamente literatura en ingles, no representativo de investigacion publicada en espanol u otros idiomas.
- Sesgo de dominio: limitado a RCTs estructurados; un modelo entrenado aqui no generalizaria bien a notas clinicas de pacientes reales, historias clinicas, o texto conversacional medico (dominios lingueisticamente distintos).
- Uso prohibido: no debe usarse para inferir o validar afirmaciones clinicas sobre pacientes reales; es un dataset de clasificacion de ESTRUCTURA de texto, no de contenido medico verificado.

## Cierre interpretativo

**Resultado principal:** Se selecciono y valido el dataset PubMed 20k RCT (180,040 oraciones etiquetadas en 5 clases retoricas) como corpus aprobado para la Unidad 02, descartando el candidato Drug Reviews (UCI) por sus restricciones de licencia mas severas (prohibicion explicita de uso comercial y redistribucion).

**Evidencia de calidad y procedencia:** Descarga reproducible mediante script propio (scripts/prepare_pubmed_rct.py) con hash SHA-256 registrado. Auditoria automatizada confirmo 0 valores nulos, 1,158 duplicados (0.64%, documentados y conservados), y distribucion de clases desbalanceada (methods 33%, objective 7.7% como minoritaria).

**Riesgo o sesgo identificado:** Ausencia de licencia explicita sobre el texto de los resumenes (riesgo legal declarado por los propios autores del dataset); cobertura limitada a literatura en ingles sobre ensayos clinicos aleatorizados estructurados, sin representar notas clinicas reales de pacientes ni otros idiomas.

**Decision de aprobacion o rechazo:** Aprobado con riesgo de licencia declarado, dado el uso academico ampliamente aceptado en la comunidad cientifica (cientos de citas y trabajos derivados publicados).

**Limitacion que debe comunicarse:** Un modelo entrenado en este corpus clasifica ESTRUCTURA retorica de resumenes cientificos, no el contenido medico en si; no debe interpretarse como validacion de afirmaciones clinicas ni aplicarse directamente a notas clinicas de pacientes reales sin reentrenamiento.

**Siguiente verificacion:** Confirmar en LAB05 que la division train/test controle el riesgo de fuga por los 1,158 textos duplicados identificados en la auditoria.
