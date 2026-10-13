---
tags: [busqueda-empleo, aprendizaje, memoria]
actualizado: 2026-10-13
---
> Sistema para recordar a largo plazo todo lo que estudias en el [[03 Plan para huir de DiSi]] · se aplica en cada día del [[04 Calendario dia por dia]] · técnicas explicadas en [[11 Clase 0.1 Datos]] · las tarjetas viven en cada nota: [[10 Teoria de CSharp]], [[11 Clase 0.1 Datos]], [[12 Clase Primer proyecto por CLI]], [[14 Evaluaciones]], [[15 Dudas resueltas]] · perfil en [[02 Contexto y perfil]] · Versión en PDF: [[13 Plan de memorizacion.pdf]]

# Plan de memorización a largo plazo

El objetivo no es pasar un examen la semana que viene. Es que en una entrevista de marzo de 2027, o en tu trabajo dentro de dos años, puedas explicar qué hace el CLR igual de claro que hoy. Este plan está hecho para eso.

## Por qué olvidamos y cómo evitarlo

En 1885 el psicólogo Hermann Ebbinghaus midió cuánto olvidamos con el tiempo. Lo que encontró se llama **curva del olvido**: sin repasar, en un día se pierde más de la mitad de lo aprendido y en una semana cerca de tres cuartas partes. Pero cada vez que **recuerdas algo justo cuando estabas por olvidarlo**, la curva se vuelve más plana y el siguiente olvido tarda más.

De ahí salen las tres reglas de este plan:

1. **Recordar, no releer.** Releer da la sensación de que ya lo sabes. Lo que fija la memoria es el esfuerzo de sacar la respuesta sin mirar.
2. **Espaciar.** Repasar poco y seguido, con intervalos cada vez más largos: 1 día, 3 días, 1 semana, 3 semanas, 2 meses, 4 meses.
3. **Entender antes de memorizar.** Una tarjeta que no entiendes se olvida aunque la repitas. Por eso cada concepto pasa primero por la escalera de comprensión.

## La escalera de comprensión

Un concepto no está "aprendido" hasta que llega al nivel 4. Cada concepto empieza en el 1.

| Nivel | Qué puedes hacer | Cómo lo compruebas |
| --- | --- | --- |
| 1. Recordar | Decir la definición | La tarjeta de repaso te sale sin mirar |
| 2. Explicar | Explicarlo con tus palabras y una analogía | 2 minutos en voz alta, sin trabarte (técnica Feynman) |
| 3. Aplicar | Usarlo o verlo en algo real | Lo comprobaste en tu máquina o en tu código |
| 4. Conectar | Relacionarlo con otros conceptos y con DiSí | Puedes contar la historia completa donde aparece |

Las calificaciones de [[14 Evaluaciones]] te dicen en qué nivel está cada concepto. Un 6 de 10 normalmente significa nivel 1: sabes la definición pero no todas sus partes.

## El sistema: tarjetas en Obsidian

### Instalación (una sola vez, 10 min)

1. En Obsidian: Configuración → Plugins de la comunidad → Explorar → busca **Spaced Repetition** (autor: st3v3nmw) → Instalar → Activar.
2. En la configuración del plugin, deja la etiqueta de tarjetas como `#flashcards`. Tus notas usan `#flashcards/fundamentos`, `#flashcards/csharp`, `#flashcards/errores` y `#flashcards/dudas`: el plugin las agrupa como mazos.
3. Para repasar: paleta de comandos → **Spaced Repetition: Review flashcards in all notes**.
4. Por cada tarjeta, piensa la respuesta **en voz alta** antes de voltearla y luego califícate con honestidad: **Hard** (no salió o salió a medias), **Good** (salió con esfuerzo), **Easy** (salió inmediato). El plugin calcula cuándo volver a mostrártela.

El plugin agrega a la nota un comentario con la fecha del siguiente repaso de cada tarjeta. Así se sincroniza solo entre tu PC y tu celular con Git.

### Cómo escribir tus propias tarjetas

Las mejores tarjetas son las que escribes tú. Reglas:

- **Una idea por tarjeta.** "¿Qué trae el SDK?" es buena. "Explica el SDK, el runtime y el CLR" son tres tarjetas.
- **Con tus palabras**, no copiadas de la nota.
- **Preguntas de "por qué"**, además de "qué": "¿Por qué el dinero va en `decimal`?" vale más que "¿Qué es `decimal`?".
- **Cada error se vuelve tarjeta.** Lo que fallaste en una evaluación es exactamente lo que más necesitas repasar.
- **Si una tarjeta te falla tres veces seguidas, no la repitas más: reescríbela** o divídela. El problema es la tarjeta o que falta entender algo.

Formato: `pregunta::respuesta`, una por línea, debajo de una etiqueta `#flashcards/…`.

## La rutina

### Cada día de estudio (5–10 min, al inicio de la sesión)

Las clases ya empiezan con un bloque de repaso. Úsalo así:
1. Abre el repaso del plugin y haz **todas las tarjetas que te toquen hoy**. Al principio serán pocas; con el tiempo, unas 15–25 por día.
2. Si una tarjeta te falla, no la estudies en ese momento: el plugin te la volverá a mostrar pronto.
3. Si el repaso te toma más de 10 minutos, se te acumularon tarjetas: no agregues tarjetas nuevas hasta ponerte al día.

### Cada domingo (dentro de los 15 min de revisión semanal)

1. Elige **2 conceptos al azar** de semanas anteriores y explícalos en voz alta 2 minutos cada uno. Grábate de vez en cuando.
2. Revisa en [[14 Evaluaciones]] tus conceptos débiles y comprueba si ya subieron de nivel.
3. Escribe tarjetas nuevas para lo que aprendiste en la semana y no tenga tarjeta todavía.

### Cada fin de mes: examen acumulado (30 min)

Al inicio de la sesión del último sábado del mes: **31 oct, 28 nov y 26 dic** (el del 26 dic coincide con el repaso final del plan).

1. Le pides a Claude un examen de 15–20 preguntas **mezcladas** de todo lo visto hasta ese día, sin decirle de qué tema empezar. Mezclar obliga a tu cerebro a elegir el concepto correcto, como en una entrevista.
2. Contestas sin mirar, por escrito o en voz alta.
3. Claude te califica y el resultado entra a [[14 Evaluaciones]]. Cada error se vuelve tarjeta de `#flashcards/errores`.

### Después del plan (desde enero de 2027)

- **10 minutos diarios de tarjetas**, aunque ya no estudies temas nuevos. Las tarjetas que ya dominas aparecerán cada varios meses; casi no cuesta tiempo.
- **Un examen acumulado al mes** hasta tener empleo nuevo. En la semana previa a cada entrevista, uno extra.

## Historia para recordar el recorrido completo

Los conceptos aislados se olvidan; una historia se recuerda. Esta une todo lo de la sección 1 de [[10 Teoria de CSharp]]. Léela, ciérrala y cuéntala tú con tus palabras.

**El viaje de Program.cs**

> Program.cs es una carta escrita en español (C#) que necesita llegar a una fábrica donde solo se habla un idioma de máquinas (código máquina).
>
> Primero pasa por la **oficina de traducción**, que es el **SDK**. Ahí el **jefe de obra, MSBuild**, lee la orden de trabajo (el `.csproj`) y llama a **Roslyn, el traductor**. Roslyn revisa la carta: si encuentra una frase sin sentido, como guardar texto en un `int`, la regresa y no traduce nada (**error de compilación**). Si todo está bien, la traduce a un **idioma universal**, el **IL**, y la mete en una **caja sellada**: el **ensamblado** `.dll`. La caja lleva una **etiqueta** (el **manifiesto**) con su nombre, versión y la lista de otras cajas que necesita, y un **inventario** de todo lo que contiene (los **metadatos**). En la tapa trae escrito **MZ**, como todas las cajas de Windows.
>
> Cuando alguien quiere usar la caja, llega primero la **recepcionista**, el **host** `dotnet.exe`. Lee la nota pegada (`runtimeconfig.json`), ve qué versión de fábrica necesita y llama al **gerente de la fábrica, el CLR**. El gerente prepara la **bodega** (el **heap**) y contrata al **personal de limpieza** (el **recolector de basura**). Abre la caja, busca la primera instrucción (`Main`) y, cada vez que se necesita una instrucción por primera vez, llama al **intérprete simultáneo, el JIT**, que la traduce al idioma exacto de las máquinas de esa fábrica (x64 o ARM64). Si algo explota (una **excepción**), el gerente busca quién se hace cargo; si nadie, cierra la fábrica e imprime el reporte de lo ocurrido (el **stack trace**).
>
> En DiSí, la fábrica está dentro de un edificio con **recepción propia**, **IIS**, que recibe a los clientes de internet y los manda al piso correcto (`w3wp.exe`), donde trabaja el gerente.

**Cómo usarla:** cuéntala completa en voz alta una vez por semana durante el primer mes. Si te trabas en una parte, esa es la que no entiendes todavía.

## Cómo medir si funciona

| Señal | Qué significa | Qué hacer |
| --- | --- | --- |
| Más del 85% de tarjetas en Good o Easy | El sistema funciona | Seguir igual |
| Muchas tarjetas en Hard | Estás memorizando sin entender | Volver a la nota y explicarla en voz alta antes de seguir |
| La misma tarjeta falla 3 veces | La tarjeta está mal hecha | Reescribirla o dividirla |
| El repaso diario pasa de 15 min | Agregas tarjetas más rápido de lo que las aprendes | Una semana sin tarjetas nuevas |
| Las calificaciones de [[14 Evaluaciones]] suben mes con mes | Retención a largo plazo | Ese es el objetivo |

## Cosas que parecen estudiar pero no sirven

- **Releer y subrayar.** Se siente productivo y casi no deja nada.
- **Estudiar todo un día antes.** Sirve para mañana, no para dentro de seis meses.
- **Ver videos sin pausar a explicarte lo que viste.**
- **Desvelarte.** La memoria se consolida mientras duermes; dormir poco borra parte de lo que estudiaste ese día.
