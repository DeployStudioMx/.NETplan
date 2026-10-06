# CLAUDE.md — Proyecto "Búsqueda de empleo .NET" de Alex

Instrucciones para Claude en cualquier sesión que trabaje en este repositorio. Léelas completas antes de tocar un archivo.

## Qué es este proyecto

Plan personal de Alex (desarrollador full stack .NET, Mid Senior en DiSí Operaciones, CDMX) para:

1. Reforzar fundamentos técnicos durante 12 semanas (5 oct – 27 dic 2026), sin vibe coding.
2. Conseguir un puesto .NET mid-senior (pretensión: 30k MXN netos).
3. Después, llegar a senior siguiendo `07 Ruta a NET senior.md`.

Empezó en una sesión de Cowork (30 sep – 5 oct 2026) y se trasladó a este repositorio, que incluye la bóveda completa de Obsidian. La historia completa de decisiones está en `01 Bitacora.md`.

## Reglas que no se rompen

0. **LA REGLA MÁS ESTRICTA: la memoria es un grafo.** La memoria del proyecto es la bóveda completa: cada nota es un nodo y cada `[[enlace]]` es una arista. Al actualizar la memoria, cada dato se escribe en **la nota que le corresponde** según la tabla "Qué se actualiza y cuándo" de `00 Indice.md`, y se conecta con `[[enlaces]]` a las notas relacionadas. **Nunca** se concentra la memoria en un solo `.md`: ni en la bitácora, ni en este archivo, ni en una nota resumen nueva. Si un dato no tiene nodo, se crea una nota nueva (siguiente número libre) enlazada desde el índice y desde al menos una nota relacionada; no puede quedar huérfana. Esta regla está por encima de todas las demás.
1. **`00 Indice.md` manda.** Contiene el árbol de archivos, la tabla "qué se actualiza y cuándo" y los **datos únicos del proyecto** (horario, fechas, niveles, IDE, repos, salario). Antes de cualquier cambio, consulta esa tabla y actualiza **todos** los archivos que indica, en el mismo commit.
2. **Todo en la raíz, sin subcarpetas ni duplicados.** Cada documento existe una sola vez como `.md`; si viene de Claude Docs o del generador del calendario, tiene además un solo `.pdf` con el mismo nombre. Imágenes con el número de su nota (`05 diagrama arbol.png`). Nunca crear copias resumen.
3. **Bitácora en cada cambio.** Toda decisión o cambio relevante se anota en `01 Bitacora.md`, con fecha, lo más reciente arriba. La bitácora solo registra *qué* cambió y enlaza con `[[ ]]` a la nota donde vive el dato; el dato en sí va en su propio nodo (regla 0).
4. **Coherencia total.** Si cambia un dato único (por ejemplo, las horas por semana), se cambia en todos los archivos, incluidos los PDF. Verifica al final con una búsqueda de términos viejos y de `[[enlaces]]` rotos.
5. **Idioma:** español, tono directo y cálido.
6. **Modo tutor en el código del plan.** Alex escribe el código de sus ejercicios (`plan-dotnet`, `SolicitudesApi`, `GcalPlan`). Claude explica, revisa y pregunta, pero **no le da el código**. Si no puede explicar una línea, no está terminada. Esta regla aplica a los ejercicios del plan, no al mantenimiento de este repo.

## Estructura

| Archivo | Qué es | Cómo se mantiene |
| --- | --- | --- |
| [[00 Indice]] | Árbol, reglas y datos únicos | A mano |
| [[01 Bitacora]] | Decisiones y pendientes | A mano, en cada cambio |
| [[02 Contexto y perfil]] | Punto de partida, proyectos en DiSí, brechas, objetivo | A mano |
| [[03 Plan para huir de DiSi]] / `.pdf` | Plan de 12 semanas | Original en Claude Docs (ver abajo) |
| [[04 Calendario dia por dia]] / `.pdf` | Qué hacer cada día | **Generado**: editar `calendario_datos.py` y correr `calendario_render.py` |
| [[05 Arbol de fundamentos]] / `.pdf` | 8 niveles (0 a 7) antes de OAuth | Original en Claude Docs |
| [[06 Clase OAuth 2.0]] / `.pdf` | Clase completa de OAuth | Original en Claude Docs |
| [[07 Ruta a NET senior]] / `.pdf` | 12 temas después del plan | Original en Claude Docs |
| [[08 Glosario]] | Términos de Alex | Lo llena Alex |
| [[09 Registro de aplicaciones]] | Vacantes y procesos | Lo llena Alex |
| `calendario_datos.py` | Contenido día por día del calendario | Fuente de verdad del calendario |
| `calendario_render.py` | Genera el PDF y el `.md` del calendario | `pip install reportlab` y `python calendario_render.py` |

## Originales en Claude Docs

| Nota | Enlace |
| --- | --- |
| 03 Plan para huir de DiSi | https://claude.ai/code/artifact/bc0d4a59-6825-49e1-937f-078e8fb92d27 |
| 05 Arbol de fundamentos | https://claude.ai/code/artifact/06402dff-f253-4fb4-bfcd-5a113e910c97 |
| 06 Clase OAuth 2.0 | https://claude.ai/code/artifact/4e829660-4189-4331-89b4-d2fae7c5a36b |
| 07 Ruta a NET senior | https://claude.ai/code/artifact/c2dac5ec-cad9-4fd6-b607-ff5c7e9544a2 |

Estos docs viven en la cuenta de Claude de la organización de DiSí. Si tu sesión puede editarlos, cambia el doc y el `.md` + `.pdf` del repo juntos. Si no puede, edita el `.md` del repo, regenera el `.pdf` con lo que tengas disponible (por ejemplo `pandoc`) y anota en la bitácora que el original en Claude Docs quedó desfasado. A partir de este traslado, **el repositorio es la fuente de verdad**.

## Estado al momento del traslado (5 oct 2026)

- Hoy arranca la **semana 1**: 0.1 Datos y 0.2 Hardware (teoría) + `dotnet` CLI, tipos y métodos (código). Detalle en `04 Calendario dia por dia.md`.
- Pendientes abiertos: ver `## Pendientes` en `01 Bitacora.md` (CV con logros, guion de proyectos de DiSí, simulacro técnico, integración con Google Calendar en la semana 8).
- Google Calendar: Alex lo integrará él mismo con la API (OAuth de escritorio, cuenta personal) en la semana 8, repo `GcalPlan`.
- Después del plan: posible enfoque en arquitectura de software (ver `07 Ruta a NET senior.md`).

## Privacidad

Este repo contiene datos personales (pretensión salarial, correo personal, planes de cambio de empleo). Debe ser **privado** y no compartirse con cuentas o equipos de DiSí.
