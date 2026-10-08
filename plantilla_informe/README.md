# Plantilla de informe LaTeX — EMMD (UTN FRP)

Plantilla para trabajos prácticos, informes y tesinas de la Especialización y Maestría en
Minería de Datos. Deriva de la usada en el Proyecto Final de grado (`../ProyectoFinal_2022/`).

## Uso rápido

```bash
cp -r docs/plantilla_informe ~/ruta/nuevo-trabajo    # copiar la carpeta completa
cd ~/ruta/nuevo-trabajo
# editar datos.tex (título, materia, autores, docentes...)
latexmk            # genera build/main.pdf
latexmk -pvc       # recompila automáticamente al guardar
latexmk -c         # borra archivos auxiliares
```

Requiere TeX Live con `biber` (en Debian/Ubuntu: `texlive-full`, o al menos
`texlive-latex-extra texlive-science texlive-bibtex-extra biber`).

## Estructura

```
main.tex              # documento: orden de secciones, índices, bibliografía
datos.tex             # ÚNICO archivo a editar para portada, encabezado y metadatos del PDF
informe.sty           # todo el formato (paquetes, colores, código, tablas, portada)
secciones/            # un archivo por sección (01-introduccion.tex, ...)
acronimos.tex         # siglas: \ac{KDD}, \acs{SQL}, ...
bibliografia.bib      # referencias (biblatex + biber)
codigo/               # .sql / .py / .R incluidos con \lstinputlisting
datos/                # CSV para tablas (\tablacsv) y gráficos (pgfplots)
imagenes/             # figuras (preferir PDF vectorial: draw.io → Exportar como PDF)
latexmkrc             # compilación: pdflatex + biber, salida en build/
```

## Opciones del estilo

En `main.tex`: `\usepackage[opciones]{informe}`

| Opción | Efecto |
|---|---|
| `cita=apa` (por defecto) | Citas autor-año APA 7 en español |
| `cita=numerico` | Citas numéricas `[1]` por orden de aparición (como en la tesis) |
| `borrador` | Marca de agua «BORRADOR» y muestra las notas `\pendiente{...}` |
| `sinsangria` | Párrafos sin sangría, separados por espacio |
| `interlineado=1.5` | Cambia el interlineado (por defecto 1.15) |

Para una tesina con capítulos: `\documentclass[11pt,a4paper]{report}` y `\chapter` en lugar de
`\section` en los archivos de `secciones/`. El estilo ya contempla `\chapter`.

## Recursos incluidos (ver ejemplos en `secciones/`)

| Necesidad | Cómo |
|---|---|
| Referencias cruzadas | `\cref{fig:x}` → «figura 1» (con enlace); `\Cref` al inicio de oración |
| Citas | `\textcite{clave}` → «Codd (1970)»; `\parencite{clave}` → «(Codd, 1970)» |
| Código SQL / Python / R | `\lstinputlisting[style=sql]{codigo/x.sql}` (también `style=python`, `r`, `consola`) |
| Tabla desde CSV | `\tablacsv{datos/x.csv}` (primera columna texto, resto con 3 decimales y coma) |
| Gráfico desde CSV | `pgfplots` → `\addplot table[x=..., y=..., col sep=comma]{datos/x.csv}` |
| Pseudocódigo | entorno `algorithm` (`algorithm2e`, en español) |
| Números y unidades | `\num{1234.5}` → 1 234,5; `\SI{3.5}{\giga\byte}`; columnas `S` alineadas por la coma |
| Notación | `\R`, `\E`, `\Var`, `\argmin`, `\argmax`, `\vect{x}`, `\mat{X}`, `\norm{x}`, `\abs{x}` |
| Recuadros | entornos `nota` e `importante` (título opcional entre `[ ]`) |

## Cambios respecto de la plantilla de la tesis

- La configuración pasó a un paquete (`informe.sty`) y los datos de portada a `datos.tex`: un trabajo
  nuevo solo requiere editar `datos.tex` y las secciones.
- Se corrigió `\include{configuracion}` (incluía el `\documentclass` y forzaba salto de página) y la
  página de derechos armada con `\\\\\\` (tenía una «s» suelta antes de `\newpage`).
- `hyperref` activo (índice, referencias y citas con enlaces) y `cleveref` en español.
- `bibtex`/`cite` → `biblatex` + `biber` (APA o numérico, acentos UTF-8 sin problemas, campos `doi`/`url`).
- `babel` con «Tabla» en lugar de «Cuadro» de forma nativa y sin conflictos con TikZ.
- Coma decimal en `siunitx` y `pgfplots`, acorde al uso en Argentina.
- Nuevos: código fuente con resaltado, tablas `booktabs`/desde CSV, gráficos `pgfplots`, algoritmos,
  acrónimos, resumen con palabras clave, modo borrador y compilación con `latexmk`.

## Sugerencias de flujo de trabajo

- **Python → LaTeX sin copiar números:** exportar métricas con `df.to_csv("datos/x.csv", index=False)`
  y usar `\tablacsv`, o `df.to_latex(...)` (genera `booktabs`) e incluirlo con `\input`.
- **Gráficos de matplotlib:** guardar en PDF (`plt.savefig("imagenes/x.pdf", bbox_inches="tight")`)
  para que sean vectoriales; para la misma tipografía que el texto, `plt.savefig("x.pgf")` + `\input`.
- **Referencias:** Zotero + extensión Better BibTeX con exportación automática a `bibliografia.bib`.
- **Editor:** VS Code con la extensión LaTeX Workshop respeta `latexmkrc` (vista previa y SyncTeX).
- **Versionado:** `build/` está en `.gitignore`; versionar solo fuentes y adjuntar el PDF en las entregas.
