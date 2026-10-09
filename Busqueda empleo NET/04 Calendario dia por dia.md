---
tags: [busqueda-empleo, calendario]
actualizado: 2026-10-09
---
> Generado por calendario_render.py desde calendario_datos.py. No editar a mano: cambia los datos y vuelve a generar.
> Versión en PDF: [[04 Calendario dia por dia.pdf]] · Resumen semanal en [[03 Plan para huir de DiSi]] · Vista interactiva (artifact): https://claude.ai/artifact/737Dvitbv6Eds9XijvuBJA

# Calendario del plan .NET, día por día

Horario: lunes teoría (1.5 h) · martes a jueves código C# (1.5 h) · viernes búsqueda (1 h) · sábado teoría a fondo (4 h) · domingo repos de GitHub + revisión semanal (45 min). Total: unas 12 horas por semana (11 h 45 min).

## Semana 0 · Preparación

### Miércoles 30 sep · Preparación
**Hoy: plan listo**
- [ ] Plan de 12 semanas, árbol de fundamentos y clase de OAuth creados
- [ ] Bóveda de Obsidian configurada

### Jueves 1 oct · Preparación · 1 h
**Preparar la máquina**
- [ ] Instalar la última actualización de Windows y reiniciar
- [ ] Visual Studio Installer: actualizar Visual Studio 2026 y confirmar la carga de trabajo ASP.NET y desarrollo web
- [ ] En PowerShell: dotnet --list-sdks; debe aparecer 10.x
- [ ] Desactivar las sugerencias de Copilot en el editor mientras dure el plan

### Viernes 2 oct · Preparación · 1 h
**GitHub y glosario**
- [ ] Crear el repo público plan-dotnet en GitHub (ejercicios de las semanas 1 a 5, una carpeta por semana)
- [ ] git config --global user.name y user.email
- [ ] Clonar el repo en tu máquina
- [ ] Abrir [[08 Glosario]] en Obsidian y agregar el primer término con su formato: definición propia + ejemplo de DiSí

### Sábado 3 oct · Preparación · 2 h
**Diagnóstico sin IA**
- [ ] Leer "Cómo usar este plan" y hojear el árbol de fundamentos
- [ ] Sin IA ni internet: consola que pida un monto y un plazo e imprima una tabla de pagos iguales
- [ ] Anotar en la bitácora cada punto donde te trabaste: es tu línea base

### Domingo 4 oct · Descanso · 15 min
**Descanso**
- [ ] Sin estudio
- [ ] Revisar en el plan qué toca en la semana 1

## Semana 1 · 0.1 Datos · 0.2 Hardware | C#: tipos y métodos

### Lunes 5 oct · Teoría · 1.5 h
**0.1 Datos: bits y bases**
- [ ] Bit, byte y por qué un byte guarda 0 a 255
- [ ] Convertir a mano 5 números a binario: 5, 12, 100, 200, 255
- [ ] Hexadecimal: 0x0A, 0xFF, 0x1F4 a decimal
- [ ] Glosario: bit, byte, binario, hexadecimal

### Martes 6 oct · Código C# · 1.5 h
**Primer proyecto por CLI**
- [ ] Lectura (20 min): [[10 Teoria de CSharp]], secciones 1 a 3 (.NET, anatomía del proyecto, tipos)
- [ ] Dentro de plan-dotnet: dotnet new console -n Semana01 desde la terminal; abrir la carpeta en Visual Studio después
- [ ] Recorrer .csproj, Program.cs, carpetas bin y obj
- [ ] dotnet build y dotnet run
- [ ] Tipos: int, long, double, decimal, bool, char, string
- [ ] Imprimir int.MaxValue y provocar un desbordamiento con checked

### Miércoles 7 oct · Código C# · 1.5 h
**Control de flujo**
- [ ] Lectura (20 min): [[10 Teoria de CSharp]], secciones 4 y 5 (control de flujo, double vs. decimal)
- [ ] if/else, switch, operadores && || !
- [ ] for, while, foreach
- [ ] Ejercicio: tabla de pagos de un crédito con un ciclo
- [ ] Comparar 0.1 + 0.2 con double y con decimal; anotar por qué el dinero va en decimal

### Jueves 8 oct · Código C# · 1.5 h
**Métodos**
- [ ] Lectura (20 min): [[10 Teoria de CSharp]], secciones 6 y 7 (métodos, convenciones)
- [ ] Métodos con parámetros y valor de retorno
- [ ] Sobrecarga de métodos
- [ ] Ejercicio: decimal CalcularInteres(decimal monto, decimal tasaAnual, int meses)
- [ ] Commit y push de los 5 ejercicios
- **Entregable:** 5 ejercicios de consola en GitHub

### Viernes 9 oct · Búsqueda · 1 h
**Logros para el CV**
- [ ] Listar 10 logros de DiSí con números: montos, tiempos, clientes, errores evitados
- [ ] Uno por sistema: revolvente, cobranza, onboarding, originación, portal

### Sábado 10 oct · Teoría · 4 h
**0.1 Texto y 0.2 Hardware**
- [ ] ASCII, Unicode y UTF-8 (1 h)
- [ ] Experimento: guardar "Acción" en UTF-8 y abrirlo como Latin-1; explicar los símbolos raros
- [ ] CPU, núcleos, RAM, disco y jerarquía de velocidad (1 h)
- [ ] Dirección de memoria y qué es una referencia
- [ ] CS50x semana 0, video principal (1 h)
- [ ] Explicar en voz alta 2 min lo aprendido; glosario (1 h)

### Domingo 11 oct · Repos de GitHub · 45 min
**Anatomía de un repo**
- [ ] Pestañas Code, Issues, Pull requests, Actions, Releases
- [ ] Recorrer el README y las carpetas de dotnet/eShop
- [ ] Anotar 3 cosas que harías igual y 1 distinta
- [ ] Revisión semanal (15 min): casillas en [[04 Calendario dia por dia|04 Calendario]], avance en [[01 Bitacora]] y leer lo que toca el lunes

## Semana 2 · 0.3 SO · 0.4 Programas | C#: clases, valor vs. referencia

### Lunes 12 oct · Teoría · 1.5 h
**0.3 Procesos e hilos**
- [ ] Qué administra el sistema operativo
- [ ] Proceso vs. hilo
- [ ] Administrador de tareas > Detalles: identificar procesos y contar hilos de uno
- [ ] Stack vs. heap: dibujarlo en papel
- [ ] Glosario: proceso, hilo, stack, heap

### Martes 13 oct · Código C# · 1.5 h
**Clases y objetos**
- [ ] Clase, campos, propiedades, constructores
- [ ] Clase Cliente: Id, RazonSocial, Rfc
- [ ] Clase Credito: Monto, Tasa, Plazo, Cliente
- [ ] Crear y mostrar 3 objetos en Program.cs

### Miércoles 14 oct · Código C# · 1.5 h
**Valor vs. referencia**
- [ ] Copiar un struct y una class a otra variable, cambiar un campo y comparar
- [ ] Explicarlo con el dibujo de stack y heap del lunes
- [ ] string es inmutable: demostrarlo
- [ ] static vs. miembros de instancia

### Jueves 15 oct · Código C# · 1.5 h
**record y encapsulamiento**
- [ ] record y la igualdad por valor; with para copiar
- [ ] private set y validación en el constructor (monto > 0)
- [ ] README corto del modelo
- [ ] Commit y push
- **Entregable:** Modelo Cliente / Credito en GitHub

### Viernes 16 oct · Búsqueda · 1 h
**Borrador del CV**
- [ ] Redactar la experiencia en DiSí usando los 10 logros
- [ ] Formato: verbo + qué + resultado medible
- [ ] Sección de stack técnico honesta

### Sábado 17 oct · Teoría · 4 h
**0.3 SO y 0.4 Programas**
- [ ] Sistema de archivos y rutas absolutas y relativas (30 min)
- [ ] PowerShell: cd, ls, mkdir, $env:PATH (30 min)
- [ ] Sockets y puertos a nivel de SO (30 min)
- [ ] Compilado vs. interpretado; C# a IL a CLR con JIT; abrir tu .dll con ILSpy (1 h)
- [ ] Garbage collector (30 min)
- [ ] Estructuras de datos y Big O; lógica booleana (1 h)

### Domingo 18 oct · Repos de GitHub · 45 min
**Historial de commits**
- [ ] Leer 10 commits de ardalis/CleanArchitecture: mensaje, diff, archivos
- [ ] Probar Blame en un archivo
- [ ] Adoptar Conventional Commits en tu repo (feat:, fix:, docs:)
- [ ] Revisión semanal (15 min): casillas en [[04 Calendario dia por dia|04 Calendario]], avance en [[01 Bitacora]] y leer lo que toca el lunes

## Semana 3 · 1. Redes | C#: interfaces y colecciones

### Lunes 19 oct · Teoría · 1.5 h
**1. Redes: lo básico**
- [ ] Cliente/servidor, IP, DNS, puertos, localhost
- [ ] ipconfig: ubicar tu IP privada y tu gateway
- [ ] nslookup disioperaciones.com
- [ ] Glosario: IP, DNS, puerto, localhost

### Martes 20 oct · Código C# · 1.5 h
**Interfaces**
- [ ] Interfaz ICredito con CalcularPago() y SaldoPendiente
- [ ] Implementar CreditoSimple con tabla de amortización
- [ ] Probar desde Program.cs con 2 créditos distintos

### Miércoles 21 oct · Código C# · 1.5 h
**Herencia y polimorfismo**
- [ ] Implementar CreditoRevolvente: límite, disposición, pago, saldo disponible
- [ ] Clase abstracta vs. interfaz: escribir cuándo usarías cada una
- [ ] List<ICredito> con ambos tipos: polimorfismo

### Jueves 22 oct · Código C# · 1.5 h
**Colecciones y genéricos**
- [ ] List, Dictionary, HashSet: cuándo usar cada uno (Big O)
- [ ] Repositorio<T> genérico en memoria: Agregar, ObtenerPorId, Listar
- [ ] Commit y push
- **Entregable:** ICredito con CreditoSimple y CreditoRevolvente

### Viernes 23 oct · Búsqueda · 1 h
**LinkedIn**
- [ ] Titular, Acerca de y experiencia en español
- [ ] Versión corta en inglés
- [ ] Activar Open to Work solo para reclutadores

### Sábado 24 oct · Teoría · 4 h
**1. Redes a fondo**
- [ ] Capas TCP/IP y OSI; encapsulamiento (1 h)
- [ ] TCP vs. UDP y three-way handshake (30 min)
- [ ] MAC, IP pública/privada, subredes CIDR, router, NAT, DHCP (1 h)
- [ ] Resolución DNS completa y registros A, CNAME, MX, TXT (30 min)
- [ ] Correr tracert google.com y netstat -ano y explicar la salida (30 min)
- [ ] Contar en voz alta: qué pasa al escribir una URL, hasta TCP (30 min)

### Domingo 25 oct · Repos de GitHub · 45 min
**Soluciones .NET**
- [ ] Mapear .sln, .csproj, src/ y tests/ de jasontaylordev/CleanArchitecture
- [ ] Ubicar Directory.Build.props
- [ ] Contestar las 5 preguntas de cierre de la fase 1
- [ ] Revisión semanal (15 min): casillas en [[04 Calendario dia por dia|04 Calendario]], avance en [[01 Bitacora]] y leer lo que toca el lunes

## Semana 4 · 2. HTTP | C#: LINQ y excepciones

### Lunes 26 oct · Teoría · 1.5 h
**2. HTTP: la petición**
- [ ] Request / response
- [ ] Anatomía de una URL: esquema, host, puerto, ruta, query string, fragmento
- [ ] Métodos GET, POST, PUT, PATCH, DELETE
- [ ] Headers principales: Content-Type, Authorization, Accept

### Martes 27 oct · Código C# · 1.5 h
**LINQ I**
- [ ] Lista de 20 créditos de prueba
- [ ] Where, Select, OrderBy, First vs. FirstOrDefault
- [ ] Sintaxis de métodos vs. de consulta

### Miércoles 28 oct · Código C# · 1.5 h
**LINQ II**
- [ ] GroupBy por estatus, Sum y Count
- [ ] Join entre clientes y créditos
- [ ] Ejecución diferida: demostrar que la consulta corre dos veces; ToList()

### Jueves 29 oct · Código C# · 1.5 h
**Excepciones y nullable**
- [ ] try / catch / finally
- [ ] Excepción propia CreditoInvalidoException
- [ ] Activar <Nullable>enable</Nullable> y corregir advertencias
- [ ] Commit y push
- **Entregable:** Reporte de cartera con LINQ

### Viernes 30 oct · Búsqueda · 1 h
**Empresas objetivo**
- [ ] Lista de 20 empresas: fintech, banca, SOFOMes, consultoras .NET (30 min)
- [ ] 2 aplicaciones de práctica y registrarlas en [[09 Registro de aplicaciones]] (30 min)

### Sábado 31 oct · Teoría · 4 h
**2. HTTP a fondo**
- [ ] Body y content types: JSON y x-www-form-urlencoded (30 min)
- [ ] Códigos de estado: memorizar 200, 201, 204, 301, 302, 400, 401, 403, 404, 409, 429, 500 (1 h)
- [ ] Redirección 302 + Location (30 min)
- [ ] Stateless e idempotencia (30 min)
- [ ] F12 > Network en el portal de DiSí: analizar una petición completa (1 h)
- [ ] Hacer login y encontrar el Set-Cookie (30 min)

### Domingo 1 nov · Repos de GitHub · 45 min
**Issues y pull requests**
- [ ] Leer un PR cerrado de App-vNext/Polly de principio a fin
- [ ] Descripción, comentarios de revisión y checks de CI
- [ ] Revisión semanal (15 min): casillas en [[04 Calendario dia por dia|04 Calendario]], avance en [[01 Bitacora]] y leer lo que toca el lunes

## Semana 5 · 3. Navegador · 4. APIs | C#: async y HttpClient

### Lunes 2 nov · Teoría · 1.5 h
**3. Navegador**
- [ ] Cookies y atributos HttpOnly, Secure, SameSite
- [ ] Origen y Same-Origin Policy
- [ ] CORS: provocar un error de CORS y leer el mensaje en consola
- [ ] Glosario

### Martes 3 nov · Código C# · 1.5 h
**async / await**
- [ ] Task y async/await
- [ ] Por qué no usar .Result ni async void
- [ ] Ejercicio: 3 Task.Delay en secuencia vs. Task.WhenAll y medir el tiempo

### Miércoles 4 nov · Código C# · 1.5 h
**HttpClient**
- [ ] GET a https://api.github.com/users/<tu-usuario>
- [ ] Agregar el header User-Agent (sin él GitHub responde 403)
- [ ] Leer el código de estado y los headers de la respuesta

### Jueves 5 nov · Código C# · 1.5 h
**JSON y errores**
- [ ] Deserializar la respuesta a un record con System.Text.Json
- [ ] Manejar 404, timeout y CancellationToken
- [ ] Commit y push
- **Entregable:** Consola que consume una API y maneja errores

### Viernes 6 nov · Búsqueda · 1 h
**Aplicaciones**
- [ ] 3 aplicaciones de práctica
- [ ] Registrar cada una en [[09 Registro de aplicaciones]]
- [ ] Anotar preguntas técnicas que no supiste

### Sábado 7 nov · Teoría · 4 h
**3. Web y 4. APIs y REST**
- [ ] Front channel vs. back channel (30 min)
- [ ] CSRF y XSS; AntiForgeryToken en MVC (1 h)
- [ ] API, REST, recurso, endpoint, JSON, serialización (1 h)
- [ ] SDK, webhook, rate limit, OpenAPI y Swagger (30 min)
- [ ] Postman o curl contra una API pública: describir código, headers y JSON (1 h)

### Domingo 8 nov · Repos de GitHub · 45 min
**Seguir un flujo**
- [ ] Abrir dotnet/eShop en github.dev (tecla punto)
- [ ] Seguir un pedido desde el endpoint hasta la base de datos con Ir a definición
- [ ] Revisión semanal (15 min): casillas en [[04 Calendario dia por dia|04 Calendario]], avance en [[01 Bitacora]] y leer lo que toca el lunes

## Semana 6 · 5. Cripto · 6. HTTPS | ASP.NET Core: DI y middleware

### Lunes 9 nov · Teoría · 1.5 h
**5. Criptografía básica**
- [ ] Codificación vs. hash vs. HMAC vs. cifrado simétrico vs. asimétrico vs. firma
- [ ] Hacer la tabla de memoria sin mirar
- [ ] Frase clave: Base64 no es cifrado

### Martes 10 nov · Código C# · 1.5 h
**Hash y HMAC en C#**
- [ ] SHA-256 de un texto y su Base64URL
- [ ] Cambiar una letra y comparar los hashes
- [ ] HMAC-SHA256 con una llave
- [ ] RandomNumberGenerator para un code_verifier de 43 caracteres

### Miércoles 11 nov · Código C# · 1.5 h
**ASP.NET Core: arranque**
- [ ] dotnet new webapi -n SolicitudesApi en su propio repo de GitHub (tu proyecto de portafolio)
- [ ] Recorrer Program.cs; Kestrel y su puerto
- [ ] appsettings.json, IOptions y entornos (Development / Production)
- [ ] Tabla .NET Framework vs. .NET 10: empezarla

### Jueves 12 nov · Código C# · 1.5 h
**DI y middleware**
- [ ] Registrar un servicio como Singleton, Scoped y Transient y mostrar la diferencia con un Guid
- [ ] Middleware propio que mide el tiempo de respuesta
- [ ] Commit y push
- **Entregable:** API de solicitudes de crédito (inicio)

### Viernes 13 nov · Búsqueda · 1 h
**Aplicaciones**
- [ ] 3 a 5 aplicaciones de práctica
- [ ] Registrar en [[09 Registro de aplicaciones]]
- [ ] Repasar preguntas que no supiste

### Sábado 14 nov · Teoría · 4 h
**5. Cripto y 6. HTTPS**
- [ ] Hash de contraseñas: salt, bcrypt, PBKDF2 (45 min)
- [ ] Certificados, CA y JWKS (45 min)
- [ ] HTTPS, TLS y handshake (1 h)
- [ ] Cadena de confianza; certificado en IIS; man-in-the-middle; mTLS (1 h)
- [ ] Abrir el certificado de disioperaciones.com en el navegador y leer emisor y vigencia (30 min)

### Domingo 15 nov · Repos de GitHub · 45 min
**Qué hace bueno a un README**
- [ ] Comparar 3 READMEs de repos .NET
- [ ] Reescribir el README de tu API: qué es, cómo correrlo, arquitectura, decisiones
- [ ] Revisión semanal (15 min): casillas en [[04 Calendario dia por dia|04 Calendario]], avance en [[01 Bitacora]] y leer lo que toca el lunes

## Semana 7 · 7. Identidad y tokens | EF Core y SQL Server

### Lunes 16 nov · Teoría · 1.5 h
**Feriado: Revolución Mexicana**
**7. Identidad**
- [ ] Identidad y credencial
- [ ] AuthN vs. AuthZ
- [ ] MFA, RBAC y mínimo privilegio
- [ ] Glosario

### Martes 17 nov · Código C# · 1.5 h
**Controllers y DTOs**
- [ ] SolicitudesController con GET y POST
- [ ] DTOs vs. entidades
- [ ] Validación con DataAnnotations
- [ ] Devolver 201, 400 y 404 correctamente

### Miércoles 18 nov · Código C# · 1.5 h
**EF Core**
- [ ] Instalar paquetes de EF Core para SQL Server
- [ ] DbContext y cadena de conexión a LocalDB
- [ ] dotnet ef migrations add Inicial
- [ ] dotnet ef database update

### Jueves 19 nov · Código C# · 1.5 h
**Relaciones**
- [ ] Cliente 1 a N Solicitud
- [ ] Include vs. AsNoTracking; detectar un N+1
- [ ] Segunda migración
- [ ] Commit y push
- **Entregable:** API con persistencia real en SQL Server

### Viernes 20 nov · Búsqueda · 1 h
**Aplicaciones**
- [ ] 3 a 5 aplicaciones de práctica
- [ ] Registrar en [[09 Registro de aplicaciones]]

### Sábado 21 nov · Teoría · 4 h
**7. Sesiones y tokens**
- [ ] Sesión (stateful) vs. token (stateless) (45 min)
- [ ] Bearer token, expiración y revocación (45 min)
- [ ] JWT: decodificar uno en jwt.io y leer iss, sub, aud, exp (1 h)
- [ ] Delegación, federación y SSO (30 min)
- [ ] Terminar la tabla .NET Framework vs. .NET 10 (1 h)

### Domingo 22 nov · Repos de GitHub · 45 min
**Tu perfil de GitHub**
- [ ] Crear tu README de perfil (repo con tu mismo usuario)
- [ ] Fijar tus repos, agregar descripción y topics
- [ ] Releer el diagrama del flujo OAuth para el lunes
- [ ] Revisión semanal (15 min): casillas en [[04 Calendario dia por dia|04 Calendario]], avance en [[01 Bitacora]] y leer lo que toca el lunes

## Semana 8 · OAuth 2.0 | Proyecto Google Calendar

### Lunes 23 nov · Teoría · 1.5 h
**OAuth: conceptos**
- [ ] Clase de OAuth, secciones 1 a 4: problema, historia, roles, terminología
- [ ] Explicar los 4 roles con tu proyecto de Google Calendar

### Martes 24 nov · Código C# · 1.5 h
**Google Calendar: pasos 1 y 2**
- [ ] Google Cloud: proyecto, habilitar Calendar API
- [ ] Pantalla de consentimiento External + tu Gmail como usuario de prueba
- [ ] Credencial Desktop app y descargar credentials.json
- [ ] Repo GcalPlan: dotnet new console -n GcalPlan; paquetes Google.Apis.Calendar.v3 y Google.Apis.Auth
- [ ] .gitignore para credentials.json y la carpeta del token

### Miércoles 25 nov · Código C# · 1.5 h
**Paso 3: autenticación**
- [ ] GoogleWebAuthorizationBroker con el scope de calendario
- [ ] Guardar el token con FileDataStore
- [ ] Listar tus calendarios en consola
- [ ] Identificar en qué paso del flujo va cada línea

### Jueves 26 nov · Código C# · 1.5 h
**Paso 4: crear eventos**
- [ ] Crear el calendario "Plan .NET"
- [ ] Crear un evento de prueba con fecha y hora
- [ ] Provocar y manejar un 401 y un 403

### Viernes 27 nov · Búsqueda · 1 h
**Empresas objetivo**
- [ ] Primeras 2 a 3 aplicaciones a tus empresas objetivo
- [ ] Agregar el proyecto de Google Calendar al CV

### Sábado 28 nov · Teoría + código · 4 h
**OAuth a fondo + agendar el plan**
- [ ] Teoría (2 h): clase de OAuth, secciones 5 a 10: PKCE, grant types, alternativas, seguridad
- [ ] Código (2 h): cargar las 12 semanas desde un JSON y crear todos los eventos del plan con tu consola
- [ ] Commit y push
- **Entregable:** Tu plan agendado en Google Calendar por tu propio código

### Domingo 29 nov · Repos de GitHub · 45 min
**Leer un SDK**
- [ ] En googleapis/google-api-dotnet-client, encontrar dónde se implementa el flujo OAuth que usaste
- [ ] Contestar las preguntas de cierre de la fase 2
- [ ] Revisión semanal (15 min): casillas en [[04 Calendario dia por dia|04 Calendario]], avance en [[01 Bitacora]] y leer lo que toca el lunes

## Semana 9 · SQL Server | JWT y roles

### Lunes 30 nov · Teoría · 1.5 h
**SQL Server I**
- [ ] INNER JOIN vs. LEFT JOIN sobre tu base de solicitudes
- [ ] GROUP BY y HAVING
- [ ] Escribir 5 consultas

### Martes 1 dic · Código C# · 1.5 h
**JWT: emitir**
- [ ] Endpoint /auth/login que emite un JWT
- [ ] AddAuthentication().AddJwtBearer()
- [ ] Validar iss, aud, exp y la firma

### Miércoles 2 dic · Código C# · 1.5 h
**Autorización**
- [ ] [Authorize] y roles analista / admin
- [ ] Políticas de autorización
- [ ] Probar la diferencia entre 401 y 403

### Jueves 3 dic · Código C# · 1.5 h
**Errores y logs**
- [ ] ProblemDetails
- [ ] Middleware global de errores
- [ ] ILogger con logs estructurados
- [ ] Commit y push
- **Entregable:** API protegida por roles

### Viernes 4 dic · Búsqueda · 1 h
**Empresas objetivo**
- [ ] 2 a 3 aplicaciones objetivo
- [ ] Seguimiento de procesos abiertos

### Sábado 5 dic · Teoría · 4 h
**SQL Server a fondo**
- [ ] Índices clustered vs. non-clustered (1 h)
- [ ] Plan de ejecución (45 min)
- [ ] Transacciones y niveles de aislamiento (45 min)
- [ ] Stored procedures (30 min)
- [ ] 5 consultas más + diagnosticar una lenta antes y después de un índice (1 h)

### Domingo 6 dic · Repos de GitHub · 45 min
**GitHub Actions por dentro**
- [ ] Leer .github/workflows de un repo .NET
- [ ] Explicar cada paso: checkout, setup-dotnet, build, test
- [ ] Revisión semanal (15 min): casillas en [[04 Calendario dia por dia|04 Calendario]], avance en [[01 Bitacora]] y leer lo que toca el lunes

## Semana 10 · Resiliencia | Webhook de Twilio

### Lunes 7 dic · Teoría · 1.5 h
**Resiliencia**
- [ ] Timeouts y reintentos con backoff
- [ ] Idempotencia en la práctica
- [ ] Rate limiting y 429
- [ ] Cómo reintentan los proveedores de webhooks

### Martes 8 dic · Código C# · 1.5 h
**Cliente tipado**
- [ ] IHttpClientFactory
- [ ] Cliente tipado a la API SIE de Banxico (tipo de cambio; pedir token gratuito)
- [ ] Configurar la URL base y el token en appsettings

### Miércoles 9 dic · Código C# · 1.5 h
**Polly**
- [ ] Política de reintentos y timeout en el cliente
- [ ] Probar contra una URL que falla
- [ ] Registrar cada reintento en los logs

### Jueves 10 dic · Código C# · 1.5 h
**Webhook de Twilio**
- [ ] Cuenta de prueba de Twilio
- [ ] Endpoint que recibe el webhook
- [ ] Exponerlo con ngrok o dev tunnels
- [ ] Validar X-Twilio-Signature
- [ ] Guardar el mensaje con EF Core

### Viernes 11 dic · Búsqueda · 1 h
**Empresas objetivo**
- [ ] 2 a 3 aplicaciones objetivo
- [ ] Preparar entrevistas agendadas

### Sábado 12 dic · Teoría + código · 4 h
**Webhook terminado**
- [ ] Idempotencia: MessageSid único, ignorar duplicados (1.5 h)
- [ ] Responder 200 rápido y procesar después (1 h)
- [ ] README con arquitectura y decisiones (1.5 h)
- [ ] Commit y push
- **Entregable:** Webhook funcionando y documentado

### Domingo 13 dic · Repos de GitHub · 45 min
**Seguridad en código ajeno**
- [ ] En twilio/twilio-csharp, encontrar RequestValidator
- [ ] Compararlo con tu validación de firma del sábado
- [ ] Revisión semanal (15 min): casillas en [[04 Calendario dia por dia|04 Calendario]], avance en [[01 Bitacora]] y leer lo que toca el lunes

## Semana 11 · Git, Docker, Azure | Pruebas y CI

### Lunes 14 dic · Teoría · 1.5 h
**Git a fondo**
- [ ] Ramas, merge vs. rebase
- [ ] Provocar y resolver un conflicto en tu repo
- [ ] Abrir un pull request contra tu propia rama main

### Martes 15 dic · Código C# · 1.5 h
**Pruebas unitarias**
- [ ] Proyecto xUnit
- [ ] Pruebas del cálculo de crédito con Arrange-Act-Assert
- [ ] Mocks con Moq o NSubstitute

### Miércoles 16 dic · Código C# · 1.5 h
**Pruebas de integración**
- [ ] WebApplicationFactory
- [ ] Webhook: firma válida, firma inválida y duplicado

### Jueves 17 dic · Código C# · 1.5 h
**Docker**
- [ ] Dockerfile de la API
- [ ] docker compose con API + SQL Server
- [ ] Levantar todo con un solo docker compose up

### Viernes 18 dic · Búsqueda · 1 h
**Seguimiento**
- [ ] Seguimiento de procesos
- [ ] Negociación: 30k netos; confirmar bruto vs. neto y nómina vs. honorarios

### Sábado 19 dic · Teoría + código · 4 h
**Portafolio terminado**
- [ ] Teoría (2 h): imagen, contenedor y capas en Docker; Azure App Service y Azure SQL
- [ ] Código (2 h): GitHub Actions que corre las pruebas; README final
- [ ] Commit y push
- **Entregable:** Repo de portafolio terminado

### Domingo 20 dic · Repos de GitHub · 45 min
**Revisión como reclutador**
- [ ] Pedirle a Claude que revise tu repo con la tabla del plan
- [ ] Corregir lo que falte
- [ ] Revisión semanal (15 min): casillas en [[04 Calendario dia por dia|04 Calendario]], avance en [[01 Bitacora]] y leer lo que toca el lunes

## Semana 12 · Repaso | Simulacros y guion

### Lunes 21 dic · Teoría · 1.5 h
**Repaso niveles 0 a 3**
- [ ] Explicar en voz alta cada nivel
- [ ] Grabarte y escucharte
- [ ] Anotar los temas débiles

### Martes 22 dic · Código C# · 1.5 h
**Live coding**
- [ ] 45 min cronometrados, sin IA: CRUD de solicitudes con minimal API
- [ ] Después, revisión con IA de lo que hiciste

### Miércoles 23 dic · Código C# · 1.5 h
**Simulacro técnico 1**
- [ ] Entrevista simulada con Claude: C#, ASP.NET Core, HTTP
- [ ] Anotar respuestas débiles

### Jueves 24 dic · Búsqueda · 1 h
**Nochebuena: sesión ligera**
**Guion de proyectos**
- [ ] Guion STAR de 2 proyectos de DiSí: problema, flujo, decisión, error, resultado

### Viernes 25 dic · Descanso
**Feriado: Navidad**
**Navidad**
- [ ] Sin estudio

### Sábado 26 dic · Teoría + código · 4 h
**Repaso final**
- [ ] Repaso niveles 4 a 7 y OAuth (1.5 h)
- [ ] Simulacro técnico 2 con Claude (1.5 h)
- [ ] Guion STAR de los 3 proyectos restantes (1 h)

### Domingo 27 dic · Repos de GitHub · 1 h
**Presentar tu repo + cierre**
- [ ] Guion de 3 minutos para recorrer tu repo en pantalla compartida y grabarte
- [ ] Revisar el checklist de salida
- [ ] Actualizar la bitácora
- [ ] Plan de enero: segunda ola de aplicaciones
- **Entregable:** Checklist de salida completo
