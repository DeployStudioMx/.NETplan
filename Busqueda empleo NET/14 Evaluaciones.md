---
tags: [busqueda-empleo, evaluaciones]
actualizado: 2026-10-19
---
> Registro de cada vez que Alex contesta preguntas de repaso o de entrevista y Claude lo califica · los conceptos débiles entran al [[13 Plan de memorizacion]] · dudas en [[15 Dudas resueltas]] · perfil en [[02 Contexto y perfil]] · avance en [[01 Bitacora]]

# Evaluaciones

Cada evaluación registra la calificación, lo que faltó y una tarjeta por cada error. Las tarjetas de errores se repasan con más frecuencia que las demás: son tus puntos débiles.

## Resumen

| Fecha | Tema | Calificación | Conceptos débiles |
| --- | --- | --- | --- |
| 2026-10-19 | [[10 Teoria de CSharp]], sección 2 (repaso) | **16 / 30 (5.3)** | Qué genera el compilador (no es `Program.cs`), qué hay en `obj`, por qué `bin` y `obj` no van a Git |
| 2026-10-13 | [[10 Teoria de CSharp]], sección 1 (repaso) | **55 / 80 (6.9)** | Código máquina por arquitectura, qué trae el SDK y qué va en producción, qué hace el host vs. el CLR, qué contiene una DLL nativa y el manifiesto |

---

## 2026-10-19 · Sección 2 de la teoría de C#

Primera lectura de la sección 2 (anatomía de un proyecto), antes del laboratorio.

### Respuestas de Alex (textuales)

1. genera el programa.cs y el método main
2. en bin está el programa en IL, un lanzador un json con la especificación de la versión a utilizar
3. en . Net framework se listan todos los archivos y en core no

### Calificación

| # | Pregunta | Calif. | Qué estuvo bien | Qué faltó o se corrige |
| --- | --- | --- | --- | --- |
| 1 | ¿Qué genera el compilador a partir de los top-level statements? | 5/10 | El método `Main` | **Corrección:** `Program.cs` no lo genera el compilador; lo crea la plantilla de `dotnet new console` y es tu código fuente. El compilador genera la **clase `Program`** y el método **`Main`** que envuelven tus líneas, y eso queda dentro del IL de la `.dll` |
| 2 | ¿Qué hay en `bin` y qué en `obj`? ¿Por qué no se suben a Git? | 4/10 | `bin`: la `.dll` con IL, el `.exe` lanzador y el `.runtimeconfig.json` con la versión del runtime | Faltó el `.pdb`. **No contestaste las otras dos partes:** `obj` tiene los archivos intermedios de la compilación (por ejemplo, `project.assets.json` con los paquetes resueltos); y no se suben a Git porque **se regeneran solos en cada build**: subirlos solo agrega peso y conflictos |
| 3 | ¿Qué cambia entre un `.csproj` de .NET Framework y uno de .NET 10? | 7/10 | En .NET Framework se listan todos los archivos y en el moderno no | Faltó decir por qué: el formato **estilo SDK** incluye automáticamente todos los `.cs` de la carpeta, así que el archivo queda en unas pocas líneas. Ojo con el nombre: desde .NET 5 ya no se llama "Core", sino **.NET** a secas |

**Total: 16 / 30 → 5.3 de 10.**

**Lo bueno:** el contenido de `bin` y la diferencia del `.csproj` los tienes claros.

**Patrón que se repite:** otra vez contestaste solo la primera parte de una pregunta compuesta. La pregunta 2 tenía tres partes (`bin`, `obj` y Git) y contestaste una. Es el mismo patrón de la evaluación del 13 oct ([[02 Contexto y perfil]]). Antes de responder, numera las partes de la pregunta en tu hoja.

### Tarjetas de los errores

#flashcards/csharp/s2-anatomia-proyecto/errores ¿Quién crea Program.cs?::La plantilla de dotnet new console; el compilador no lo genera
#flashcards/csharp/s2-anatomia-proyecto/errores ¿Qué genera el compilador a partir de los top-level statements?::La clase Program y el método Main, dentro del IL de la .dll
#flashcards/csharp/s2-anatomia-proyecto/errores ¿Qué hay en la carpeta obj?::Archivos intermedios de la compilación, como project.assets.json con los paquetes resueltos
#flashcards/csharp/s2-anatomia-proyecto/errores ¿Por qué bin y obj no se suben a Git?::Porque se regeneran en cada build; subirlos solo agrega peso y conflictos
#flashcards/csharp/s2-anatomia-proyecto/errores ¿Por qué el .csproj moderno es tan corto?::Es estilo SDK: incluye automáticamente todos los .cs de la carpeta
#flashcards/csharp/s2-anatomia-proyecto/errores ¿Cómo se llama hoy .NET Core?::Desde .NET 5, simplemente .NET

---

## 2026-10-13 · Sección 1 de la teoría de C#

Primera lectura, sin haber hecho todavía el laboratorio.

### Respuestas de Alex (textuales)

1. El codigo maquina es el lenguaje que utiliza el procesador de mi computadora para ejecutar instrucciones. es en bytes, binario.
2. compilar es traducir un programa de un lenguaje a otro revisando si existen errores sintacticos o semanticos. La diferencia es que una surge al momento de compilar (lo veo yo como desarrollador) y el otro es en tiempo de ejecución (lo ve el usuario que utiliza la aplicacion)
3. Compila en dos etapas porque primero lo traduce en intermediate lenguaje y despues el jit lo traduce a codigo maquina cuando se necesite en tiempo de ejecucion por el clr. gano compatibilidad y optimizacion y metadatos.
4. runtime es el codigo necesario o software para ejecutar una aplicacion de .net. en otro contexto es el tiempo de ejecucion de una aplicacion, que puedo interpretar como el momento en el que el programa corre.
5. el sdk trae ademas el software necesario para desarrollar aplicaciones y probarlas. trae librerias utiles y ademas un compilador para compilar el proytecto
6. un cli es una interfaz de comandos de texto que puede ejecutar metodos de un sdk o programa y vs no lo sustituye porque la interfaz grafica ejecuta al final las instrucciones en comandos de texto
7. el clr revisa el runtime a ejecutar, lo ejecuta, seguido del dll, mediante jit ejecuta lo que se mande a llamar, administra la memoria, expeciones e hilos
8. una dll nativa trae instrucciones directas del sistema operativo y uno de .net trae IL para ser ejecutado por un runtime de .net. un ensamblado contiene informacion de que aplicacion lo ejecuta, codigo il, metadatos, info de version y recursos.

### Calificación

| # | Pregunta | Calif. | Qué estuvo bien | Qué faltó o se corrige |
| --- | --- | --- | --- | --- |
| 1 | Código máquina y por qué x64 no corre en ARM64 | 6/10 | Son instrucciones del procesador, en bytes | **No contestaste la segunda parte:** cada familia de procesador tiene su propio código máquina; los mismos bytes significan otra cosa en ARM64 |
| 2 | Qué es compilar; error de compilación vs. de ejecución | 9/10 | Traducir revisando errores sintácticos y semánticos; cuándo aparece cada error | Falta "**antes** de ejecutar" y "el programa **completo**". El error de ejecución no solo lo ve el usuario: lo distingue el **momento** en que ocurre |
| 3 | Por qué dos etapas; qué ganas y qué pagas | 7/10 | IL, luego JIT dentro del CLR; ganas portabilidad, optimización y metadatos | **No dijiste qué pagas:** la primera llamada a cada método espera al JIT (arranque más lento). "Compatibilidad" se dice **portabilidad**: la misma `.dll` corre en cualquier sistema y procesador |
| 4 | Qué es un runtime; ejemplo fuera de .NET | 8/10 | Los dos sentidos, bien explicados | Faltó el ejemplo: la **JVM** de Java. Y qué lo forma en .NET: CLR + BCL + host |
| 5 | Qué trae el SDK; qué va en producción | 6/10 | Trae lo necesario para desarrollar y un compilador | Nombra las piezas: **Roslyn, MSBuild, plantillas, NuGet, la CLI y un runtime**. Las "librerías útiles" (la BCL) vienen en el runtime, no son lo que distingue al SDK. **No contestaste:** en producción se instala solo el runtime |
| 6 | Qué es una CLI; por qué Visual Studio no la reemplaza | 7/10 | Interfaz de comandos de texto; Visual Studio usa por debajo lo mismo | Una CLI ejecuta **comandos**, no "métodos" (método es otra cosa en C#). Faltó la razón más fuerte: **se puede automatizar** (servidores sin pantalla, GitHub Actions) y es igual en todos los sistemas |
| 7 | Qué hace el CLR al ejecutar | 6/10 | JIT de lo que se llama, memoria, excepciones, hilos | **Corrección:** el CLR no "revisa el runtime a ejecutar"; eso lo hace el **host** (`dotnet.exe`), que lee `runtimeconfig.json` y carga el CLR. Faltaron: cargar el ensamblado y buscar `Main`, preparar el **heap** y el **GC**, y la verificación de tipos |
| 8 | DLL nativa vs. ensamblado; qué contiene un ensamblado | 6/10 | IL, metadatos, versión, recursos; el ensamblado lo ejecuta el runtime | **Corrección:** una DLL nativa trae **código máquina para la CPU**, no "instrucciones del sistema operativo". El manifiesto no dice qué aplicación lo ejecuta: dice **su propia identidad** (nombre, versión, cultura, firma) y **de qué otros ensamblados depende**. Faltaron los encabezados PE y CLI |

**Total: 55 / 80 → 6.9 de 10.**

**Lo bueno:** entendiste la idea central de cada concepto en una sola lectura, y las respuestas 2 y 4 ya sirven para una entrevista.

**Patrón a corregir:** en 4 de 8 preguntas contestaste solo la primera parte. En una entrevista, contestar a medias se nota más que equivocarse. Antes de responder, cuenta cuántas cosas te están preguntando.

### Tarjetas de los errores


#flashcards/csharp/s1-plataforma-net/errores ¿Por qué un programa compilado para x64 no corre en ARM64?::Cada familia de procesador tiene su propio código máquina; los mismos bytes significan otra cosa
#flashcards/csharp/s1-plataforma-net/errores ¿Qué pagas por compilar en dos etapas (IL + JIT)?::Un arranque más lento: la primera llamada a cada método espera al JIT
#flashcards/csharp/s1-plataforma-net/errores ¿Cómo se llama la ventaja de que la misma .dll corra en cualquier sistema?::Portabilidad
#flashcards/csharp/s1-plataforma-net/errores ¿Qué piezas distinguen al SDK del runtime?::Roslyn, MSBuild, plantillas, cliente de NuGet y la CLI dotnet
#flashcards/csharp/s1-plataforma-net/errores ¿Qué se instala en un servidor de producción?::Solo el runtime (en IIS, el Hosting Bundle)
#flashcards/csharp/s1-plataforma-net/errores ¿Quién lee runtimeconfig.json y carga el CLR?::El host (dotnet.exe o el .exe lanzador), no el CLR
#flashcards/csharp/s1-plataforma-net/errores ¿Qué contiene una DLL nativa?::Código máquina para una CPU específica
#flashcards/csharp/s1-plataforma-net/errores ¿Qué dice el manifiesto de un ensamblado?::Su propia identidad (nombre, versión, cultura, firma) y de qué ensamblados depende
#flashcards/csharp/s1-plataforma-net/errores ¿Cuál es la mejor razón para usar la CLI aunque exista Visual Studio?::Se puede automatizar en servidores sin pantalla (CI) y es igual en todos los sistemas
