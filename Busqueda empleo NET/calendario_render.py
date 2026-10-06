"""Genera 04 Calendario dia por dia.pdf y .md a partir de calendario_datos.py.
Uso (desde la raíz del repo):  python calendario_render.py
Requiere: pip install reportlab
"""
import datetime as dt, os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from calendario_datos import D, SEMANAS
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor, white
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase.pdfmetrics import registerFontFamily

# Fuentes: DejaVu Sans Condensed (Linux) o Arial Narrow / Arial (Windows).
CANDIDATAS = [
    ("/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf"),
    ("C:/Windows/Fonts/ARIALN.TTF", "C:/Windows/Fonts/ARIALNB.TTF"),
    ("C:/Windows/Fonts/arial.ttf", "C:/Windows/Fonts/arialbd.ttf"),
]
for reg, bold in CANDIDATAS:
    if os.path.exists(reg) and os.path.exists(bold):
        pdfmetrics.registerFont(TTFont("R", reg)); pdfmetrics.registerFont(TTFont("B", bold)); break
else:
    sys.exit("No encontré una fuente TTF compatible; agrega su ruta en CANDIDATAS.")
registerFontFamily("R", normal="R", bold="B", italic="R", boldItalic="B")

SALIDA_PDF = os.path.join(AQUI, "04 Calendario dia por dia.pdf")
SALIDA_MD = os.path.join(AQUI, "04 Calendario dia por dia.md")

INK = HexColor("#1F2328"); MUTED = HexColor("#6B7280"); LINE = HexColor("#D8DCE1")
T = {  # tipo: (etiqueta, color fuerte, fondo)
    "teoria":   ("Teoría",       HexColor("#2F5FD0"), HexColor("#EEF3FD")),
    "codigo":   ("Código C#",    HexColor("#1E8A4C"), HexColor("#EDF7F1")),
    "mixto":    ("Mixto", HexColor("#6B4FC8"), HexColor("#F2EFFC")),
    "busqueda": ("Búsqueda",     HexColor("#B8650A"), HexColor("#FDF4E7")),
    "repos":    ("Repos", HexColor("#24292F"), HexColor("#F1F3F5")),
    "descanso": ("Descanso",     HexColor("#6B7280"), HexColor("#F4F5F7")),
    "prep":     ("Preparación",  HexColor("#0F7C86"), HexColor("#EAF6F7")),
    "pasado":   ("",             HexColor("#C4C8CE"), HexColor("#FAFAFB")),
}
MESES = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
DIAS = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]

W, H = landscape(letter)
M = 26
c = canvas.Canvas(SALIDA_PDF, pagesize=(W, H))
c.setTitle("Calendario del plan .NET · 12 semanas"); c.setAuthor("Alex")

def esc(s): return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def para(text, size, font="R", color=INK, lead=None):
    return Paragraph(text, ParagraphStyle("p", fontName=font, fontSize=size, leading=lead or size * 1.22, textColor=color))

# ---------------- Portada ----------------
def portada():
    c.setFillColor(INK); c.setFont("B", 26)
    c.drawString(M + 10, H - 70, "Plan .NET · calendario de 12 semanas")
    c.setFont("R", 12); c.setFillColor(MUTED)
    c.drawString(M + 10, H - 92, "Del 1 de octubre al 27 de diciembre de 2026 · ~12 horas por semana (11 h 45 min) · de los fundamentos a .NET sólido")
    y = H - 140
    c.setFont("B", 12); c.setFillColor(INK); c.drawString(M + 10, y, "Horario de cada semana")
    y -= 10
    filas = [("Lunes", "teoria", "1.5 h", "Teoría: arranca el nivel del árbol que toca"),
             ("Martes a jueves", "codigo", "1.5 h/día", "Código en C#: practicar lo que explicó la teoría"),
             ("Viernes", "busqueda", "1 h", "Búsqueda de empleo: CV, LinkedIn, aplicaciones"),
             ("Sábado", "teoria", "4 h", "Teoría a fondo (o teoría + código en semanas de cierre)"),
             ("Domingo", "repos", "45 min", "Leer repos de GitHub (30 min) + revisión semanal (15 min)")]
    for dia, t, h, txt in filas:
        y -= 26
        _, fuerte, fondo = T[t]
        c.setFillColor(fondo); c.roundRect(M + 10, y - 6, 470, 22, 5, fill=1, stroke=0)
        c.setFillColor(fuerte); c.rect(M + 10, y - 6, 4, 22, fill=1, stroke=0)
        c.setFillColor(INK); c.setFont("B", 10); c.drawString(M + 22, y + 1, dia)
        c.setFont("B", 10); c.setFillColor(fuerte); c.drawString(M + 130, y + 1, h)
        c.setFont("R", 10); c.setFillColor(INK); c.drawString(M + 195, y + 1, txt)

    x2 = M + 520; y2 = H - 140
    c.setFont("B", 12); c.setFillColor(INK); c.drawString(x2, y2, "Leyenda")
    y2 -= 8
    for t in ["prep", "teoria", "codigo", "mixto", "busqueda", "repos", "descanso"]:
        y2 -= 22
        et, fuerte, fondo = T[t]
        if t == "mixto": et = "Mixto (teoría + código)"
        if t == "repos": et = "Repos de GitHub"
        c.setFillColor(fondo); c.roundRect(x2, y2 - 5, 150, 18, 4, fill=1, stroke=0)
        c.setFillColor(fuerte); c.rect(x2, y2 - 5, 4, 18, fill=1, stroke=0)
        c.setFont("B", 9.5); c.drawString(x2 + 12, y2 + 1, et)
    y2 -= 26
    c.setFillColor(HexColor("#FFF7E0")); c.roundRect(x2, y2 - 5, 210, 18, 4, fill=1, stroke=0)
    c.setFillColor(HexColor("#8A5A00")); c.setFont("B", 9.5); c.drawString(x2 + 8, y2 + 1, "Entregable: se sube a GitHub ese día")
    y2 -= 22
    c.setFillColor(HexColor("#B42318")); c.setFont("B", 9.5); c.drawString(x2 + 8, y2 + 1, "Texto rojo: feriado o fecha especial")

    y = H - 330
    c.setFont("B", 12); c.setFillColor(INK); c.drawString(M + 10, y, "Fases")
    fases = [("Fase 1 · semanas 1–3", "La computadora por dentro (nivel 0), redes y C# base"),
             ("Fase 2 · semanas 4–8", "HTTP, web, APIs, criptografía, HTTPS, identidad, ASP.NET Core, EF Core y OAuth con Google Calendar"),
             ("Fase 3 · semanas 9–12", "SQL Server, JWT, webhooks, pruebas, Docker, CI y entrevistas")]
    for f, txt in fases:
        y -= 20
        c.setFont("B", 10); c.drawString(M + 10, y, f)
        c.setFont("R", 10); c.drawString(M + 150, y, txt)

    y -= 36
    c.setFont("B", 12); c.drawString(M + 10, y, "Reglas")
    reglas = ["Tú escribes el código; la IA explica, revisa y pregunta. Si no puedes explicar una línea, no está terminada.",
              "Cada término nuevo va a 08 Glosario con tu definición y un ejemplo de DiSí.",
              "Cierra cada sesión explicando en voz alta, en 2 minutos, lo que aprendiste.",
              "Si una semana se atrasa, no la saltes: mueve todo una semana."]
    for r in reglas:
        y -= 18
        c.setFont("R", 10); c.drawString(M + 10, y, "•  " + r)
    c.setFont("R", 8.5); c.setFillColor(MUTED)
    c.drawString(M + 10, 30, "Fuente de verdad: bóveda de Obsidian, carpeta Busqueda empleo NET (ver 00 Indice). Este calendario es 04 Calendario dia por dia.")
    c.showPage()

# ---------------- Páginas de semanas ----------------
TOP = 58; DAYH = 16; LABW = 30
GRIDX = M + LABW; GRIDW = W - M - GRIDX; COLW = GRIDW / 7
ROWH = (H - TOP - DAYH - M - 14) / 2

def caja(x, y, w, h, fecha):
    info = D.get(fecha.isoformat())
    tipo, horas, titulo, tareas, entregable, nota = info if info else ("pasado", "", "", [], None, None)
    et, fuerte, fondo = T[tipo]
    c.setFillColor(white); c.setStrokeColor(LINE); c.setLineWidth(0.8)
    c.roundRect(x + 2, y + 2, w - 4, h - 4, 5, fill=1, stroke=1)
    # banda superior
    bh = 24
    c.setFillColor(fondo); c.roundRect(x + 2, y + h - 2 - bh, w - 4, bh, 5, fill=1, stroke=0)
    c.rect(x + 2, y + h - 2 - bh, w - 4, 6, fill=1, stroke=0)
    c.setFillColor(fuerte); c.setFont("B", 15)
    c.drawString(x + 8, y + h - 21, str(fecha.day))
    nx = x + 8 + c.stringWidth(str(fecha.day), "B", 15) + 4
    c.setFont("R", 6.8); c.setFillColor(MUTED)
    c.drawString(nx, y + h - 13, MESES[fecha.month - 1][:3])
    if et and tipo != "descanso":
        c.setFont("B", 6.8); c.setFillColor(fuerte); c.drawString(nx, y + h - 21.5, et)
    if horas:
        c.setFont("B", 7.2); tw = c.stringWidth(horas, "B", 7.2)
        c.setFillColor(fuerte); c.roundRect(x + w - 10 - tw - 6, y + h - 20, tw + 8, 11, 5, fill=1, stroke=0)
        c.setFillColor(white); c.drawString(x + w - 10 - tw - 2, y + h - 17, horas)
    cy = y + h - 2 - bh - 4
    inner = w - 16
    bloques = []
    if nota:
        bloques.append(para(esc(nota), 6.6, "B", HexColor("#B42318")))
    if titulo:
        bloques.append(para(esc(titulo), 8.4, "B", INK))
    size = 7.4
    for _ in range(10):
        items = [para("• " + esc(t), size, "R", INK, size * 1.2) for t in tareas]
        ent = para("<b>Entregable:</b> " + esc(entregable), size, "R", HexColor("#6A4500"), size * 1.2) if entregable else None
        total = sum(p.wrap(inner, 999)[1] + 1.5 for p in bloques + items) + ((ent.wrap(inner - 8, 999)[1] + 10) if ent else 0)
        if total <= (cy - (y + 6)): break
        size -= 0.2
    yy = cy
    for p in bloques + items:
        _, ph = p.wrap(inner, 999); yy -= ph
        p.drawOn(c, x + 8, yy); yy -= 1.5
    if ent:
        _, ph = ent.wrap(inner - 8, 999)
        by = y + 7
        c.setFillColor(HexColor("#FFF7E0")); c.roundRect(x + 5, by, w - 10, ph + 7, 3, fill=1, stroke=0)
        ent.drawOn(c, x + 9, by + 3.5)
    if tipo == "pasado":
        c.setStrokeColor(HexColor("#E4E6EA")); c.setLineWidth(0.6)
        c.line(x + 10, y + 10, x + w - 10, y + h - 30)

def pagina(sems):
    ini = dt.date.fromisoformat(sems[0][0]); fin = dt.date.fromisoformat(sems[-1][0]) + dt.timedelta(days=6)
    meses = MESES[ini.month - 1].capitalize() if ini.month == fin.month else f"{MESES[ini.month-1].capitalize()} – {MESES[fin.month-1]}"
    c.setFillColor(INK); c.setFont("B", 20); c.drawString(M, H - 38, f"{meses} 2026")
    c.setFont("R", 9.5); c.setFillColor(MUTED)
    c.drawRightString(W - M, H - 36, f"{ini.day} {MESES[ini.month-1][:3]} – {fin.day} {MESES[fin.month-1][:3]} · Plan .NET")
    for i, dn in enumerate(DIAS):
        c.setFont("B", 8.5); c.setFillColor(MUTED)
        c.drawCentredString(GRIDX + COLW * i + COLW / 2, H - TOP - 11, dn.upper())
    for r, (lunes, nombre, foco) in enumerate(sems):
        y = H - TOP - DAYH - (r + 1) * ROWH - r * 14
        # etiqueta lateral
        c.saveState(); c.translate(M + 12, y + ROWH / 2); c.rotate(90)
        c.setFillColor(INK); c.setFont("B", 9.5)
        c.drawCentredString(0, 5, nombre.upper())
        c.setFont("R", 7.2); c.setFillColor(MUTED); c.drawCentredString(0, -6, foco)
        c.restoreState()
        base = dt.date.fromisoformat(lunes)
        for i in range(7):
            caja(GRIDX + COLW * i, y, COLW, ROWH, base + dt.timedelta(days=i))
    c.setFont("R", 7); c.setFillColor(MUTED)
    c.drawString(M, 14, "Teoría: sáb. + lun. · Código: mar.–jue. · Búsqueda: vie. · Repos de GitHub y revisión: dom.")
    c.drawRightString(W - M, 14, f"Página {c.getPageNumber()}")
    c.showPage()

portada()
for i in range(0, len(SEMANAS), 2):
    pagina(SEMANAS[i:i + 2])
c.save()


# ---------- Transcripción en Markdown (misma fuente de datos) ----------
ET = {"teoria":"Teoría","codigo":"Código C#","mixto":"Teoría + código","busqueda":"Búsqueda","descanso":"Descanso","prep":"Preparación","repos":"Repos de GitHub"}
def enlaces(t):
    t = t.replace("04 Calendario", "[[04 Calendario dia por dia|04 Calendario]]")
    for n in ["01 Bitacora", "08 Glosario", "09 Registro de aplicaciones"]:
        t = t.replace(n, f"[[{n}]]")
    return t
L = ["---", "tags: [busqueda-empleo, calendario]", f"actualizado: {dt.date.today().isoformat()}", "---",
     "> Generado por calendario_render.py desde calendario_datos.py. No editar a mano: cambia los datos y vuelve a generar.",
     "> Versión en PDF: [[04 Calendario dia por dia.pdf]] · Resumen semanal en [[03 Plan para huir de DiSi]] · Vista interactiva (artifact): https://claude.ai/artifact/737Dvitbv6Eds9XijvuBJA", "",
     "# Calendario del plan .NET, día por día", "",
     "Horario: lunes teoría (1.5 h) · martes a jueves código C# (1.5 h) · viernes búsqueda (1 h) · sábado teoría a fondo (4 h) · domingo repos de GitHub + revisión semanal (45 min). Total: unas 12 horas por semana (11 h 45 min).", ""]
MES3 = [m[:3] for m in MESES]
for lunes, nombre, foco in SEMANAS:
    L += [f"## {nombre} · {foco}", ""]
    base = dt.date.fromisoformat(lunes)
    for i in range(7):
        f = base + dt.timedelta(days=i); info = D.get(f.isoformat())
        if not info or info[0] == "pasado": continue
        tipo, horas, titulo, tareas, ent, nota = info
        L.append(f"### {DIAS[i]} {f.day} {MES3[f.month-1]} · {ET.get(tipo,'')}" + (f" · {horas}" if horas else ""))
        if nota: L.append(f"**{nota}**")
        if titulo: L.append(f"**{titulo}**")
        L += [f"- [ ] {enlaces(t)}" for t in tareas]
        if ent: L.append(f"- **Entregable:** {ent}")
        L.append("")
open(SALIDA_MD, "w", encoding="utf-8").write("\n".join(L))
print("Listo:", SALIDA_PDF, "y", SALIDA_MD)
