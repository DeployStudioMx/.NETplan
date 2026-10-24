---
tags: [busqueda-empleo, bitacora]
actualizado: 2026-10-24
---
# Bitácora

Registro fechado, lo más reciente arriba. Se actualiza cada vez que cambia la memoria del proyecto.

## 2026-10-24
- Alex no tenía creado el repo `plan-dotnet` (tarea del 2 oct en [[04 Calendario dia por dia]]). Agregado a [[12 Clase Primer proyecto por CLI]] el laboratorio 0: qué es un repositorio, configurar Git, crear `plan-dotnet` público en la cuenta personal (README sí, .gitignore no) y clonarlo en `C:\Repos`. 4 tarjetas nuevas en `csharp/lab-primer-proyecto` ([[13 Plan de memorizacion]]).

## 2026-10-23
- Alex terminó la sección 3 de [[10 Teoria de CSharp]] (día 0 de la unidad `csharp/s3-tipos`). Registro y fechas en [[13 Plan de memorizacion]]. Limpieza de pendientes ya cumplidos.

## 2026-10-19
- Agregada al inicio de la sección 3 de [[10 Teoria de CSharp]] la definición de entrevista de "tipo", con una tarjeta nueva. Preferencia nueva de Alex: definición de entrevista primero, luego los fundamentos ([[02 Contexto y perfil]], regla 7 de [[CLAUDE]]).
- A pedido de Alex, reescrita también la sección 2 de [[10 Teoria de CSharp]] desde los fundamentos: proyecto y plantilla, XML y cada línea del `.csproj` (tipo de SDK, `OutputType`, TFM, espacio de nombres y `using`, `null` y advertencias), `.csproj` de .NET Framework vs. moderno, `Program.cs` con método, clase, punto de entrada y `Main`, paquetes y restore, `obj`, `bin` (con `deps.json` y `.pdb`), Debug vs. Release, `.gitignore` y proyecto vs. solución. Integra las respuestas de [[15 Dudas resueltas]] del 19 oct. 21 tarjetas nuevas en `csharp/s2-anatomia-proyecto` ([[13 Plan de memorizacion]]); PDFs regenerados.
- El sync del celular juntó bien la sección 3 nueva con las fechas de repaso, pero Obsidian volvió a guardar la versión vieja de [[10 Teoria de CSharp]] que tenía abierta. Regla nueva en [[13 Plan de memorizacion]]: cerrar todas las notas antes de cada pull o sync.
- A pedido de Alex, reescrita la sección 3 de [[10 Teoria de CSharp]] desde los fundamentos, igual que la 1: memoria y casillas, variable, tipo, tipado estático y fuerte, `var` y `const`, tipos básicos (con signo, exacto vs. aproximado), alias y espacio de nombres, valor vs. referencia, literales, conversiones (cast, `Parse`, `TryParse`, excepción, `out`), desbordamiento con complemento a dos y `checked`, interpolación y cultura. Ningún concepto se usa antes de explicarlo. 25 tarjetas en el mazo nuevo `csharp/s3-tipos` ([[13 Plan de memorizacion]]); PDF regenerado.
- Un respaldo automático del celular (`vault backup` 07:46) subió versiones viejas de [[01 Bitacora]], [[02 Contexto y perfil]], [[13 Plan de memorizacion]], [[14 Evaluaciones]] y [[15 Dudas resueltas]] encima de las nuevas. Restauradas desde el commit anterior conservando las fechas de repaso de las 55 tarjetas repasadas. Agregada a [[13 Plan de memorizacion]] la regla para el celular: sin auto commit-and-sync y reiniciar Obsidian después de cada pull.
- Alex estudió la sección 2 de [[10 Teoria de CSharp]]. Dudas (Program.cs, método, Main y punto de entrada, solución vs. proyecto, paquetes resueltos, .pdb) respondidas en [[15 Dudas resueltas]]; evaluación 16/30 (5.3) en [[14 Evaluaciones]]. Nueva unidad `csharp/s2-anatomia-proyecto` (17 tarjetas) en el registro de [[13 Plan de memorizacion]].

## 2026-10-15
- Mazos reorganizados **por unidad de estudio** para repasar solo lo ya estudiado: cada tarjeta empieza con su etiqueta (`#flashcards/csharp/s1-plataforma-net`, `…/errores`, `…/dudas`, `csharp/lab-primer-proyecto`, `fundamentos/0-1-datos`). Agregados a [[13 Plan de memorizacion]] el protocolo de cada unidad (día 0, 1, 2, 4, 8, 21), la respuesta a "¿releer o no?", el plan concreto para la sección 1 estudiada el 14 oct y el registro de unidades. Retiquetadas las tarjetas de [[10 Teoria de CSharp]], [[11 Clase 0.1 Datos]], [[12 Clase Primer proyecto por CLI]], [[14 Evaluaciones]] y [[15 Dudas resueltas]] (solo la etiqueta, sin cambiar contenido); PDFs regenerados.
- Definida la configuración completa del plugin Spaced Repetition en [[13 Plan de memorizacion]], verificada contra el código del plugin (v1.15.4): desactivar "Convert highlights to clozes" (el operador `==` de una tabla de [[10 Teoria de CSharp]] crearía una tarjeta falsa), activar el comentario de programación en la misma línea, quedarse con el algoritmo SM-2-OSR (FSRS lo marca el propio plugin como experimental). Definidos los 4 mazos (66 tarjetas), cómo repasar, cómo evitar conflictos de Git y el primer repaso. `clase_pdf.py` ahora oculta las fechas de repaso del plugin en los PDF.

## 2026-10-13
- Agregadas las respuestas textuales de Alex a [[14 Evaluaciones]]. Fin de la sesión del día.
- Primera evaluación: Alex contestó las 8 preguntas de repaso de la sección 1 de [[10 Teoria de CSharp]]; 55/80 (6.9). Detalle, correcciones y tarjetas de errores en [[14 Evaluaciones]].
- Dudas sobre IIS, heap e IntelliSense respondidas en [[15 Dudas resueltas]] (la teoría no se toca por decisión de Alex).
- Creado [[13 Plan de memorizacion]] (+ PDF): sistema de repaso a largo plazo con el plugin Spaced Repetition, escalera de comprensión, rutina diaria, semanal y mensual (exámenes acumulados el 31 oct, 28 nov y 26 dic) e historia "El viaje de Program.cs".
- Corregido el stack en [[02 Contexto y perfil]]: Next.js y Puppeteer solo se usaron para generar PDFs en DiSí, implementado con IA; no es su front principal.
- Alex no conoce Node.js ni Next.js: dejan de usarse como ancla al explicar ([[02 Contexto y perfil]], regla 7 de [[CLAUDE]]). Por decisión de Alex, [[10 Teoria de CSharp]] no se modifica por ahora, aunque su sección 1 menciona Node.js y JavaScript como comparación.
- Alex compartió sus dudas de la sección 1 de [[10 Teoria de CSharp]] (SDK, runtime, CLI, compilar, CLR, DLL). La sección se reescribió desde la CPU hacia arriba (código máquina, compilar, dos etapas IL/JIT, runtime, SDK y CLI, qué hace el CLR paso a paso, qué es y qué contiene un ensamblado), con ejercicios para comprobar en su máquina y 17 tarjetas; PDF regenerado. Registrado en [[02 Contexto y perfil]] cómo aprende y la nueva regla de profundidad en [[00 Indice]] y [[CLAUDE]].
- Generado el PDF de [[10 Teoria de CSharp]], que faltaba. `clase_pdf.py` ahora dibuja los diagramas Mermaid en el PDF. Regla actualizada en [[00 Indice]] y [[CLAUDE]]: la teoría de C# también lleva PDF y se regenera en cada cambio.

## 2026-10-12
- Creada [[12 Clase Primer proyecto por CLI]] (+ PDF): laboratorio guiado del martes 6 oct (preparar `plan-dotnet` con solución `.slnx`, explorar `bin`/`obj`, ficha de tipos y desbordamiento). Respeta el modo tutor: enunciados y pistas, sin código de solución. La teoría sigue en [[10 Teoria de CSharp]]. Enlazada desde el día 6 oct de [[04 Calendario dia por dia]], [[00 Indice]] y [[CLAUDE]].

## 2026-10-09
- Creada [[11 Clase 0.1 Datos]] (+ PDF): la clase completa del lunes 5 oct con técnicas de memorización y aprendizaje (pretest, recuperación activa, repetición espaciada, Feynman, chunking, codificación dual) y tarjetas para el plugin Spaced Repetition de Obsidian. Nuevo generador `clase_pdf.py` para el PDF de las clases. Enlazada desde el día 5 oct de [[04 Calendario dia por dia]], [[00 Indice]] y [[CLAUDE]].
- Detectado un hueco en el plan: el carril de código no tenía teoría del lenguaje C#. Creada [[10 Teoria de CSharp]] con la teoría de la semana 1 (qué es .NET, anatomía del proyecto, tipos, control de flujo, double vs. decimal, métodos, convenciones). Se lee 20 min al inicio de cada día de código, sin cambiar las ~12 h por semana. Agregada la lectura a los días 6, 7 y 8 oct de [[04 Calendario dia por dia]] (calendario y PDF regenerados). Enlazada desde [[00 Indice]], [[CLAUDE]], [[02 Contexto y perfil]] y [[08 Glosario]].
- Sincronización de la bóveda con el celular vía Obsidian Git. Agregado un `.gitignore` en la raíz del repositorio para que la configuración `.obsidian/` de cada dispositivo no se suba. El repositorio sigue siendo la fuente de verdad ([[CLAUDE]], [[00 Indice]]).

## 2026-10-06
- Regla nueva, la más estricta del proyecto: la memoria es un grafo. Cada actualización se escribe en la nota que le corresponde y se enlaza con `[[ ]]` a sus notas relacionadas; nunca se concentra en un solo `.md`. Esta bitácora solo registra el cambio y enlaza al nodo. Reglas en [[00 Indice]] y [[CLAUDE]].
- Reforzado el grafo: [[06 Clase OAuth 2.0]] y [[07 Ruta a NET senior]] ahora enlazan a sus notas relacionadas, [[03 Plan para huir de DiSi]] enlaza al [[05 Arbol de fundamentos]] con `[[ ]]` en lugar de la URL de Claude Docs, y la tabla de estructura de [[CLAUDE]] usa enlaces. Solo cambió la navegación de las notas; el texto de los PDF sigue igual, así que no se regeneraron.
- Publicada una vista interactiva del calendario como artifact (https://claude.ai/artifact/737Dvitbv6Eds9XijvuBJA), generada desde `calendario_datos.py`. Es de solo lectura: las casillas se siguen marcando en [[04 Calendario dia por dia]], que ahora enlaza al artifact en su encabezado. El PDF no cambió.

## 2026-10-05
- Traslado del proyecto de Cowork a un repositorio de Git para trabajarlo en sesiones de Claude Code. Se agregaron [[CLAUDE]] (reglas para Claude), README, .gitignore y el generador del calendario (`calendario_datos.py` + `calendario_render.py`). Desde ahora, el repositorio es la fuente de verdad.

## 2026-10-02
- El plan de 12 semanas se renombró a "Plan para huir de DiSí" (Claude Docs, nota y PDF: [[03 Plan para huir de DiSi]]).

## 2026-10-01
- Reorganizada la bóveda: todo en la carpeta raíz, sin subcarpetas ni duplicados. Eliminados la carpeta Artifacts y el resumen duplicado del plan. Renumerado: 03 Plan, 04 Calendario, 05 Árbol, 06 OAuth, 07 Ruta a senior. El índice ahora tiene el árbol de archivos y la tabla de qué actualizar en cada caso.
- Barrido de coherencia en todo el proyecto: horas unificadas en ~12 h por semana (antes aparecían 10 y 11.5), árbol en 8 niveles y 28 h (había 7 niveles y 30 h), .NET 10 en todas partes, tres repos definidos (plan-dotnet, SolicitudesApi, GcalPlan), glosario y registro de aplicaciones como notas propias ([[08 Glosario]], [[09 Registro de aplicaciones]]), revisión del domingo apuntando a 04 Calendario y a esta bitácora. Los datos únicos del proyecto quedaron en [[00 Indice]].

## 2026-09-30
- Inicio formal de la búsqueda de trabajo como programador .NET.
- Diagnóstico: mucha experiencia entregando apps full stack en DiSí, pero huecos en fundamentos de C#/.NET, terminología técnica y conexión de APIs sin IA. Sin escribir código a mano desde dic 2025.
- Elegido como primer paso: plan semana por semana (originalmente 8 semanas, ~10 h/semana, pendiente de confirmar horas).
- Creado el plan en Claude Docs → [[03 Plan para huir de DiSi]].
- Creada esta bóveda del proyecto. Regla: cada actualización de memoria se refleja aquí.
- Decidido usar Google Calendar (cuenta a.ortega8897@gmail.com) para controlar actividades y tiempos del plan. Conector nativo de Claude no disponible en la organización.
- Decisión: integrar Google Calendar con la API de Google directamente (OAuth2), no con la integración nativa de Claude.
- Bloqueo: la red del entorno en la nube de Claude no permite conexiones a googleapis.com (política de la organización), y la terminal local no arranca por la actualización de Windows del 8 de septiembre.
- Decisión: escribir yo mismo la integración con Google Calendar como consola en C# (`Google.Apis.Calendar.v3`), como ejercicio del plan. Claude guía y revisa; no me da el código.
- Clase de OAuth 2.0 en Claude Docs: https://claude.ai/code/artifact/4e829660-4189-4331-89b4-d2fae7c5a36b
- Conclusión: antes de OAuth necesito fundamentos previos. Creado el árbol de 7 niveles (redes, HTTP, navegador, APIs, criptografía, HTTPS, identidad y tokens, ~12 h): https://claude.ai/code/artifact/06402dff-f253-4fb4-bfcd-5a113e910c97
- Agregado el Nivel 0 al árbol (cómo funciona una computadora: bits, hardware, sistema operativo, cómo corre .NET) y profundizado redes (capas TCP/IP y OSI, MAC, subredes, NAT, DNS completo).
- Plan reestructurado de 8 a 12 semanas (5 oct – 27 dic 2026): teoría sábado + lunes siguiendo el árbol; código C# martes a jueves. Google Calendar pasa a la semana 8 → [[03 Plan para huir de DiSi]] (ahora de 12 semanas).
- Creado el calendario de sobremesa día por día (1 oct – 27 dic): [[04 Calendario dia por dia.pdf]].
- Decisión: el IDE del plan es Visual Studio 2026 (no VS Code), con .NET 10 LTS. En semanas 1–2 los proyectos se crean con el CLI y las sugerencias de Copilot quedan apagadas. Calendario y plan actualizados.
- Regla nueva: todo artifact que genere Claude se transcribe a la bóveda y se guarda también en PDF, en la carpeta Artifacts. Transcritos: plan de 12 semanas, árbol de fundamentos, clase de OAuth y calendario día por día.
- Agregado al plan el carril de los domingos (45 min): aprender a leer y presentar repositorios de GitHub (qué mira un reclutador, temario de 12 domingos con repos reales). La semana queda en ~11.5 h. Plan, calendario y transcripciones actualizados.
- Después del plan de 12 semanas: seguir con un tema que agregue valor al portafolio; considerando arquitectura de software aplicada (monolito modular, Clean Architecture/DDD, eventos) + Azure AZ-204. Sin decidir.
- Creada la ruta a .NET senior (12 temas por peso, orden por trimestres de 2027, con el flujo completo de una aplicación de Program.cs a la base de datos) → [[07 Ruta a NET senior]]. Tema de mayor interés: entender el flujo y la estructura de una aplicación completa.

## Pendientes
- [ ] Sección 3: dudas y respuestas a las 4 preguntas de repaso; día 1 el 24 oct, evaluación el 31 oct (junto con el examen acumulado) ([[13 Plan de memorizacion]])
- [ ] Sección 2: día 1 el 20 oct (volcado de memoria + primer repaso del mazo `s2-anatomia-proyecto`), evaluación el 27 oct ([[13 Plan de memorizacion]])
- [x] Definir por completo la configuración de las tarjetas en [[13 Plan de memorizacion]] (2026-10-15)
- [x] Instalar y configurar el plugin Spaced Repetition y comprobar los mazos ([[13 Plan de memorizacion]])
- [x] Día 1 de la sección 1: primer repaso del mazo `s1-plataforma-net`
- [ ] **Atrasada:** segunda evaluación de la sección 1 (era el 22 oct) en [[14 Evaluaciones]]
- [ ] Confirmar si Alex ya estudió la clase de 0.1 Datos ([[11 Clase 0.1 Datos]]) para activar su mazo
- [x] Sección 2 de [[10 Teoria de CSharp]] (19 oct)
- [ ] Exámenes acumulados: 31 oct, 28 nov y 26 dic ([[13 Plan de memorizacion]])
- [ ] Escribir en [[10 Teoria de CSharp]] la teoría de las semanas 2 a 5, cada una antes de que empiece (semana 2: antes del 13 oct)
- [ ] Confirmar que las ~12 horas por semana son realistas
- [ ] Reescribir CV con logros medibles
- [ ] Preparar guion de proyectos de DiSí
- [ ] Simulacro de entrevista técnica (diagnóstico)
- [ ] Estudiar el árbol de fundamentos (niveles 0 a 7), semanas 1 a 7
- [ ] Conectar Google Calendar vía API y agendar bloques de estudio (semana 8)
    - [ ] Paso 1: proyecto en Google Cloud + credentials.json
    - [ ] Paso 2: consola .NET 10 con paquetes NuGet
    - [ ] Paso 3: autenticación OAuth2 y listar calendarios
    - [ ] Paso 4: crear calendario "Plan .NET" y eventos
- [x] Terminal local funcionando de nuevo (2026-10-01)
