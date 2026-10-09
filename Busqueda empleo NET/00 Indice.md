---
tags: [busqueda-empleo, indice]
actualizado: 2026-10-09
---
# Búsqueda de empleo .NET — Índice

Proyecto para conseguir un puesto como desarrollador .NET mid-senior y llegar a senior, reforzando fundamentos técnicos en paralelo. Instrucciones para Claude: [[CLAUDE]].

**Regla más estricta — la memoria es un grafo:** la memoria del proyecto es esta bóveda completa; cada nota es un nodo y cada `[[enlace]]` una arista. Cada dato se guarda en la nota que le corresponde según la tabla de abajo y se enlaza a las notas relacionadas. Nunca se concentra la memoria en un solo `.md` (ni en [[01 Bitacora]], ni en [[CLAUDE]], ni en un resumen nuevo). Un dato sin nodo se vuelve una nota nueva, enlazada desde este índice y desde al menos una nota relacionada.

**Regla de estructura:** todo vive en la raíz, sin subcarpetas. Cada documento existe **una sola vez** como nota `.md`; si viene de un artifact de Claude o del generador del calendario, tiene además **un solo** `.pdf` con el mismo nombre. Las notas 08 y 09 son tuyas y no llevan PDF; la 10 se escribe directo en el repo y tampoco lleva PDF. Las imágenes llevan el número de la nota que las usa.

**Datos únicos del proyecto** (si cambian, se cambian en todos los archivos): ~12 h por semana (lun 1.5 h teoría, mar–jue 1.5 h código, vie 1 h búsqueda, sáb 4 h teoría, dom 45 min repos y revisión) · plan del 5 oct al 27 dic de 2026 · árbol de 8 niveles (0 a 7), ~28 h de teoría · Visual Studio 2026 + .NET 10 LTS · repos `plan-dotnet`, `SolicitudesApi` y `GcalPlan` · pretensión 30k MXN netos.

## Árbol de archivos

```
Busqueda empleo NET/
├── 00 Indice.md                         ← este archivo: árbol, reglas y datos únicos
├── 01 Bitacora.md                       ← registro fechado de decisiones y pendientes
├── 02 Contexto y perfil.md              ← punto de partida, experiencia, salario, brechas
├── 03 Plan para huir de DiSi.md / .pdf  ← plan de 12 semanas (original en Claude Docs)
├── 04 Calendario dia por dia.md / .pdf  ← qué hacer cada día (GENERADO por calendario_render.py)
├── 05 Arbol de fundamentos.md / .pdf    ← niveles 0 a 7 antes de OAuth (original en Claude Docs)
│   └── 05 diagrama arbol.png
├── 06 Clase OAuth 2.0.md / .pdf         ← clase completa de OAuth (original en Claude Docs)
│   └── 06 diagrama flujo oauth.png
├── 07 Ruta a NET senior.md / .pdf       ← 12 temas después del plan (original en Claude Docs)
│   └── 07 diagrama flujo aplicacion.png
├── 08 Glosario.md                       ← tus términos (lo llenas tú; meta: 100)
├── 09 Registro de aplicaciones.md       ← una fila por vacante (lo llenas tú los viernes)
├── 10 Teoria de CSharp.md               ← teoría del lenguaje, 20 min al inicio de cada día de código
├── calendario_datos.py                  ← contenido día por día del calendario (fuente)
├── calendario_render.py                 ← genera 04 Calendario .md + .pdf
├── CLAUDE.md                            ← reglas para cualquier sesión de Claude
├── README.md                            ← portada del repositorio
└── .gitignore
```

## Qué se actualiza y cuándo

| Cuando pasa esto… | Se modifican estos archivos (todos, en el mismo momento) |
| --- | --- |
| Cualquier cambio en la memoria del proyecto | El dato va **en su nodo** (el archivo afectado de esta tabla), enlazado con `[[ ]]` a sus notas relacionadas; `01 Bitacora` solo lleva una entrada fechada que enlaza a ese nodo. Nunca todo en un solo `.md` |
| Cambia un dato de perfil (salario, experiencia, CV, brechas) | `02 Contexto y perfil` + `01 Bitacora` |
| Cambia el plan | `03 Plan para huir de DiSi.md` + `.pdf` (y el original en Claude Docs si la sesión lo permite); si cambian días, horas o tareas también el calendario; + `01 Bitacora` |
| Cambia el calendario (días, horas, tareas) | Editar `calendario_datos.py` y correr `python calendario_render.py` (regenera `04` `.md` + `.pdf`); si cambia el resumen semanal, `03 Plan` `.md` + `.pdf`; + `01 Bitacora` |
| Cambia el árbol de fundamentos | `05 Arbol de fundamentos.md` + `.pdf` (+ `05 diagrama arbol.png` si cambia el diagrama); + `01 Bitacora` |
| Cambia la clase de OAuth | `06 Clase OAuth 2.0.md` + `.pdf` (+ su diagrama); + `01 Bitacora` |
| Cambia o se agrega teoría de C# | `10 Teoria de CSharp.md` (la sección de cada semana se escribe antes de que empiece); si cambia qué sección toca qué día, también `calendario_datos.py` y regenerar `04`; + `01 Bitacora` |
| Cambia la ruta a senior | `07 Ruta a NET senior.md` + `.pdf` (+ su diagrama); + `01 Bitacora` |
| Se crea un documento nuevo | `NN Nombre.md` (+ `.pdf` y `NN diagrama ….png` si aplica) con el siguiente número libre; agregarlo al árbol, a las notas de este índice y a `CLAUDE.md`; + `01 Bitacora` |
| Cambian las reglas de trabajo | Este índice + `CLAUDE.md` + `01 Bitacora` |
| Se renombra o renumera un archivo | Actualizar todos los `[[enlaces]]` de la carpeta, este índice y `CLAUDE.md` |
| Termina una semana del plan | Marcar casillas en `04 Calendario`; entrada en `01 Bitacora` con avance y dudas |
| Aprendes un término nuevo | Fila en `08 Glosario` |
| Aplicas a una vacante o avanza un proceso | Fila en `09 Registro de aplicaciones`; si cambia la pretensión o el CV, también `02 Contexto` |

**Nunca:** crear copias resumen de un documento que ya existe, ni subcarpetas, ni editar a mano `04 Calendario dia por dia.md` (se sobrescribe al regenerar).

## Notas
- [[01 Bitacora]] — decisiones y pendientes
- [[02 Contexto y perfil]] — punto de partida
- [[03 Plan para huir de DiSi]] · [[03 Plan para huir de DiSi.pdf|PDF]]
- [[04 Calendario dia por dia]] · [[04 Calendario dia por dia.pdf|PDF]]
- [[05 Arbol de fundamentos]] · [[05 Arbol de fundamentos.pdf|PDF]]
- [[06 Clase OAuth 2.0]] · [[06 Clase OAuth 2.0.pdf|PDF]]
- [[07 Ruta a NET senior]] · [[07 Ruta a NET senior.pdf|PDF]]
- [[08 Glosario]] — tus términos
- [[09 Registro de aplicaciones]] — vacantes y procesos
- [[10 Teoria de CSharp]] — teoría del lenguaje para los días de código

## Originales en Claude Docs
| Nota | Enlace |
| --- | --- |
| 03 Plan para huir de DiSi | https://claude.ai/code/artifact/bc0d4a59-6825-49e1-937f-078e8fb92d27 |
| 05 Arbol de fundamentos | https://claude.ai/code/artifact/06402dff-f253-4fb4-bfcd-5a113e910c97 |
| 06 Clase OAuth 2.0 | https://claude.ai/code/artifact/4e829660-4189-4331-89b4-d2fae7c5a36b |
| 07 Ruta a NET senior | https://claude.ai/code/artifact/c2dac5ec-cad9-4fd6-b607-ff5c7e9544a2 |
