// Genera "17 CV.docx" a partir del texto vigente de 17 CV.md (copiado a mano aquí). Uso: node cv_docx.js; requiere el paquete npm "docx". Después: exportar a PDF desde Word, o con LibreOffice: soffice --headless --convert-to pdf "17 CV.docx".
const fs=require('fs');
const {Document,Packer,Paragraph,TextRun,AlignmentType,LevelFormat,BorderStyle,TabStopType}=require('docx');
const F="Calibri", INK="1F2328", ACC="1F4E79", MUT="555555";
const r=(t,o={})=>new TextRun({text:t,font:F,size:o.size||20,bold:o.bold,color:o.color||INK,italics:o.italics});
const P=(runs,o={})=>new Paragraph({children:runs,spacing:{before:o.before||0,after:o.after??60,line:o.line||264},alignment:o.align,keepNext:o.keepNext,tabStops:o.tabs});
const H=(t)=>new Paragraph({children:[r(t.toUpperCase(),{bold:true,size:21,color:ACC})],spacing:{before:200,after:80},keepNext:true,border:{bottom:{style:BorderStyle.SINGLE,size:6,color:ACC,space:2}}});
const B=(label,rest)=>new Paragraph({children:[r(label,{bold:true}),r(rest)],numbering:{reference:"b",level:0},spacing:{after:70,line:264}});
const Bt=(runs)=>new Paragraph({children:runs,numbering:{reference:"b",level:0},spacing:{after:50,line:264}});
const job=(title,company,dates)=>P([r(title,{bold:true,size:21}),r("  ·  "+company,{size:21}),new TextRun({text:"\t"+dates,font:F,size:20,color:MUT})],{tabs:[{type:TabStopType.RIGHT,position:10080}],keepNext:true,after:40,before:60});
const children=[
 P([r("ALEXIS ORTEGA",{bold:true,size:36})],{after:20}),
 P([r("Desarrollador .NET Full Stack · Fintech",{bold:true,size:24,color:ACC})],{after:20}),
 P([r("C# · ASP.NET MVC · Oracle PL/SQL · APIs REST · IA aplicada",{size:20,color:MUT})],{after:60}),
 P([r("Ciudad de México  ·  55 1402 2249  ·  a.ortega8897@gmail.com  ·  linkedin.com/in/alexisoc8",{size:19})],{after:60}),
 H("Resumen"),
 P([r("Desarrollador .NET Full Stack con más de 3 años de experiencia. Soy el desarrollador principal de la plataforma de crédito empresarial de una SOFOM (factoraje, crédito simple y crédito revolvente para PyMEs): construí el ciclo completo del crédito, del onboarding digital a la cobranza, en C#, ASP.NET MVC y Oracle PL/SQL. Integré más de 15 servicios externos (WhatsApp Cloud API, Twilio, SAT, Círculo de Crédito, Mifiel, Ekatena, Google Maps) y llevé a producción IA para la lectura automática de documentos. Ascendido de Junior a Mid en 2026.")],{after:40}),
 H("Experiencia"),
 job("Desarrollador .NET Full Stack","DiSí Operaciones Empresariales (SOFOM, crédito a PyMEs)","Abr 2024 – actual"),
 P([r("Ingresé como Junior y fui ascendido a Mid en 2026.",{italics:true,color:MUT,size:19})],{after:60}),
 B("Onboarding digital: ","diseñé y desarrollé cuatro generaciones del alta de clientes, hasta pasar de un formulario de más de 600 campos a un expediente donde el cliente solo sube documentos y la IA (Claude Vision) extrae los datos. El frontend quedó 4 veces más ligero y las mejoras se decidieron con mapas de calor (Microsoft Clarity)."),
 B("Originación y dictamen de crédito: ","automaticé el dictamen con unos 20 módulos de análisis de riesgo y 88 criterios de scoring, análisis fiscal del SAT vía Ekatena (webhook y procesamiento en paralelo), geovalidación con Google Maps y Street View, y el dictamen ejecutivo de unas 34 láminas en PDF con un clic. El armado de un dictamen bajó de 2 a 3 días a unas horas (estimado)."),
 B("Crédito revolvente: ","construí el producto de punta a punta: paquete Oracle PL/SQL de unos 22 procedimientos con devengo diario de intereses y prelación de pagos, 17 pantallas de operación interna, portal del cliente y estados de cuenta."),
 B("Canal de WhatsApp: ","diseñé y construí solo el canal sobre la WhatsApp Cloud API de Meta, con dos productos en producción: onboarding por chat y un bot para operar la línea de crédito (10 flujos, 3 productos). Comparte las reglas de negocio con el portal web, y una auditoría automatizada de más de 2,000 verificaciones comprueba que ambos canales den los mismos resultados."),
 B("Cobranza: ","desarrollé un motor de reglas en PL/SQL con un job diario (8 programas por etapa de mora, calendario de 17 semanas) que agenda llamadas, correos, WhatsApp y visitas. Llamadas desde el navegador con Twilio Voice (grabación y detección de buzón), visitas de campo enviadas a Kobra por API y verificación domiciliaria virtual con cámara, video y GPS del celular."),
 B("Portal del cliente: ","desarrollé la app web móvil de autoservicio (unos 170 endpoints y más de 100 procedimientos): disposición de factoraje con validación de CFDI ante el SAT y firma con e.firma (FIEL), crédito simple y revolvente, pagos y estados de cuenta."),
 B("Contratos: ","automaticé el paquete legal (contrato, pagaré y anexos) con autollenado de unos 56 campos, extracción con IA de escrituras e identificaciones, y firma electrónica con FIEL vía Mifiel para varios firmantes. El armado pasó de horas a minutos por crédito (estimado)."),
 B("Estados de cuenta y cumplimiento: ","construí los estados de cuenta a cualquier fecha de corte para los tres productos y la certificación contable de intereses; diagnostiqué y corregí dos errores de cálculo en Oracle (43 de 43 créditos revisados cuadran contra cartera). Integré la consulta a Círculo de Crédito de avales con autorización por NIP y firma digital de peticiones."),
 job("Desarrollador .NET","Probiomed (empresa biofarmacéutica)","Ene 2023 – Ene 2024"),
 H("Habilidades técnicas"),
 Bt([r("Back end: ",{bold:true}),r("C#, .NET Framework 4.8, ASP.NET MVC 5, ASP.NET Web API 2, Entity Framework 6, ADO.NET, LINQ, async/await, SignalR")]),
 Bt([r("Bases de datos: ",{bold:true}),r("Oracle (PL/SQL, paquetes, jobs programados), SQL Server (T-SQL, stored procedures)")]),
 Bt([r("Front end: ",{bold:true}),r("JavaScript (ES6+), jQuery, Razor, HTML5, CSS3 (mobile first), Bootstrap, Chart.js")]),
 Bt([r("Integraciones: ",{bold:true}),r("APIs REST, webhooks, OAuth2, WhatsApp Cloud API, Twilio (Voice, Verify), SAT (CFDI, e.firma), Círculo de Crédito, Mifiel, Google Maps")]),
 Bt([r("IA aplicada: ",{bold:true}),r("extracción de datos de documentos con modelos de visión (Anthropic Claude)")]),
 Bt([r("Seguridad: ",{bold:true}),r("firma digital (RSA, ECDSA), HMAC en webhooks, certificados X.509")]),
 Bt([r("Herramientas y prácticas: ",{bold:true}),r("Visual Studio, Git, IIS, Microsoft Clarity, Scrum")]),
 H("Educación"),
 P([r("Ingeniería en Mecatrónica",{bold:true}),r("  ·  Universidad Nacional Autónoma de México (UNAM)  ·  2017 – 2022  ·  Titulado, con cédula profesional")]),
 H("Certificaciones"),
 P([r("Scrum Foundation Professional Certificate (SFPC)",{bold:true}),r("  ·  CertiProf  ·  2024")]),
 H("Idiomas"),
 P([r("Español: nativo  ·  Inglés: básico (A2)")]),
];
const doc=new Document({creator:"Alexis Ortega",title:"CV Alexis Ortega",
 styles:{default:{document:{run:{font:F,size:20}}}},
 numbering:{config:[{reference:"b",levels:[{level:0,format:LevelFormat.BULLET,text:"•",alignment:AlignmentType.LEFT,style:{paragraph:{indent:{left:300,hanging:220}}}}]}]},
 sections:[{properties:{page:{size:{width:12240,height:15840},margin:{top:900,bottom:900,left:1080,right:1080}}},children}]});
Packer.toBuffer(doc).then(b=>fs.writeFileSync("17 CV.docx",b));
