---
tags: [busqueda-empleo, perfil]
actualizado: 2026-10-13
---
# Contexto y perfil

## Situación actual
- Desarrollador Mid Senior en DiSí Operaciones (fintech/SOFOM, crédito a PyMEs), ~3 años; ascenso a inicios de 2026.
- Radica en CDMX.
- Pretensión salarial: 30k MXN netos (aclarar siempre bruto/neto y nómina vs. honorarios).
- Stack: ASP.NET MVC / .NET Framework sobre IIS, SQL Server. Además, un servicio de generación de PDFs con Next.js y Puppeteer, implementado con IA (no domina esa tecnología).

## Proyectos en DiSí (para CV y guion de entrevista)
- Reestructuración del workflow de la empresa
- Dashboard de gestión de cobranza (APIs de Twilio y Kobra)
- Crédito revolvente completo: cálculos, gestión interna y lado del cliente
- 3 versiones de onboarding centradas en UX/UI
- Gestión del área de originación de crédito (APIs de Ekatena y Google Maps) para dictaminación
- Módulos internos para el área operativa
- Portal del cliente para gestión de líneas de crédito
- Monitoreo de aplicaciones en producción
- Integración de WhatsApp API en el onboarding con validaciones en tiempo real
- Reportes, presentaciones y videos demostrativos de cada desarrollo

## Brechas identificadas
- Fundamentos de C# y .NET moderno (ASP.NET Core en .NET 10 LTS) → teoría en [[10 Teoria de CSharp]]
- Vocabulario técnico
- Integraciones de API hechas con ayuda de IA, nunca de punta a punta solo
- Nunca ha levantado un proyecto desde cero

## Cómo aprende Alex
- **No asumir vocabulario.** Cada término técnico se define antes de usarlo y se desglosa hasta los fundamentos (de la CPU hacia arriba), con analogías de la vida diaria y anclas a lo que sí conoce: las apps de DiSí y el [[05 Arbol de fundamentos]]. Ojo: trabaja con IIS y `web.config` pero no conocía sus conceptos; explicarlos antes de usarlos como ancla.
- **Definición de entrevista primero** (2026-10-19): cada concepto clave empieza con una definición corta, lista para decirla en una entrevista, y después viene la explicación desde los fundamentos que la justifica.
- **No conoce Node.js ni Next.js** (2026-10-13). Solo los tocó en la generación de PDFs con Puppeteer, implementada con IA; no sirven como ancla: no usarlos para explicar nada.
- 2026-10-13, dudas sobre la sección 1 de [[10 Teoria de CSharp]]: qué son el SDK y el runtime, qué es una CLI, qué significa compilar, qué hace el CLR más allá de su definición, qué es y qué contiene una DLL. Respondidas al reescribir esa sección desde cero.
- 2026-10-13, más dudas: qué es IIS, qué es el heap, qué es IntelliSense → [[15 Dudas resueltas]].
- 2026-10-13, primera evaluación: 6.9 de 10 en la sección 1 de la teoría. Patrón: contesta solo la primera parte de las preguntas compuestas → [[14 Evaluaciones]].
- 2026-10-19, dudas de la sección 2: si `Program.cs` lo genera el compilador, qué es un método, qué es `Main` y el punto de entrada, solución vs. proyecto, paquetes resueltos, el `.pdb` → [[15 Dudas resueltas]]. Evaluación: 5.3; el patrón de contestar solo la primera parte se repite ([[14 Evaluaciones]]).
- Usa las técnicas de estudio de [[11 Clase 0.1 Datos]] y el sistema de repaso de [[13 Plan de memorizacion]] para retener a largo plazo.

## Herramientas y repos del plan
- IDE: Visual Studio 2026 con .NET 10 LTS; sugerencias de Copilot apagadas durante el plan.
- Repos de GitHub: `plan-dotnet` (ejercicios, semanas 1 a 5), `SolicitudesApi` (API de portafolio, semanas 6 a 11) y `GcalPlan` (integración con Google Calendar, semana 8).
- Horario: ~12 h por semana (detalle en [[03 Plan para huir de DiSi]] y [[04 Calendario dia por dia]]).

## Objetivo
- Corto plazo: puesto .NET mid-senior con 30k MXN netos.
- Después del plan: llegar a senior siguiendo [[07 Ruta a NET senior]].
