# Plantilla de presentación Beamer — UTN FRC

Plantilla para presentaciones de **Análisis de Señales y Sistemas** (UTN Facultad Regional
Córdoba), pensada para contenido con mucha matemática. Usa la identidad visual oficial de la
UTN FRC: logos, paleta y tipografía del [Manual de Identidad Visual](https://identidad.frc.utn.edu.ar/)
(versión reducida, mayo 2026).

## Uso rápido

```bash
cp -r plantilla_presentacion ~/ruta/nueva-presentacion
cd ~/ruta/nueva-presentacion
# editar datos.tex (título, materia, curso, autores, docentes, fecha)
latexmk            # genera build/main.pdf
latexmk -pvc       # recompila automáticamente al guardar
latexmk -c         # borra archivos auxiliares
```

Requiere TeX Live con pdfLaTeX y `biber` (en Debian/Ubuntu: `texlive-full`, o al menos
`texlive-latex-extra texlive-science texlive-fonts-extra texlive-pictures biber`).

## Estructura

```
main.tex                 # documento: portada, índice, orden de secciones, bibliografía, cierre
datos.tex                # ÚNICO archivo a editar para portada, pie y metadatos del PDF
beamerthemeutnfrc.sty    # tema visual (colores, fuentes, portada, separadores, pie, bloques)
senales.sty              # notación de señales y sistemas + estilos TikZ/pgfplots
secciones/               # un archivo por sección (01-senales.tex, ...) y A-respaldo.tex
bibliografia.bib         # referencias (biblatex + biber, numérico)
imagenes/logos/          # logos oficiales UTN FRC en PDF vectorial
latexmkrc                # compilación: pdflatex + biber, salida en build/
```

## Opciones de la clase

En `main.tex`: `\documentclass[aspectratio=169, 11pt]{beamer}`

| Opción | Efecto |
|---|---|
| `aspectratio=169` (por defecto) / `43` | Formato panorámico o 4:3 |
| `handout` | Versión para imprimir o compartir: colapsa las capas (`\pause`, `<2->`) en una sola página |
| `10pt` / `11pt` / `12pt` | Tamaño base de letra |

## Elementos del tema

| Necesidad | Cómo |
|---|---|
| Portada | `\portada` (usa `\title`, `\subtitle`, `\author`, `\materia`, `\curso`, `\docentes`, `\date`) |
| Separador de sección | Automático en cada `\section{...}` (número grande + título) |
| Cierre | `\diapositivacierre[correo o URL]{¿Preguntas?}` |
| Bloques | `definicion`, `teorema`, `propiedad`, `ejemplo`, `importante`, `observacion`; título opcional: `\begin{teorema}[Parseval]` |
| Bloque por capas | `\begin{ejemplo}<2->[...]` |
| Demostración | entorno `demostracion` (termina con `\qedhere` dentro de `align*`) |
| Resaltar una expresión | `\resaltar{...}` o `\resaltar<3->{...}` (fondo azul claro, sin mover la ecuación) |
| Diapositivas de respaldo | después de `\appendix`; no suman al total del pie |

Colores disponibles (paleta oficial): `azulutn`, `azuloscuro`, `azulclaro`, `celeste`,
`celesteoscuro`, `celesteclaro`, `gris`, `negro`, `grisclaro`, `vital`, `vision`, `energia`.

## Notación (`senales.sty`)

| Comando | Resultado |
|---|---|
| `\R \C \N \Zent` | Conjuntos ℝ ℂ ℕ ℤ |
| `\j`, `\e`, `\dd` | Unidad imaginaria j, número e y diferencial rectos: `\int x(t) \dd t` |
| `\abs{x}`, `\norm{x}`, `\conj{X}` | \|x\|, ‖x‖, X* (`\abs*{...}` ajusta el tamaño) |
| `\Re`, `\Im` | Parte real e imaginaria (operadores rectos) |
| `\escalon{t}`, `\impulso{t}` | u(t), δ(t) |
| `\rect`, `\sinc`, `\sgn` | Operadores; `\sinc(x) = sen(πx)/(πx)` |
| `\conv`, `\convcirc` | Convolución lineal ∗ y circular ⊛ |
| `\TF{x(t)}`, `\iTF{}`, `\TL{}`, `\iTL{}`, `\TZ{}`, `\iTZ{}` | ℱ{·}, ℱ⁻¹{·}, ℒ{·}, 𝒵{·} … |
| `\fourier`, `\laplace`, `\ztransf` | Par transformado ○—● con ℱ, ℒ o 𝒵 encima: `x(t) \fourier X(\j\omega)` |
| `\Fourier`, `\Laplace`, `\Ztransf` | Mismo símbolo en sentido inverso ●—○ |
| `\ROC` | Región de convergencia |
| `\laplaciano` | Operador laplaciano ∆ (el nombre `\laplace` se usa para el par) |

Con babel en español, `\sin` se escribe «sen» y `\lim` se escribe «lím».

## Gráficos (`senales.sty`)

| Estilo | Uso |
|---|---|
| `ejes senal` | Ejes centrados con flechas: `\begin{axis}[ejes senal, xlabel={$t$}]` |
| `senal continua` | `\addplot[senal continua, domain=0:5] {exp(-x)};` |
| `senal discreta` | Tallos con círculo: `\addplot[senal discreta, domain=0:10, samples=11] {0.8^x};` |
| `espectro` | Igual que `ejes senal`, con eje en ω |
| `bode` | `\begin{semilogxaxis}[bode] ... \end{semilogxaxis}` (escala log y grilla) |
| `plano s`, `plano z` | Plano complejo; `plano z` dibuja el círculo unitario |
| `polo`, `cero` | `\addplot[polo] coordinates {(-1,2) (-1,-2)};` |
| `bloque`, `sumador`, `rama`, `flecha` | Diagramas de bloques en TikZ (ver `02-sistemas-lti.tex` y `04-laplace-z.tex`) |

Las curvas con `\addplot+` siguen la paleta institucional (azul, naranja, magenta, verde,
celeste). Las funciones trigonométricas de pgfplots trabajan en grados: `sin(deg(x))`.

## Identidad visual

- **Logos:** descargados en SVG de `https://identidad.frc.utn.edu.ar/logos/` (versiones
  Extendida Facultad, Reducida y Reducida Vertical) y convertidos a PDF con Inkscape. No deben
  deformarse ni recolorearse; para fondos oscuros se usan las versiones blancas.
- **Colores:** paleta primaria (azules), secundaria (celestes), neutros y complementarios del
  manual; el gradiente oficial va de Celeste Asento `#40C5F2` a Azul UTN FRC `#1538B8`.
- **Tipografía:** el manual indica **Barlow** para textos generales y **Noto Sans** para títulos
  y textos destacados. La plantilla usa Noto Sans en todo el documento porque tiene una fuente
  matemática del mismo diseño (`notomath`) que funciona con pdfLaTeX. Barlow no tiene versión
  matemática, y combinarla con otra fuente para las ecuaciones da un resultado menos coherente
  en una presentación con mucha matemática.

## Sugerencias

- **Gráficos de Python:** `plt.savefig("imagenes/x.pdf", bbox_inches="tight")` para que sean
  vectoriales, o exportar los datos a CSV y graficarlos con `pgfplots`
  (`\addplot table[x=t, y=y, col sep=comma]{datos/x.csv};`).
- **Capas:** usar `\only<n>` / `\onslide<n->` dentro de gráficos y en las celdas de `align*`
  (`\onslide<2->{c_k} &\onslide<2->{= ...}`); `\pause` dentro de `align*` desordena las capas.
- **Versionado:** `build/` está en `.gitignore`; versionar solo las fuentes.
