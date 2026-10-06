---
tags: [busqueda-empleo, bitacora]
actualizado: 2026-10-06
---
# Bitácora

Registro fechado, lo más reciente arriba. Se actualiza cada vez que cambia la memoria del proyecto.

## 2026-10-06
- Regla nueva, la más estricta del proyecto: la memoria es un grafo. Cada actualización se escribe en la nota que le corresponde y se enlaza con `[[ ]]` a sus notas relacionadas; nunca se concentra en un solo `.md`. Esta bitácora solo registra el cambio y enlaza al nodo. Reglas en [[00 Indice]] y [[CLAUDE]].
- Reforzado el grafo: [[06 Clase OAuth 2.0]] y [[07 Ruta a NET senior]] ahora enlazan a sus notas relacionadas, [[03 Plan para huir de DiSi]] enlaza al [[05 Arbol de fundamentos]] con `[[ ]]` en lugar de la URL de Claude Docs, y la tabla de estructura de [[CLAUDE]] usa enlaces. Solo cambió la navegación de las notas; el texto de los PDF sigue igual, así que no se regeneraron.

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
