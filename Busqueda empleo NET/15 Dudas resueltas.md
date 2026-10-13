---
tags: [busqueda-empleo, dudas]
actualizado: 2026-10-13
---
> Dudas de Alex que surgen fuera de una clase o en una nota que no se debe modificar. Cada una enlaza a la nota de la que salió · registro de dudas en [[02 Contexto y perfil]] · se repasan con el [[13 Plan de memorizacion]] · los errores de las evaluaciones están en [[14 Evaluaciones]]

# Dudas resueltas

Lo más reciente arriba. Las dudas de la sección 1 de la teoría (SDK, runtime, CLI, compilar, CLR, DLL) se respondieron directo en [[10 Teoria de CSharp]].

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

#flashcards/dudas

¿Qué es IIS?::El servidor web de Microsoft para Windows: recibe peticiones HTTP en un puerto y las entrega a la aplicación correcta
¿Qué es un servidor web?::Un programa que escucha en un puerto (80 o 443) y responde peticiones HTTP
¿Qué es un application pool de IIS?::Un grupo aislado de aplicaciones con su propio proceso de trabajo (w3wp.exe)
¿Qué es w3wp.exe?::El proceso de trabajo de IIS donde corre tu app y está cargado el CLR
¿Cuál es el servidor web interno de ASP.NET Core?::Kestrel
¿Qué guarda el stack?::Las llamadas a métodos y sus variables locales; se libera sola al terminar el método
¿Qué guarda el heap?::Los objetos que pueden vivir más que el método que los creó; los libera el GC
¿Qué es el heap administrado?::El heap controlado por el CLR: aparta espacio con new y lo libera el recolector de basura
En string nombre = "Alex", ¿dónde vive cada parte?::El texto en el heap; la variable en el stack, con la dirección (referencia) del texto
¿Qué es IntelliSense?::La ayuda de Visual Studio al escribir: lista de miembros, parámetros, información rápida y errores
¿Cómo sabe IntelliSense qué tiene una clase?::Roslyn lee los metadatos de las DLL que usa el proyecto
¿IntelliSense es IA?::No; lo que se apaga en el plan es Copilot e IntelliCode de línea completa
