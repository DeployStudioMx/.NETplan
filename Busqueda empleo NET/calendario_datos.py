# Contenido día por día del plan de 12 semanas.
# tipo: prep | teoria | codigo | busqueda | descanso | mixto | pasado
# Cada entrada: (tipo, horas, titulo, [tareas], entregable, nota)

D = {}
def d(fecha, tipo, horas, titulo, tareas, entregable=None, nota=None):
    D[fecha] = (tipo, horas, titulo, tareas, entregable, nota)

DESC = ["Sin estudio: descansar también es parte del plan",
        "Revisión semanal (15 min): marcar las casillas de la semana en 04 Calendario, anotar avance y dudas en 01 Bitacora y leer lo que toca el lunes"]

# ---------- Semana 0: preparación ----------
for f in ["2026-09-28", "2026-09-29"]:
    d(f, "pasado", "", "", [])
d("2026-09-30", "prep", "", "Hoy: plan listo",
  ["Plan de 12 semanas, árbol de fundamentos y clase de OAuth creados",
   "Bóveda de Obsidian configurada"])
d("2026-10-01", "prep", "1 h", "Preparar la máquina",
  ["Instalar la última actualización de Windows y reiniciar",
   "Visual Studio Installer: actualizar Visual Studio 2026 y confirmar la carga de trabajo ASP.NET y desarrollo web",
   "En PowerShell: dotnet --list-sdks; debe aparecer 10.x",
   "Desactivar las sugerencias de Copilot en el editor mientras dure el plan"])
d("2026-10-02", "prep", "1 h", "GitHub y glosario",
  ["Crear el repo público plan-dotnet en GitHub (ejercicios de las semanas 1 a 5, una carpeta por semana)",
   "git config --global user.name y user.email",
   "Clonar el repo en tu máquina",
   "Abrir 08 Glosario en Obsidian y agregar el primer término con su formato: definición propia + ejemplo de DiSí"])
d("2026-10-03", "prep", "2 h", "Diagnóstico sin IA",
  ["Leer \"Cómo usar este plan\" y hojear el árbol de fundamentos",
   "Sin IA ni internet: consola que pida un monto y un plazo e imprima una tabla de pagos iguales",
   "Anotar en la bitácora cada punto donde te trabaste: es tu línea base"])
d("2026-10-04", "descanso", "15 min", "Descanso",
  ["Sin estudio", "Revisar en el plan qué toca en la semana 1"])

# ---------- Semana 1 ----------
d("2026-10-05", "teoria", "1.5 h", "0.1 Datos: bits y bases",
  ["Bit, byte y por qué un byte guarda 0 a 255",
   "Convertir a mano 5 números a binario: 5, 12, 100, 200, 255",
   "Hexadecimal: 0x0A, 0xFF, 0x1F4 a decimal",
   "Glosario: bit, byte, binario, hexadecimal"])
d("2026-10-06", "codigo", "1.5 h", "Primer proyecto por CLI",
  ["Dentro de plan-dotnet: dotnet new console -n Semana01 desde la terminal; abrir la carpeta en Visual Studio después",
   "Recorrer .csproj, Program.cs, carpetas bin y obj",
   "dotnet build y dotnet run",
   "Tipos: int, long, double, decimal, bool, char, string",
   "Imprimir int.MaxValue y provocar un desbordamiento con checked"])
d("2026-10-07", "codigo", "1.5 h", "Control de flujo",
  ["if/else, switch, operadores && || !",
   "for, while, foreach",
   "Ejercicio: tabla de pagos de un crédito con un ciclo",
   "Comparar 0.1 + 0.2 con double y con decimal; anotar por qué el dinero va en decimal"])
d("2026-10-08", "codigo", "1.5 h", "Métodos",
  ["Métodos con parámetros y valor de retorno",
   "Sobrecarga de métodos",
   "Ejercicio: decimal CalcularInteres(decimal monto, decimal tasaAnual, int meses)",
   "Commit y push de los 5 ejercicios"],
  "5 ejercicios de consola en GitHub")
d("2026-10-09", "busqueda", "1 h", "Logros para el CV",
  ["Listar 10 logros de DiSí con números: montos, tiempos, clientes, errores evitados",
   "Uno por sistema: revolvente, cobranza, onboarding, originación, portal"])
d("2026-10-10", "teoria", "4 h", "0.1 Texto y 0.2 Hardware",
  ["ASCII, Unicode y UTF-8 (1 h)",
   "Experimento: guardar \"Acción\" en UTF-8 y abrirlo como Latin-1; explicar los símbolos raros",
   "CPU, núcleos, RAM, disco y jerarquía de velocidad (1 h)",
   "Dirección de memoria y qué es una referencia",
   "CS50x semana 0, video principal (1 h)",
   "Explicar en voz alta 2 min lo aprendido; glosario (1 h)"])
d("2026-10-11", "descanso", "15 min", "Descanso", DESC)

# ---------- Semana 2 ----------
d("2026-10-12", "teoria", "1.5 h", "0.3 Procesos e hilos",
  ["Qué administra el sistema operativo",
   "Proceso vs. hilo",
   "Administrador de tareas > Detalles: identificar procesos y contar hilos de uno",
   "Stack vs. heap: dibujarlo en papel",
   "Glosario: proceso, hilo, stack, heap"])
d("2026-10-13", "codigo", "1.5 h", "Clases y objetos",
  ["Clase, campos, propiedades, constructores",
   "Clase Cliente: Id, RazonSocial, Rfc",
   "Clase Credito: Monto, Tasa, Plazo, Cliente",
   "Crear y mostrar 3 objetos en Program.cs"])
d("2026-10-14", "codigo", "1.5 h", "Valor vs. referencia",
  ["Copiar un struct y una class a otra variable, cambiar un campo y comparar",
   "Explicarlo con el dibujo de stack y heap del lunes",
   "string es inmutable: demostrarlo",
   "static vs. miembros de instancia"])
d("2026-10-15", "codigo", "1.5 h", "record y encapsulamiento",
  ["record y la igualdad por valor; with para copiar",
   "private set y validación en el constructor (monto > 0)",
   "README corto del modelo",
   "Commit y push"],
  "Modelo Cliente / Credito en GitHub")
d("2026-10-16", "busqueda", "1 h", "Borrador del CV",
  ["Redactar la experiencia en DiSí usando los 10 logros",
   "Formato: verbo + qué + resultado medible",
   "Sección de stack técnico honesta"])
d("2026-10-17", "teoria", "4 h", "0.3 SO y 0.4 Programas",
  ["Sistema de archivos y rutas absolutas y relativas (30 min)",
   "PowerShell: cd, ls, mkdir, $env:PATH (30 min)",
   "Sockets y puertos a nivel de SO (30 min)",
   "Compilado vs. interpretado; C# a IL a CLR con JIT; abrir tu .dll con ILSpy (1 h)",
   "Garbage collector (30 min)",
   "Estructuras de datos y Big O; lógica booleana (1 h)"])
d("2026-10-18", "descanso", "15 min", "Descanso", DESC)

# ---------- Semana 3 ----------
d("2026-10-19", "teoria", "1.5 h", "1. Redes: lo básico",
  ["Cliente/servidor, IP, DNS, puertos, localhost",
   "ipconfig: ubicar tu IP privada y tu gateway",
   "nslookup disioperaciones.com",
   "Glosario: IP, DNS, puerto, localhost"])
d("2026-10-20", "codigo", "1.5 h", "Interfaces",
  ["Interfaz ICredito con CalcularPago() y SaldoPendiente",
   "Implementar CreditoSimple con tabla de amortización",
   "Probar desde Program.cs con 2 créditos distintos"])
d("2026-10-21", "codigo", "1.5 h", "Herencia y polimorfismo",
  ["Implementar CreditoRevolvente: límite, disposición, pago, saldo disponible",
   "Clase abstracta vs. interfaz: escribir cuándo usarías cada una",
   "List<ICredito> con ambos tipos: polimorfismo"])
d("2026-10-22", "codigo", "1.5 h", "Colecciones y genéricos",
  ["List, Dictionary, HashSet: cuándo usar cada uno (Big O)",
   "Repositorio<T> genérico en memoria: Agregar, ObtenerPorId, Listar",
   "Commit y push"],
  "ICredito con CreditoSimple y CreditoRevolvente")
d("2026-10-23", "busqueda", "1 h", "LinkedIn",
  ["Titular, Acerca de y experiencia en español",
   "Versión corta en inglés",
   "Activar Open to Work solo para reclutadores"])
d("2026-10-24", "teoria", "4 h", "1. Redes a fondo",
  ["Capas TCP/IP y OSI; encapsulamiento (1 h)",
   "TCP vs. UDP y three-way handshake (30 min)",
   "MAC, IP pública/privada, subredes CIDR, router, NAT, DHCP (1 h)",
   "Resolución DNS completa y registros A, CNAME, MX, TXT (30 min)",
   "Correr tracert google.com y netstat -ano y explicar la salida (30 min)",
   "Contar en voz alta: qué pasa al escribir una URL, hasta TCP (30 min)"])
d("2026-10-25", "descanso", "30 min", "Cierre de fase 1",
  ["Contestar en voz alta las 5 preguntas de cierre de la fase 1",
   "Revisión semanal: casillas en 04 Calendario y avance en 01 Bitacora"])

# ---------- Semana 4 ----------
d("2026-10-26", "teoria", "1.5 h", "2. HTTP: la petición",
  ["Request / response",
   "Anatomía de una URL: esquema, host, puerto, ruta, query string, fragmento",
   "Métodos GET, POST, PUT, PATCH, DELETE",
   "Headers principales: Content-Type, Authorization, Accept"])
d("2026-10-27", "codigo", "1.5 h", "LINQ I",
  ["Lista de 20 créditos de prueba",
   "Where, Select, OrderBy, First vs. FirstOrDefault",
   "Sintaxis de métodos vs. de consulta"])
d("2026-10-28", "codigo", "1.5 h", "LINQ II",
  ["GroupBy por estatus, Sum y Count",
   "Join entre clientes y créditos",
   "Ejecución diferida: demostrar que la consulta corre dos veces; ToList()"])
d("2026-10-29", "codigo", "1.5 h", "Excepciones y nullable",
  ["try / catch / finally",
   "Excepción propia CreditoInvalidoException",
   "Activar <Nullable>enable</Nullable> y corregir advertencias",
   "Commit y push"],
  "Reporte de cartera con LINQ")
d("2026-10-30", "busqueda", "1 h", "Empresas objetivo",
  ["Lista de 20 empresas: fintech, banca, SOFOMes, consultoras .NET (30 min)",
   "2 aplicaciones de práctica y registrarlas en 09 Registro de aplicaciones (30 min)"])
d("2026-10-31", "teoria", "4 h", "2. HTTP a fondo",
  ["Body y content types: JSON y x-www-form-urlencoded (30 min)",
   "Códigos de estado: memorizar 200, 201, 204, 301, 302, 400, 401, 403, 404, 409, 429, 500 (1 h)",
   "Redirección 302 + Location (30 min)",
   "Stateless e idempotencia (30 min)",
   "F12 > Network en el portal de DiSí: analizar una petición completa (1 h)",
   "Hacer login y encontrar el Set-Cookie (30 min)"])
d("2026-11-01", "descanso", "15 min", "Descanso", DESC)

# ---------- Semana 5 ----------
d("2026-11-02", "teoria", "1.5 h", "3. Navegador",
  ["Cookies y atributos HttpOnly, Secure, SameSite",
   "Origen y Same-Origin Policy",
   "CORS: provocar un error de CORS y leer el mensaje en consola",
   "Glosario"])
d("2026-11-03", "codigo", "1.5 h", "async / await",
  ["Task y async/await",
   "Por qué no usar .Result ni async void",
   "Ejercicio: 3 Task.Delay en secuencia vs. Task.WhenAll y medir el tiempo"])
d("2026-11-04", "codigo", "1.5 h", "HttpClient",
  ["GET a https://api.github.com/users/<tu-usuario>",
   "Agregar el header User-Agent (sin él GitHub responde 403)",
   "Leer el código de estado y los headers de la respuesta"])
d("2026-11-05", "codigo", "1.5 h", "JSON y errores",
  ["Deserializar la respuesta a un record con System.Text.Json",
   "Manejar 404, timeout y CancellationToken",
   "Commit y push"],
  "Consola que consume una API y maneja errores")
d("2026-11-06", "busqueda", "1 h", "Aplicaciones",
  ["3 aplicaciones de práctica",
   "Registrar cada una en 09 Registro de aplicaciones",
   "Anotar preguntas técnicas que no supiste"])
d("2026-11-07", "teoria", "4 h", "3. Web y 4. APIs y REST",
  ["Front channel vs. back channel (30 min)",
   "CSRF y XSS; AntiForgeryToken en MVC (1 h)",
   "API, REST, recurso, endpoint, JSON, serialización (1 h)",
   "SDK, webhook, rate limit, OpenAPI y Swagger (30 min)",
   "Postman o curl contra una API pública: describir código, headers y JSON (1 h)"])
d("2026-11-08", "descanso", "15 min", "Descanso", DESC)

# ---------- Semana 6 ----------
d("2026-11-09", "teoria", "1.5 h", "5. Criptografía básica",
  ["Codificación vs. hash vs. HMAC vs. cifrado simétrico vs. asimétrico vs. firma",
   "Hacer la tabla de memoria sin mirar",
   "Frase clave: Base64 no es cifrado"])
d("2026-11-10", "codigo", "1.5 h", "Hash y HMAC en C#",
  ["SHA-256 de un texto y su Base64URL",
   "Cambiar una letra y comparar los hashes",
   "HMAC-SHA256 con una llave",
   "RandomNumberGenerator para un code_verifier de 43 caracteres"])
d("2026-11-11", "codigo", "1.5 h", "ASP.NET Core: arranque",
  ["dotnet new webapi -n SolicitudesApi en su propio repo de GitHub (tu proyecto de portafolio)",
   "Recorrer Program.cs; Kestrel y su puerto",
   "appsettings.json, IOptions y entornos (Development / Production)",
   "Tabla .NET Framework vs. .NET 10: empezarla"])
d("2026-11-12", "codigo", "1.5 h", "DI y middleware",
  ["Registrar un servicio como Singleton, Scoped y Transient y mostrar la diferencia con un Guid",
   "Middleware propio que mide el tiempo de respuesta",
   "Commit y push"],
  "API de solicitudes de crédito (inicio)")
d("2026-11-13", "busqueda", "1 h", "Aplicaciones",
  ["3 a 5 aplicaciones de práctica",
   "Registrar en 09 Registro de aplicaciones", "Repasar preguntas que no supiste"])
d("2026-11-14", "teoria", "4 h", "5. Cripto y 6. HTTPS",
  ["Hash de contraseñas: salt, bcrypt, PBKDF2 (45 min)",
   "Certificados, CA y JWKS (45 min)",
   "HTTPS, TLS y handshake (1 h)",
   "Cadena de confianza; certificado en IIS; man-in-the-middle; mTLS (1 h)",
   "Abrir el certificado de disioperaciones.com en el navegador y leer emisor y vigencia (30 min)"])
d("2026-11-15", "descanso", "15 min", "Descanso", DESC)

# ---------- Semana 7 ----------
d("2026-11-16", "teoria", "1.5 h", "7. Identidad",
  ["Identidad y credencial",
   "AuthN vs. AuthZ",
   "MFA, RBAC y mínimo privilegio",
   "Glosario"], nota="Feriado: Revolución Mexicana")
d("2026-11-17", "codigo", "1.5 h", "Controllers y DTOs",
  ["SolicitudesController con GET y POST",
   "DTOs vs. entidades",
   "Validación con DataAnnotations",
   "Devolver 201, 400 y 404 correctamente"])
d("2026-11-18", "codigo", "1.5 h", "EF Core",
  ["Instalar paquetes de EF Core para SQL Server",
   "DbContext y cadena de conexión a LocalDB",
   "dotnet ef migrations add Inicial",
   "dotnet ef database update"])
d("2026-11-19", "codigo", "1.5 h", "Relaciones",
  ["Cliente 1 a N Solicitud",
   "Include vs. AsNoTracking; detectar un N+1",
   "Segunda migración",
   "Commit y push"],
  "API con persistencia real en SQL Server")
d("2026-11-20", "busqueda", "1 h", "Aplicaciones",
  ["3 a 5 aplicaciones de práctica", "Registrar en 09 Registro de aplicaciones"])
d("2026-11-21", "teoria", "4 h", "7. Sesiones y tokens",
  ["Sesión (stateful) vs. token (stateless) (45 min)",
   "Bearer token, expiración y revocación (45 min)",
   "JWT: decodificar uno en jwt.io y leer iss, sub, aud, exp (1 h)",
   "Delegación, federación y SSO (30 min)",
   "Terminar la tabla .NET Framework vs. .NET 10 (1 h)"])
d("2026-11-22", "descanso", "30 min", "Descanso",
  ["Sin estudio", "Revisión semanal: casillas en 04 Calendario y avance en 01 Bitacora", "Releer el diagrama del flujo OAuth para el lunes"])

# ---------- Semana 8 ----------
d("2026-11-23", "teoria", "1.5 h", "OAuth: conceptos",
  ["Clase de OAuth, secciones 1 a 4: problema, historia, roles, terminología",
   "Explicar los 4 roles con tu proyecto de Google Calendar"])
d("2026-11-24", "codigo", "1.5 h", "Google Calendar: pasos 1 y 2",
  ["Google Cloud: proyecto, habilitar Calendar API",
   "Pantalla de consentimiento External + tu Gmail como usuario de prueba",
   "Credencial Desktop app y descargar credentials.json",
   "Repo GcalPlan: dotnet new console -n GcalPlan; paquetes Google.Apis.Calendar.v3 y Google.Apis.Auth",
   ".gitignore para credentials.json y la carpeta del token"])
d("2026-11-25", "codigo", "1.5 h", "Paso 3: autenticación",
  ["GoogleWebAuthorizationBroker con el scope de calendario",
   "Guardar el token con FileDataStore",
   "Listar tus calendarios en consola",
   "Identificar en qué paso del flujo va cada línea"])
d("2026-11-26", "codigo", "1.5 h", "Paso 4: crear eventos",
  ["Crear el calendario \"Plan .NET\"",
   "Crear un evento de prueba con fecha y hora",
   "Provocar y manejar un 401 y un 403"])
d("2026-11-27", "busqueda", "1 h", "Empresas objetivo",
  ["Primeras 2 a 3 aplicaciones a tus empresas objetivo",
   "Agregar el proyecto de Google Calendar al CV"])
d("2026-11-28", "mixto", "4 h", "OAuth a fondo + agendar el plan",
  ["Teoría (2 h): clase de OAuth, secciones 5 a 10: PKCE, grant types, alternativas, seguridad",
   "Código (2 h): cargar las 12 semanas desde un JSON y crear todos los eventos del plan con tu consola",
   "Commit y push"],
  "Tu plan agendado en Google Calendar por tu propio código")
d("2026-11-29", "descanso", "30 min", "Cierre de fase 2",
  ["Contestar las preguntas de cierre de la fase 2", "Revisión semanal: casillas en 04 Calendario y avance en 01 Bitacora"])

# ---------- Semana 9 ----------
d("2026-11-30", "teoria", "1.5 h", "SQL Server I",
  ["INNER JOIN vs. LEFT JOIN sobre tu base de solicitudes",
   "GROUP BY y HAVING",
   "Escribir 5 consultas"])
d("2026-12-01", "codigo", "1.5 h", "JWT: emitir",
  ["Endpoint /auth/login que emite un JWT",
   "AddAuthentication().AddJwtBearer()",
   "Validar iss, aud, exp y la firma"])
d("2026-12-02", "codigo", "1.5 h", "Autorización",
  ["[Authorize] y roles analista / admin",
   "Políticas de autorización",
   "Probar la diferencia entre 401 y 403"])
d("2026-12-03", "codigo", "1.5 h", "Errores y logs",
  ["ProblemDetails",
   "Middleware global de errores",
   "ILogger con logs estructurados",
   "Commit y push"],
  "API protegida por roles")
d("2026-12-04", "busqueda", "1 h", "Empresas objetivo",
  ["2 a 3 aplicaciones objetivo", "Seguimiento de procesos abiertos"])
d("2026-12-05", "teoria", "4 h", "SQL Server a fondo",
  ["Índices clustered vs. non-clustered (1 h)",
   "Plan de ejecución (45 min)",
   "Transacciones y niveles de aislamiento (45 min)",
   "Stored procedures (30 min)",
   "5 consultas más + diagnosticar una lenta antes y después de un índice (1 h)"])
d("2026-12-06", "descanso", "15 min", "Descanso", DESC)

# ---------- Semana 10 ----------
d("2026-12-07", "teoria", "1.5 h", "Resiliencia",
  ["Timeouts y reintentos con backoff",
   "Idempotencia en la práctica",
   "Rate limiting y 429",
   "Cómo reintentan los proveedores de webhooks"])
d("2026-12-08", "codigo", "1.5 h", "Cliente tipado",
  ["IHttpClientFactory",
   "Cliente tipado a la API SIE de Banxico (tipo de cambio; pedir token gratuito)",
   "Configurar la URL base y el token en appsettings"])
d("2026-12-09", "codigo", "1.5 h", "Polly",
  ["Política de reintentos y timeout en el cliente",
   "Probar contra una URL que falla",
   "Registrar cada reintento en los logs"])
d("2026-12-10", "codigo", "1.5 h", "Webhook de Twilio",
  ["Cuenta de prueba de Twilio",
   "Endpoint que recibe el webhook",
   "Exponerlo con ngrok o dev tunnels",
   "Validar X-Twilio-Signature",
   "Guardar el mensaje con EF Core"])
d("2026-12-11", "busqueda", "1 h", "Empresas objetivo",
  ["2 a 3 aplicaciones objetivo", "Preparar entrevistas agendadas"])
d("2026-12-12", "mixto", "4 h", "Webhook terminado",
  ["Idempotencia: MessageSid único, ignorar duplicados (1.5 h)",
   "Responder 200 rápido y procesar después (1 h)",
   "README con arquitectura y decisiones (1.5 h)",
   "Commit y push"],
  "Webhook funcionando y documentado")
d("2026-12-13", "descanso", "15 min", "Descanso", DESC)

# ---------- Semana 11 ----------
d("2026-12-14", "teoria", "1.5 h", "Git a fondo",
  ["Ramas, merge vs. rebase",
   "Provocar y resolver un conflicto en tu repo",
   "Abrir un pull request contra tu propia rama main"])
d("2026-12-15", "codigo", "1.5 h", "Pruebas unitarias",
  ["Proyecto xUnit",
   "Pruebas del cálculo de crédito con Arrange-Act-Assert",
   "Mocks con Moq o NSubstitute"])
d("2026-12-16", "codigo", "1.5 h", "Pruebas de integración",
  ["WebApplicationFactory",
   "Webhook: firma válida, firma inválida y duplicado"])
d("2026-12-17", "codigo", "1.5 h", "Docker",
  ["Dockerfile de la API",
   "docker compose con API + SQL Server",
   "Levantar todo con un solo docker compose up"])
d("2026-12-18", "busqueda", "1 h", "Seguimiento",
  ["Seguimiento de procesos",
   "Negociación: 30k netos; confirmar bruto vs. neto y nómina vs. honorarios"])
d("2026-12-19", "mixto", "4 h", "Portafolio terminado",
  ["Teoría (2 h): imagen, contenedor y capas en Docker; Azure App Service y Azure SQL",
   "Código (2 h): GitHub Actions que corre las pruebas; README final",
   "Commit y push"],
  "Repo de portafolio terminado")
d("2026-12-20", "descanso", "15 min", "Descanso", DESC)

# ---------- Semana 12 ----------
d("2026-12-21", "teoria", "1.5 h", "Repaso niveles 0 a 3",
  ["Explicar en voz alta cada nivel",
   "Grabarte y escucharte",
   "Anotar los temas débiles"])
d("2026-12-22", "codigo", "1.5 h", "Live coding",
  ["45 min cronometrados, sin IA: CRUD de solicitudes con minimal API",
   "Después, revisión con IA de lo que hiciste"])
d("2026-12-23", "codigo", "1.5 h", "Simulacro técnico 1",
  ["Entrevista simulada con Claude: C#, ASP.NET Core, HTTP",
   "Anotar respuestas débiles"])
d("2026-12-24", "busqueda", "1 h", "Guion de proyectos",
  ["Guion STAR de 2 proyectos de DiSí: problema, flujo, decisión, error, resultado"],
  nota="Nochebuena: sesión ligera")
d("2026-12-25", "descanso", "", "Navidad",
  ["Sin estudio"], nota="Feriado: Navidad")
d("2026-12-26", "mixto", "4 h", "Repaso final",
  ["Repaso niveles 4 a 7 y OAuth (1.5 h)",
   "Simulacro técnico 2 con Claude (1.5 h)",
   "Guion STAR de los 3 proyectos restantes (1 h)"])
d("2026-12-27", "descanso", "1 h", "Cierre del plan",
  ["Revisar el checklist de salida",
   "Actualizar la bitácora",
   "Plan de enero: segunda ola de aplicaciones"],
  "Checklist de salida completo")

SEMANAS = [
    ("2026-09-28", "Semana 0", "Preparación"),
    ("2026-10-05", "Semana 1", "0.1 Datos · 0.2 Hardware | C#: tipos y métodos"),
    ("2026-10-12", "Semana 2", "0.3 SO · 0.4 Programas | C#: clases, valor vs. referencia"),
    ("2026-10-19", "Semana 3", "1. Redes | C#: interfaces y colecciones"),
    ("2026-10-26", "Semana 4", "2. HTTP | C#: LINQ y excepciones"),
    ("2026-11-02", "Semana 5", "3. Navegador · 4. APIs | C#: async y HttpClient"),
    ("2026-11-09", "Semana 6", "5. Cripto · 6. HTTPS | ASP.NET Core: DI y middleware"),
    ("2026-11-16", "Semana 7", "7. Identidad y tokens | EF Core y SQL Server"),
    ("2026-11-23", "Semana 8", "OAuth 2.0 | Proyecto Google Calendar"),
    ("2026-11-30", "Semana 9", "SQL Server | JWT y roles"),
    ("2026-12-07", "Semana 10", "Resiliencia | Webhook de Twilio"),
    ("2026-12-14", "Semana 11", "Git, Docker, Azure | Pruebas y CI"),
    ("2026-12-21", "Semana 12", "Repaso | Simulacros y guion"),
]

# ---------- Carril de repositorios (domingos) ----------
REV = "Revisión semanal (15 min): casillas en 04 Calendario, avance en 01 Bitacora y leer lo que toca el lunes"
REPOS = {
 "2026-10-11": ("Anatomía de un repo", ["Pestañas Code, Issues, Pull requests, Actions, Releases", "Recorrer el README y las carpetas de dotnet/eShop", "Anotar 3 cosas que harías igual y 1 distinta"]),
 "2026-10-18": ("Historial de commits", ["Leer 10 commits de ardalis/CleanArchitecture: mensaje, diff, archivos", "Probar Blame en un archivo", "Adoptar Conventional Commits en tu repo (feat:, fix:, docs:)"]),
 "2026-10-25": ("Soluciones .NET", ["Mapear .sln, .csproj, src/ y tests/ de jasontaylordev/CleanArchitecture", "Ubicar Directory.Build.props", "Contestar las 5 preguntas de cierre de la fase 1"]),
 "2026-11-01": ("Issues y pull requests", ["Leer un PR cerrado de App-vNext/Polly de principio a fin", "Descripción, comentarios de revisión y checks de CI"]),
 "2026-11-08": ("Seguir un flujo", ["Abrir dotnet/eShop en github.dev (tecla punto)", "Seguir un pedido desde el endpoint hasta la base de datos con Ir a definición"]),
 "2026-11-15": ("Qué hace bueno a un README", ["Comparar 3 READMEs de repos .NET", "Reescribir el README de tu API: qué es, cómo correrlo, arquitectura, decisiones"]),
 "2026-11-22": ("Tu perfil de GitHub", ["Crear tu README de perfil (repo con tu mismo usuario)", "Fijar tus repos, agregar descripción y topics", "Releer el diagrama del flujo OAuth para el lunes"]),
 "2026-11-29": ("Leer un SDK", ["En googleapis/google-api-dotnet-client, encontrar dónde se implementa el flujo OAuth que usaste", "Contestar las preguntas de cierre de la fase 2"]),
 "2026-12-06": ("GitHub Actions por dentro", ["Leer .github/workflows de un repo .NET", "Explicar cada paso: checkout, setup-dotnet, build, test"]),
 "2026-12-13": ("Seguridad en código ajeno", ["En twilio/twilio-csharp, encontrar RequestValidator", "Compararlo con tu validación de firma del sábado"]),
 "2026-12-20": ("Revisión como reclutador", ["Pedirle a Claude que revise tu repo con la tabla del plan", "Corregir lo que falte"]),
}
for f,(t,tareas) in REPOS.items():
    D[f] = ("repos", "45 min", t, tareas + [REV], None, None)
D["2026-12-27"] = ("repos", "1 h", "Presentar tu repo + cierre", ["Guion de 3 minutos para recorrer tu repo en pantalla compartida y grabarte", "Revisar el checklist de salida", "Actualizar la bitácora", "Plan de enero: segunda ola de aplicaciones"], "Checklist de salida completo", None)
