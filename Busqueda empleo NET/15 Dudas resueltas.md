---
tags: [busqueda-empleo, dudas]
actualizado: 2026-10-19
---
> Dudas de Alex que surgen fuera de una clase o en una nota que no se debe modificar. Cada una enlaza a la nota de la que salió · registro de dudas en [[02 Contexto y perfil]] · se repasan con el [[13 Plan de memorizacion]] · los errores de las evaluaciones están en [[14 Evaluaciones]]

# Dudas resueltas

Lo más reciente arriba. Las dudas de la sección 1 de la teoría (SDK, runtime, CLI, compilar, CLR, DLL) se respondieron directo en [[10 Teoria de CSharp]].

---

## 2026-10-19 · Leyendo la sección 2 de [[10 Teoria de CSharp]]

### ¿`Program.cs` se genera al compilar?

**No.** `Program.cs` lo crea el comando `dotnet new console` a partir de una **plantilla**, antes de compilar nada. Es **tu código fuente**: un archivo de texto que tú escribes y modificas.

Lo que sí genera el compilador, y no ves como archivo, es lo que *envuelve* a ese código. El orden es:

1. `dotnet new console` crea `Program.cs` (texto) y `Semana01.csproj`.
2. Tú escribes tu código en `Program.cs`.
3. `dotnet build`: Roslyn lee `Program.cs` y produce `Semana01.dll`. Al traducirlo, **agrega por su cuenta** una clase llamada `Program` y un método `Main` alrededor de tus líneas. Eso queda en el IL dentro de la `.dll`, no en ningún archivo `.cs`.

### ¿Qué es un método?

Un **método** es un bloque de instrucciones **con nombre** que hace una tarea. Puede recibir datos (**parámetros**) y puede devolver un resultado.

**Analogía:** una receta con nombre. "PrepararCafé(tazas)" agrupa los pasos (calentar agua, moler, servir). Cuando alguien dice "prepara café para 3", no repite los pasos: **llama** a la receta por su nombre y le pasa el dato que necesita.

**Ejemplos que ya usas:**
- `Console.WriteLine("Hola")` es una llamada al método `WriteLine`, que recibe un texto y lo imprime.
- En tus apps MVC de DiSí, cada **acción** de un controlador es un método: `public ActionResult Index()` es el método `Index`, que devuelve la página.

Lo verás a fondo en la sección 6 de [[10 Teoria de CSharp]].

### ¿Qué es el método `Main` y qué es el punto de entrada?

Cuando un programa arranca, el CLR necesita saber **cuál es la primera instrucción** que debe ejecutar. Ese lugar se llama **punto de entrada** (*entry point*). En C# es un método con un nombre especial: **`Main`**, que en inglés significa "principal".

**Analogía:** un edificio tiene muchas oficinas (los métodos), pero todos entran por la **puerta principal**. `Main` es esa puerta: de ahí sale todo lo demás, porque `Main` llama a otros métodos, que llaman a otros.

Antes de C# 9 (2020), todo programa de consola tenía que escribirse así:

```csharp
class Program                        // una clase que contiene todo
{
    static void Main(string[] args)  // el punto de entrada
    {
        Console.WriteLine("Hello, World!");
    }
}
```

Con **top-level statements** escribes solo la línea de en medio, y el compilador agrega por ti la clase `Program` y el método `Main` que la envuelven. Por eso no los ves en tu `Program.cs`.

**En DiSí:** en tus apps web de .NET Framework no hay un `Main` visible. El programa que arranca es IIS (`w3wp.exe`), y tu código empieza a ejecutarse en `Global.asax`, en el método `Application_Start`. En ASP.NET Core sí vuelve a haber un `Program.cs` con punto de entrada (semana 6).

### ¿Qué es una solución y en qué se diferencia de un proyecto?

| | **Proyecto** (`.csproj`) | **Solución** (`.sln` o `.slnx`) |
| --- | --- | --- |
| Qué es | Una unidad de código que se compila a **un** ensamblado (`.dll` o `.exe`) | Un contenedor que **agrupa varios proyectos** |
| Qué produce al compilar | Su propia `.dll` | Nada propio: compila cada proyecto que contiene |
| Para qué sirve | Definir qué se compila y con qué paquetes | Abrir y compilar varios proyectos juntos en Visual Studio |

**Analogía:** cada proyecto es un **libro**; la solución es el **estante** donde los acomodas juntos. El estante no es un libro.

**Ejemplos:**
- En DiSí, al abrir el `.sln` en Visual Studio, el Explorador de soluciones muestra varios proyectos: el sitio web y quizá bibliotecas de acceso a datos o de pruebas. Cada uno tiene su `.csproj` y produce su propia `.dll`.
- En `plan-dotnet` tendrás una solución, `PlanDotnet.slnx`, con un proyecto por semana: `Semana01`, `Semana02`…

### ¿Qué son los "paquetes resueltos"?

Un **paquete NuGet** es una biblioteca hecha por otros que tu proyecto usa (sección 1.8). En el `.csproj` solo escribes **qué** paquete y **qué versión** quieres:

```xml
<PackageReference Include="Google.Apis.Calendar.v3" Version="1.68.0" />
```

**Resolver** es averiguar todo lo que hace falta para cumplir esa lista:
1. Qué versión exacta de cada paquete usar.
2. **De qué otros paquetes depende cada uno** (dependencias transitivas): `Google.Apis.Calendar.v3` necesita otros paquetes de Google, que a su vez necesitan otros.
3. Descargarlos a una carpeta de tu PC (`C:\Users\<tú>\.nuget\packages`).
4. Escribir el resultado completo en `obj/project.assets.json`.

A ese proceso se le llama **restore** (`dotnet restore`) y corre solo cada vez que haces `dotnet build`.

**Analogía:** tu receta dice "harina". Resolver es ir a la tienda, elegir la marca y el peso exactos, y además conseguir lo que esa harina necesita. La lista de compras completa y ya surtida es `project.assets.json`.

**En DiSí:** en .NET Framework esto se hacía con el archivo `packages.config` y una carpeta `packages` dentro de la solución. El .NET moderno lo simplificó con `PackageReference` en el `.csproj`.

### ¿Qué es el `.pdb`?

**PDB** significa *Program Database*: es el archivo de **símbolos de depuración**.

La `.dll` tiene tu código traducido a IL, pero **no** sabe en qué archivo ni en qué línea de tu código fuente estaba cada instrucción. El `.pdb` guarda esa correspondencia: "esta instrucción del IL viene de `Program.cs`, línea 12", además de los nombres de tus variables locales.

**Analogía:** la `.dll` es un libro traducido; el `.pdb` es el índice que dice "este párrafo corresponde a la página 12 del original".

**Para qué sirve:**
- **Depurar:** sin `.pdb`, Visual Studio no puede detenerse en tus puntos de interrupción (breakpoints) ni avanzar línea por línea.
- **Errores con número de línea:** cuando una excepción sale en pantalla o en un log, el *stack trace* dice `en Program.cs:línea 12` gracias al `.pdb`. Sin él, solo verías el nombre del método.

Para **ejecutar** el programa no hace falta. Aun así, suele publicarse junto con la `.dll` en producción, para que los errores en los logs digan en qué línea ocurrieron.

### Tarjetas de esta sesión

#flashcards/csharp/s2-anatomia-proyecto/dudas ¿Program.cs lo genera el compilador?::No; lo crea la plantilla de dotnet new console. Es tu código fuente; el compilador lo lee
#flashcards/csharp/s2-anatomia-proyecto/dudas ¿Qué agrega el compilador a los top-level statements?::La clase Program y el método Main que los envuelven, dentro del IL de la .dll
#flashcards/csharp/s2-anatomia-proyecto/dudas ¿Qué es un método?::Un bloque de instrucciones con nombre que hace una tarea; puede recibir parámetros y devolver un resultado
#flashcards/csharp/s2-anatomia-proyecto/dudas ¿Qué es el punto de entrada de un programa?::La primera instrucción que ejecuta el CLR al arrancar; en C# es el método Main
#flashcards/csharp/s2-anatomia-proyecto/dudas ¿Dónde empieza tu código en una app MVC de .NET Framework?::En Global.asax, en Application_Start; el proceso lo arranca IIS (w3wp.exe)
#flashcards/csharp/s2-anatomia-proyecto/dudas ¿Proyecto vs. solución?::El proyecto (.csproj) compila a una .dll; la solución (.sln/.slnx) agrupa varios proyectos y no produce nada propio
#flashcards/csharp/s2-anatomia-proyecto/dudas ¿Qué significa resolver paquetes?::Calcular versiones exactas y dependencias transitivas, descargarlas y escribir el resultado en obj/project.assets.json
#flashcards/csharp/s2-anatomia-proyecto/dudas ¿Qué es una dependencia transitiva?::Un paquete que necesita otro paquete que tú usas, aunque tú no lo pediste directamente
#flashcards/csharp/s2-anatomia-proyecto/dudas ¿Qué comando resuelve los paquetes?::dotnet restore; corre solo con dotnet build
#flashcards/csharp/s2-anatomia-proyecto/dudas ¿Qué guarda el .pdb?::La correspondencia entre el IL y tu código fuente (archivo, línea, variables locales)
#flashcards/csharp/s2-anatomia-proyecto/dudas ¿Para qué sirve el .pdb?::Para depurar con breakpoints y para que los stack traces muestren el número de línea

---

## 2026-10-13 · Leyendo la sección 1 de [[10 Teoria de CSharp]]

### ¿Qué es IIS?

**IIS** (*Internet Information Services*) es el **servidor web** de Microsoft para Windows.

**Primero, qué es un servidor web:** un programa que se queda "escuchando" en un puerto de la computadora (el 80 para HTTP, el 443 para HTTPS) y, cuando llega una petición desde un navegador u otra aplicación, se la entrega a la aplicación correcta y devuelve la respuesta. Puertos y HTTP los verás a fondo en las semanas 3 y 4.

**Analogía:** IIS es la recepción de un edificio de oficinas. Los visitantes (las peticiones) llegan a recepción; recepción revisa a qué oficina van (qué sitio o aplicación) y los manda ahí. Cada piso del edificio es un **grupo de aplicaciones** (*application pool*) con su propio personal, de modo que si un piso tiene un problema, los demás siguen trabajando.

**Qué pasa en DiSí cuando alguien abre una de tus apps:**
1. La petición llega al servidor Windows por el puerto 443.
2. IIS la recibe y revisa a qué sitio pertenece por el dominio o la ruta.
3. IIS se la pasa al **proceso de trabajo** `w3wp.exe` del grupo de aplicaciones de ese sitio. Dentro de ese proceso está cargado el CLR de .NET Framework con las DLL de tu app.
4. Tu código (un controlador de MVC) genera la respuesta, e IIS la devuelve al navegador.

Lo que configuras en el **Administrador de IIS** (sitios, enlaces, certificados, grupos de aplicaciones) y en el `web.config` es justo eso: a dónde va cada petición y con qué reglas.

**En .NET moderno** cambia un poco: cada aplicación trae su propio servidor web interno, llamado **Kestrel**. IIS puede seguir delante como recepción (le pasa las peticiones a Kestrel) o cargar la app dentro de su proceso. Lo verás en la semana 6.

### ¿Qué es el heap?

La memoria RAM que el sistema operativo le da a tu programa se organiza en zonas. Las dos que más importan en C# son:

| | **Stack** (pila) | **Heap** (montón) |
| --- | --- | --- |
| Para qué | Las llamadas a métodos y sus variables locales | Los objetos que pueden vivir más que el método que los creó |
| Cómo se ordena | Como una pila de platos: lo último que entra es lo primero que sale | Espacio grande, sin orden fijo, donde se aparta lugar donde haya |
| Cuándo se libera | Sola, en cuanto el método termina | Cuando ya nadie usa el objeto, el recolector de basura lo libera |
| Velocidad | Muy rápida | Más lenta: hay que buscar espacio y después limpiar |

**Analogía:** el stack son las notas adhesivas de tu escritorio: pegas una por cada tarea en curso y la tiras en cuanto terminas. El heap es una bodega con estantes: ahí guardas cajas que pueden necesitarse días después. El **recolector de basura** (GC) es el personal de limpieza que revisa periódicamente qué cajas ya nadie reclama y las saca.

**"Heap administrado"** significa que esa bodega la controla el CLR: tú solo dices `new` y el CLR aparta el espacio y después lo libera. Por eso en C# nunca liberas memoria a mano.

**Ejemplo:** en `string nombre = "Alex";`, el texto "Alex" vive en el heap y la variable `nombre`, en el stack, solo guarda la **dirección** donde está el texto. Esa dirección es una **referencia**: por eso `string` es un "tipo por referencia".

Lo verás a fondo el lunes 12 oct (0.3 Procesos e hilos: dibujar stack y heap en papel) y en la semana 2 de código (valor vs. referencia).

### ¿Qué es IntelliSense?

Es la ayuda de **Visual Studio** mientras escribes código:
- **Lista de miembros:** al escribir `Console.` te muestra todo lo que tiene `Console` (`WriteLine`, `ReadLine`…).
- **Información de parámetros:** al abrir el paréntesis te dice qué recibe el método y de qué tipo.
- **Información rápida:** al pasar el mouse sobre algo, te dice qué es.
- **Subrayado de errores:** la línea ondulada roja antes de compilar.

**Cómo funciona:** el compilador Roslyn analiza tu código mientras escribes y lee los **metadatos** de las DLL que tu proyecto usa. Por eso sabe que `Console` tiene `WriteLine`: lo leyó en los metadatos de `System.Console.dll`. Es uno de los beneficios de que un ensamblado "se describa a sí mismo" ([[10 Teoria de CSharp]], sección 1.7).

**Para el plan:** IntelliSense **sí se queda prendido**; no es IA, solo lee metadatos. Lo que se apaga es **Copilot** y también **IntelliCode** con completado de líneas enteras, que sí sugiere código con IA. En Visual Studio: Herramientas → Opciones → IntelliCode, y desactiva las sugerencias de línea completa.

### "Todavía no existe `Semana01.dll`"

Correcto. `Semana01.dll` se crea hasta que corres `dotnet build` en el laboratorio 1 de [[12 Clase Primer proyecto por CLI]]. Los puntos 4 y 5 de "Para comprobar en tu máquina" de la sección 1 son para **después** del laboratorio; los puntos 1 a 3 sí puedes hacerlos ya, porque solo necesitan el SDK instalado.

---

## Tarjetas de repaso


#flashcards/csharp/s1-plataforma-net/dudas ¿Qué es IIS?::El servidor web de Microsoft para Windows: recibe peticiones HTTP en un puerto y las entrega a la aplicación correcta
#flashcards/csharp/s1-plataforma-net/dudas ¿Qué es un servidor web?::Un programa que escucha en un puerto (80 o 443) y responde peticiones HTTP
#flashcards/csharp/s1-plataforma-net/dudas ¿Qué es un application pool de IIS?::Un grupo aislado de aplicaciones con su propio proceso de trabajo (w3wp.exe)
#flashcards/csharp/s1-plataforma-net/dudas ¿Qué es w3wp.exe?::El proceso de trabajo de IIS donde corre tu app y está cargado el CLR
#flashcards/csharp/s1-plataforma-net/dudas ¿Cuál es el servidor web interno de ASP.NET Core?::Kestrel
#flashcards/csharp/s1-plataforma-net/dudas ¿Qué guarda el stack?::Las llamadas a métodos y sus variables locales; se libera sola al terminar el método
#flashcards/csharp/s1-plataforma-net/dudas ¿Qué guarda el heap?::Los objetos que pueden vivir más que el método que los creó; los libera el GC
#flashcards/csharp/s1-plataforma-net/dudas ¿Qué es el heap administrado?::El heap controlado por el CLR: aparta espacio con new y lo libera el recolector de basura
#flashcards/csharp/s1-plataforma-net/dudas En string nombre = "Alex", ¿dónde vive cada parte?::El texto en el heap; la variable en el stack, con la dirección (referencia) del texto
#flashcards/csharp/s1-plataforma-net/dudas ¿Qué es IntelliSense?::La ayuda de Visual Studio al escribir: lista de miembros, parámetros, información rápida y errores
#flashcards/csharp/s1-plataforma-net/dudas ¿Cómo sabe IntelliSense qué tiene una clase?::Roslyn lee los metadatos de las DLL que usa el proyecto
#flashcards/csharp/s1-plataforma-net/dudas ¿IntelliSense es IA?::No; lo que se apaga en el plan es Copilot e IntelliCode de línea completa
