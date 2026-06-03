from openpyxl import load_workbook

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

from reportlab.platypus import (
    Paragraph,
    Table,
    TableStyle
)

from reportlab.lib.styles import (
    ParagraphStyle
)

from utils.header_footer import (
    dibujar_header_footer
)

from utils.excel import (
    cargar_excel
)

from styles.textos import (
    TITULO_2,
    PARRAFO
)

from styles.tablas import (
    TABLA_L2
)


def crear_metodologia(
    pdf,
    archivo_excel
):

    workbook = cargar_excel(
        archivo_excel
    )

    hoja = workbook.active

    ancho_pagina, alto_pagina = A4

    # ==================================================
    # PAGINA 1
    # PORTADA METODOLOGICA
    # ==================================================

    PORTADA_X = 0
    PORTADA_Y = 0

    PORTADA_ANCHO = ancho_pagina
    PORTADA_ALTO = alto_pagina

    pdf.drawImage(
        "portadas/metodologico.png",
        PORTADA_X,
        PORTADA_Y,
        width=PORTADA_ANCHO,
        height=PORTADA_ALTO
    )

    pdf.showPage()

    # ==================================================
    # PAGINA 2
    # PROCESO METODOLOGICO
    # ==================================================

    dibujar_header_footer(pdf)

    # ==================================================
    # PARAMETROS GENERALES
    # ==================================================

    TITULO_X = 40
    TITULO_Y = 750

    TEXTO_X = 40
    TEXTO_Y = 715

    TEXTO_ANCHO = 500
    TEXTO_ALTO = 40

    TABLA_COMUNIDAD_X = 40
    TABLA_COMUNIDAD_Y = 700

    TABLA_OTRAS_X = 40
    TABLA_OTRAS_Y = 600

    NETQUEST_X =20
    NETQUEST_Y = 300

    NETQUEST_ANCHO = 550
    NETQUEST_ALTO = 125

    LINEA_Y = 400

    DATOS_X = 0
    DATOS_Y = 90

    DATOS_ANCHO = 550
    DATOS_ALTO = 400

    # ==================================================
    # TITULO
    # ==================================================

    pdf.setFillColor(
        colors.HexColor(
            TITULO_2["color"]
        )
    )

    pdf.setFont(
        "Helvetica-Bold",
        TITULO_2["tamano"]
    )

    pdf.drawString(
        TITULO_X,
        TITULO_Y,
        "Proceso Metodologico"
    )

    # ==================================================
    # TEXTO
    # ==================================================

    estilo_parrafo = ParagraphStyle(
        "metodologia",
        fontName="Helvetica",
        fontSize=PARRAFO["tamano"],
        leading=15,
        alignment=4
    )

    texto = Paragraph(
        "Información demográfica según zona asignada a la Delegación Policial.",
        estilo_parrafo
    )

    texto.wrapOn(
        pdf,
        TEXTO_ANCHO,
        TEXTO_ALTO
    )

    texto.drawOn(
        pdf,
        TEXTO_X,
        TEXTO_Y
    )

    # ==================================================
    # TABLA ENCUESTA COMUNIDAD
    # ==================================================

    datos_comunidad = [

        [
            "Encuesta Comunidad",
            "",
            "",
            ""
        ]
    ]

    for fila in range(
        59,
        62
    ):

        datos_comunidad.append(
            [
                str(
                    hoja[f"A{fila}"].value
                    if hoja[f"A{fila}"].value is not None
                    else ""
                ),

                str(
                    hoja[f"B{fila}"].value
                    if hoja[f"B{fila}"].value is not None
                    else ""
                ),

                str(
                    hoja[f"C{fila}"].value
                    if hoja[f"C{fila}"].value is not None
                    else ""
                ),

                str(
                    hoja[f"D{fila}"].value
                    if hoja[f"D{fila}"].value is not None
                    else ""
                )
            ]
        )

    tabla_comunidad = Table(
        datos_comunidad,
        colWidths=[125] * 4,
        rowHeights=TABLA_L2["alto_fila"]
    )

    tabla_comunidad.setStyle(

        TableStyle(

            [

                (
                    "SPAN",
                    (0, 0),
                    (3, 0)
                ),

                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor(
                        TABLA_L2["color_header"]
                    )
                ),

                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor(
                        TABLA_L2["color_texto_header"]
                    )
                ),

                (
                    "FONTNAME",
                    (0, 0),
                    (-1, 0),
                    "Helvetica-Bold"
                ),

                (
                    "FONTSIZE",
                    (0, 0),
                    (-1, 0),
                    TABLA_L2["fuente_header"]
                ),

                (
                    "FONTSIZE",
                    (0, 1),
                    (-1, -1),
                    TABLA_L2["fuente_texto"]
                ),

                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    1,
                    colors.HexColor(
                        TABLA_L2["color_borde"]
                    )
                ),

                (
                    "ALIGN",
                    (0, 0),
                    (-1, -1),
                    "CENTER"
                ),

                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE"
                )

            ]

        )

    )

    ancho_tabla, alto_tabla = tabla_comunidad.wrap(
        0,
        0
    )

    tabla_comunidad.drawOn(
        pdf,
        TABLA_COMUNIDAD_X,
        TABLA_COMUNIDAD_Y - alto_tabla
    )

    # ==================================================
    # TABLA OTRAS ENCUESTAS
    # ==================================================

    datos_otras = [

        [
            "Otras Encuestas",
            "",
            ""
        ]
    ]

    for fila in range(
        63,
        65
    ):

        valor_a = hoja[
            f"G{fila}"
        ].value

        valor_c = hoja[
            f"I{fila}"
        ].value

        valor_d = hoja[
            f"J{fila}"
        ].value

        if (
            valor_a is None
            and
            valor_c is None
            and
            valor_d is None
        ):

            continue

        datos_otras.append(

            [

                str(valor_a)
                if valor_a is not None
                else "",

                str(valor_c)
                if valor_c is not None
                else "",

                str(valor_d)
                if valor_d is not None
                else ""

            ]

        )

    tabla_otras = Table(
        datos_otras,
        colWidths=[166, 166, 166],
        rowHeights=TABLA_L2["alto_fila"]
    )

    tabla_otras.setStyle(

        TableStyle(

            [

                (
                    "SPAN",
                    (0, 0),
                    (2, 0)
                ),

                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor(
                        TABLA_L2["color_header"]
                    )
                ),

                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor(
                        TABLA_L2["color_texto_header"]
                    )
                ),

                (
                    "FONTNAME",
                    (0, 0),
                    (-1, 0),
                    "Helvetica-Bold"
                ),

                (
                    "FONTSIZE",
                    (0, 0),
                    (-1, 0),
                    TABLA_L2["fuente_header"]
                ),

                (
                    "FONTSIZE",
                    (0, 1),
                    (-1, -1),
                    TABLA_L2["fuente_texto"]
                ),

                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    1,
                    colors.HexColor(
                        TABLA_L2["color_borde"]
                    )
                ),

                (
                    "ALIGN",
                    (0, 0),
                    (-1, -1),
                    "CENTER"
                ),

                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE"
                )

            ]

        )

    )

    ancho_tabla, alto_tabla = tabla_otras.wrap(
        0,
        0
    )

    tabla_otras.drawOn(
        pdf,
        TABLA_OTRAS_X,
        TABLA_OTRAS_Y - alto_tabla
    )

    # ==================================================
    # IMAGEN NETQUEST
    # ==================================================

    pdf.drawImage(
        "portadas/netquest.png",
        NETQUEST_X,
        NETQUEST_Y,
        width=NETQUEST_ANCHO,
        height=NETQUEST_ALTO
    )

    # ==================================================
    # LINEA
    # ==================================================

    pdf.line(
        0,
        LINEA_Y,
        ancho_pagina,
        LINEA_Y
    )

    # ==================================================
    # IMAGEN DATOS
    # ==================================================

    pdf.drawImage(
        "portadas/datos.png",
        DATOS_X,
        DATOS_Y,
        width=DATOS_ANCHO,
        height=DATOS_ALTO
    )

    # ==================================================
    # DATOS EXCEL
    # ==================================================

    comunidad = hoja["B83"].value
    comercio = hoja["B84"].value
    policial = hoja["B85"].value
    estadistica = hoja["C87"].value
    total = hoja["B88"].value

    # ==================================================
    # POSICIONES EDITABLES
    # ==================================================

    COMUNIDAD_X = 165
    COMUNIDAD_Y = 185

    COMERCIO_X = 165
    COMERCIO_Y = 95

    POLICIAL_X = 425
    POLICIAL_Y = 185

    ESTADISTICA_X = 425
    ESTADISTICA_Y = 95

    TOTAL_X = 295
    TOTAL_Y = 140

    # ==================================================
    # ESTILO NUMEROS
    # ==================================================

    pdf.setFillColor(
        colors.black
    )

    pdf.setFont(
        "Helvetica-Bold",
        18
    )

    pdf.drawCentredString(
        COMUNIDAD_X,
        COMUNIDAD_Y,
        str(comunidad)
    )

    pdf.drawCentredString(
        COMERCIO_X,
        COMERCIO_Y,
        str(comercio)
    )

    pdf.drawCentredString(
        POLICIAL_X,
        POLICIAL_Y,
        str(policial)
    )

    pdf.drawCentredString(
        ESTADISTICA_X,
        ESTADISTICA_Y,
        str(estadistica)
    )

    pdf.drawCentredString(
        TOTAL_X,
        TOTAL_Y,
        str(total)
    )

    pdf.showPage()
