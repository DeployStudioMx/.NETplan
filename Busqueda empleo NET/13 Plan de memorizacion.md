---
tags: [busqueda-empleo, aprendizaje, memoria]
actualizado: 2026-10-15
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

### Paso 1. Instalar el plugin (5 min, en la PC y en el celular)

1. En Obsidian: **Configuración → Plugins de la comunidad**. Si dice "Modo restringido", desactívalo.
2. **Explorar** → busca **Spaced Repetition** (autor: Stephen Mwangi, versión 1.15 o mayor) → **Instalar** → **Activar**.
3. Repite lo mismo en el celular. La configuración de los plugins no viaja por Git (la carpeta `.obsidian/` está excluida a propósito), así que cada dispositivo se configura una vez.

### Paso 2. Configurar (5 min, en cada dispositivo)

Configuración → Spaced Repetition. Solo cambia lo que dice **Cambiar**; lo demás déjalo como viene. Si tu Obsidian está en español, el plugin también lo estará: te pongo los dos nombres.

| Opción (inglés / español) | Valor | Por qué |
| --- | --- | --- |
| Flashcard tags / Etiquetas de las tarjetas de memorización | `#flashcards` | Ya viene así. Encuentra todas tus notas con `#flashcards/…` |
| Convert folders to decks / ¿Convertir directorios a mazos? | Desactivado | Ya viene así. Los mazos salen de las etiquetas, no de carpetas |
| **Convert ==highlights== to clozes / ¿Convertir ==resaltados== a deletreo de huecos?** | **Cambiar: desactivado** | Si queda activo, cualquier texto entre `==` se vuelve tarjeta. En la teoría hay una tabla con el operador `==` de C# que crearía una tarjeta falsa |
| Convert \*\*bolded text\*\* to clozes / ¿Convertir texto en negrita…? | Desactivado | Ya viene así. Tus notas usan muchas negritas; si se activa, cada una sería una tarjeta |
| Separator for inline flashcards / Separador de tarjetas en línea | `::` | Ya viene así. Es el formato de todas tus tarjetas |
| Algorithm / Algoritmo | **SM-2-OSR** | Ya viene así. Es el algoritmo clásico de repetición espaciada (el de Anki), probado por años. El plugin también ofrece **FSRS**, más moderno, pero el propio plugin advierte que todavía está poco probado y puede perder datos al cambiar: **no lo actives** |
| **Save scheduling comment on the same line / ¿Guardar el comentario de programación en la última línea?** | **Cambiar: activado** | Así la fecha de repaso queda al final de la misma línea de la tarjeta: cada tarjeta sigue ocupando una sola línea y las notas se ven más limpias |
| Show context in cards | Activado | Ya viene así. Muestra de qué nota y sección sale la tarjeta |
| Show interval in review buttons | Activado | Ya viene así. Ves en cuántos días volverá la tarjeta según el botón que elijas |
| Status bar | Activado | Ya viene así. Abajo a la derecha verás cuántas tarjetas te tocan hoy |

### Paso 3. Comprobar que lee tus tarjetas (2 min)

Abre la paleta de comandos → **Spaced Repetition: Review flashcards from all notes** (en español: **Revisar tarjetas de todas las notas**). Debe aparecer este árbol de mazos:

| Mazo | Nota de origen | Tarjetas |
| --- | --- | --- |
| `flashcards/csharp` | [[10 Teoria de CSharp]] (17) y [[12 Clase Primer proyecto por CLI]] (11) | 28 |
| `flashcards/dudas` | [[15 Dudas resueltas]] | 12 |
| `flashcards/errores` | [[14 Evaluaciones]] | 9 |
| `flashcards/fundamentos` | [[11 Clase 0.1 Datos]] | 17 |
| **Total** | | **66** |

Si los números no coinciden, avísame con una captura antes de repasar.

### Los mazos

Cada nota con tarjetas lleva **una sola** etiqueta de mazo, en su propia línea, justo antes de sus tarjetas. Los mazos son por área, no por fecha:

| Etiqueta | Qué va ahí |
| --- | --- |
| `#flashcards/fundamentos` | Árbol de fundamentos: datos, hardware, sistema operativo, redes, HTTP, criptografía… |
| `#flashcards/csharp` | Lenguaje C# y plataforma .NET |
| `#flashcards/errores` | Lo que fallaste en [[14 Evaluaciones]]. Es el mazo más importante |
| `#flashcards/dudas` | Lo que preguntaste fuera de clase ([[15 Dudas resueltas]]) |

Cuando lleguen temas nuevos (ASP.NET Core, SQL, OAuth) se agrega un mazo por área, por ejemplo `#flashcards/aspnet`, y se registra en esta tabla.

### Cómo repasar

1. Paleta de comandos → **Review flashcards from all notes** (**Revisar tarjetas de todas las notas**), o el ícono de tarjetas en la barra lateral.
2. Lee la pregunta y **contesta en voz alta, completa**, antes de mostrar la respuesta. Si la pregunta tiene dos partes, contesta las dos.
3. Muestra la respuesta y califícate con honestidad:

| Botón | Cuándo usarlo |
| --- | --- |
| **Again** | No salió, o salió mal. La vuelve a mostrar en la misma sesión |
| **Hard / Difícil** | Salió incompleta o te costó mucho |
| **Good / Bien** | Salió completa, con algo de esfuerzo. Debe ser tu respuesta más común |
| **Easy / Fácil** | Salió completa e inmediata |

4. Al calificar, el plugin escribe al final de la línea de la tarjeta un comentario invisible como `<!--SR:!2026-10-18,3,250-->`: fecha del siguiente repaso, intervalo en días y facilidad. **No lo borres:** es la memoria del plugin.

### El repaso y Git (importante)

Como las fechas de repaso se guardan **dentro de las notas**, si repasas en el celular y en la PC el mismo día sin sincronizar, Git puede marcar un conflicto. Para evitarlo:

1. **Antes de repasar:** paleta de comandos → **Git: Pull**.
2. **Repasa en un solo dispositivo por día.**
3. **Al terminar:** paleta de comandos → **Git: Commit-and-sync**.

Si aun así aparece un conflicto, no lo resuelvas a mano: avísame y lo arreglo desde el repositorio.

### Primer repaso (hoy, 15 min)

Las 66 tarjetas son nuevas, así que el primer día te las mostrará todas. Después de hoy, cada día verás solo las que te toquen.

1. Haz `Git: Pull`.
2. Empieza por el mazo **errores**, luego **dudas**, **fundamentos** y **csharp**.
3. Si una respuesta no la entiendes (no solo que no la recuerdes), márcala **Again** y anótala para preguntarme.
4. Termina con `Git: Commit-and-sync`.

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
| Más del 85% de tarjetas en Good o Easy (Bien o Fácil) | El sistema funciona | Seguir igual |
| Muchas tarjetas en Again o Hard | Estás memorizando sin entender | Volver a la nota y explicarla en voz alta antes de seguir |
| La misma tarjeta falla 3 veces | La tarjeta está mal hecha | Reescribirla o dividirla |
| El repaso diario pasa de 15 min | Agregas tarjetas más rápido de lo que las aprendes | Una semana sin tarjetas nuevas |
| Las calificaciones de [[14 Evaluaciones]] suben mes con mes | Retención a largo plazo | Ese es el objetivo |

## Cosas que parecen estudiar pero no sirven

- **Releer y subrayar.** Se siente productivo y casi no deja nada.
- **Estudiar todo un día antes.** Sirve para mañana, no para dentro de seis meses.
- **Ver videos sin pausar a explicarte lo que viste.**
- **Desvelarte.** La memoria se consolida mientras duermes; dormir poco borra parte de lo que estudiaste ese día.
