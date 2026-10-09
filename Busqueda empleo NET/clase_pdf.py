"""Genera el PDF de una nota de clase (por ejemplo, 11 Clase 0.1 Datos.md).
Uso (desde la raíz de la bóveda):  python clase_pdf.py "11 Clase 0.1 Datos"
Requiere: pandoc y Google Chrome o Chromium (variable CHROME si no está en la ruta por defecto).
"""
import os, re, shutil, subprocess, sys, tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
CHROMES = [os.environ.get("CHROME", ""), "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
           shutil.which("chromium") or "", shutil.which("google-chrome") or "",
           r"C:\Program Files\Google\Chrome\Application\chrome.exe"]

CSS = """
@page { size: letter; margin: 18mm 17mm 18mm 17mm; }
:root { --ink:#1F2328; --muted:#5F6672; --line:#D8DCE1; --accent:#2F5FD0; --soft:#EEF3FD; --warm:#FDF4E7; }
body { font-family: "DejaVu Sans", "Segoe UI", Arial, sans-serif; font-size: 10.2pt; line-height: 1.5; color: var(--ink); }
h1 { font-size: 24pt; line-height: 1.1; margin: 0 0 4pt; letter-spacing: -0.01em; }
h2 { font-size: 15pt; margin: 20pt 0 6pt; padding-top: 8pt; border-top: 2px solid var(--ink); break-after: avoid; }
h3 { font-size: 11.5pt; margin: 14pt 0 4pt; color: var(--accent); break-after: avoid; }
p, li { orphans: 3; widows: 3; }
hr { display: none; }
code { font-family: "DejaVu Sans Mono", Consolas, monospace; font-size: 9pt; background: #F1F3F5; padding: 0 3px; border-radius: 3px; }
table { border-collapse: collapse; width: 100%; margin: 6pt 0 10pt; font-size: 9.2pt; break-inside: avoid; }
th { text-align: left; background: var(--soft); font-weight: 700; }
th, td { border: 1px solid var(--line); padding: 4pt 6pt; vertical-align: top; }
blockquote { margin: 8pt 0; padding: 6pt 10pt; background: var(--warm); border-left: 4px solid #B8650A; }
blockquote p { margin: 0; }
strong { font-weight: 700; }
table.tarjetas td:first-child { width: 48%; font-weight: 600; }
"""

def a_markdown_imprimible(md: str) -> str:
    md = re.sub(r"\A---\n.*?\n---\n", "", md, flags=re.S)                 # frontmatter
    md = re.sub(r"\A\s*(>.*\n)+", "", md)                                  # encabezado de navegación de la bóveda
    md = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", md)                 # [[nota|texto]] -> texto
    md = re.sub(r"\[\[([^\]]+)\]\]", r"\1", md)                            # [[nota]] -> nota
    md = re.sub(r"^#flashcards\S*\s*$", "", md, flags=re.M)               # etiqueta del plugin
    salida, tarjetas = [], []
    for linea in md.split("\n") + [""]:
        m = None if "`::`" in linea else re.match(r"^(?!\|)(.+?)::(.+)$", linea)
        if m:
            tarjetas.append(m.groups()); continue
        if tarjetas:
            salida += ["", "<!--tarjetas-->", "| Pregunta | Respuesta |", "| --- | --- |"]
            salida += [f"| {q.strip()} | {a.strip()} |" for q, a in tarjetas] + [""]
            tarjetas = []
        salida.append(linea)
    return "\n".join(salida)

def main(nombre: str):
    origen = os.path.join(AQUI, nombre + ".md")
    destino = os.path.join(AQUI, nombre + ".pdf")
    md = a_markdown_imprimible(open(origen, encoding="utf-8").read())
    html = subprocess.run(["pandoc", "-f", "gfm", "-t", "html"], input=md, capture_output=True,
                          text=True, encoding="utf-8", check=True).stdout
    html = html.replace("<!--tarjetas-->\n<table>", '<table class="tarjetas">')
    doc = f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{nombre}</title><style>{CSS}</style></head><body>{html}</body></html>'
    chrome = next((c for c in CHROMES if c and os.path.exists(c)), None)
    if not chrome:
        sys.exit("No encontré Chrome/Chromium; define la variable CHROME con su ruta.")
    with tempfile.TemporaryDirectory() as tmp:
        ruta_html = os.path.join(tmp, "clase.html")
        open(ruta_html, "w", encoding="utf-8").write(doc)
        subprocess.run([chrome, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                        f"--print-to-pdf={destino}", "file://" + ruta_html.replace(os.sep, "/")],
                       check=True, capture_output=True)
    print("Listo:", destino)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('Uso: python clase_pdf.py "11 Clase 0.1 Datos"')
    main(sys.argv[1])
