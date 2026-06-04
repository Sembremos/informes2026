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
    TABLA_L1
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

    NETQUEST_ANCHO = 550
    NETQUEST_ALTO = 120
    
    NETQUEST_X = (
        ancho_pagina -
        NETQUEST_ANCHO
    ) / 2
    
    NETQUEST_Y = 390

    LINEA_Y = 380
    
    DATOS_ANCHO = 550
    DATOS_ALTO = 263
    
    DATOS_X = (
        ancho_pagina -
        DATOS_ANCHO
    ) / 2
    
    DATOS_Y = 85

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
        61
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
        66
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

    COMUNIDAD_X = 150
    COMUNIDAD_Y = 255

    COMERCIO_X = 120
    COMERCIO_Y = 140

    POLICIAL_X = 425
    POLICIAL_Y = 255

    ESTADISTICA_X = 445
    ESTADISTICA_Y = 140

    TOTAL_X = 300
    TOTAL_Y = 140

    # ==================================================
    # ESTILO NUMEROS
    # ==================================================

    pdf.setFillColor(
        colors.white
    )

    pdf.setFont(
        "Helvetica-Bold",
        24
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


    # ==================================================
    # PAGINA 3
    # DIAGRAMA DE PARETO
    # ==================================================
    
    pdf.showPage()
    
    dibujar_header_footer(pdf)
    
    # ==================================================
    # PARAMETROS EDITABLES
    # ==================================================
    
    TITULO_X = 40
    TITULO_Y = 750
    
    TEXTO_X = 40
    TEXTO_Y = 715
    
    TEXTO_ANCHO = 500
    TEXTO_ALTO = 40
    
    PARETO_ANCHO = 550
    PARETO_ALTO = (750 * PARETO_ANCHO) / 2480
    
    PARETO_X = (
        ancho_pagina -
        PARETO_ANCHO
    ) / 2
    
    PARETO_Y = 550
    
    LINEA_Y = 535
    
    # -------------------------
    # DATOS SOBRE IMAGEN PARETO
    # -------------------------
    
    ENTRADA_X = 130
    ENTRADA_Y = 610
    
    REGISTRADOS_X = 445
    REGISTRADOS_Y = 650
    
    PARETO_20_80_X = 445
    PARETO_20_80_Y = 570
    
    FUENTE_PARETO = 24
    
    # -------------------------
    # TABLAS
    # -------------------------
    
    TABLA_DELITOS_X = 40
    TABLA_DELITOS_Y = 455
    
    TABLA_RIESGOS_X = 310
    TABLA_RIESGOS_Y = 455
    
    TABLA_ANCHO = 240
    
    # -------------------------
    # TOTALES
    # -------------------------
    
    PORC_DELITOS_X = 160
    PORC_DELITOS_Y = 450
    
    TOTAL_DELITOS_X = 160
    TOTAL_DELITOS_Y = 425
    
    PORC_RIESGOS_X = 430
    PORC_RIESGOS_Y = 450
    
    TOTAL_RIESGOS_X = 430
    TOTAL_RIESGOS_Y = 425
    
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
        "Diagrama de Pareto"
    )
    
    # ==================================================
    # PARRAFO
    # ==================================================
    
    estilo_parrafo = ParagraphStyle(
        "pareto",
        fontName="Helvetica",
        fontSize=PARRAFO["tamano"],
        leading=15,
        alignment=4
    )
    
    texto = Paragraph(
        "(Aplicando el principio de 80/20 donde el 80% es lo trivial y el 20% es lo vital)",
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
    # IMAGEN PARETO
    # ==================================================
    
    pdf.drawImage(
        "portadas/pareto.png",
        PARETO_X,
        PARETO_Y,
        width=PARETO_ANCHO,
        height=PARETO_ALTO
    )
    
    # ==================================================
    # DATOS PARETO
    # ==================================================
    
    entrada = hoja["A93"].value
    registrados = hoja["B93"].value
    pareto_20_80 = hoja["C93"].value
    
    pdf.setFillColor(
        colors.black
    )
    
    pdf.setFont(
        "Helvetica-Bold",
        FUENTE_PARETO
    )
    
    pdf.drawCentredString(
        ENTRADA_X,
        ENTRADA_Y,
        str(entrada)
    )
    
    pdf.drawCentredString(
        REGISTRADOS_X,
        REGISTRADOS_Y,
        str(registrados)
    )
    
    pdf.drawCentredString(
        PARETO_20_80_X,
        PARETO_20_80_Y,
        str(pareto_20_80)
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
    # TABLA DELITOS
    # ==================================================
    
    datos_delitos = [
        ["Delitos"]
    ]
    
    for fila in range(
        97,
        118
    ):
    
        valor = hoja[
            f"B{fila}"
        ].value
    
        if (
            valor is None
            or
            str(valor).strip() == ""
        ):
            continue
    
        datos_delitos.append(
            [str(valor)]
        )
    
    cantidad_delitos = len(
        datos_delitos
    ) - 1
    
    if cantidad_delitos <= 10:
    
        alto_fila_delitos = 20
    
    elif cantidad_delitos <= 15:
    
        alto_fila_delitos = 15
    
    else:
    
        alto_fila_delitos = 11
    
    tabla_delitos = Table(
        datos_delitos,
        colWidths=[
            TABLA_ANCHO
        ],
        rowHeights=alto_fila_delitos
    )
    
    tabla_delitos.setStyle(

        TableStyle(
    
            [
    
                (
                    "BACKGROUND",
                    (0,0),
                    (-1,0),
                    colors.HexColor(
                        TABLA_L1["color_header"]
                    )
                ),
    
                (
                    "TEXTCOLOR",
                    (0,0),
                    (-1,0),
                    colors.HexColor(
                        TABLA_L1["color_texto_header"]
                    )
                ),
    
                (
                    "FONTNAME",
                    (0,0),
                    (-1,0),
                    "Helvetica-Bold"
                ),
    
                (
                    "FONTSIZE",
                    (0,0),
                    (-1,0),
                    TABLA_L1["fuente_header"]
                ),
    
                (
                    "FONTSIZE",
                    (0,1),
                    (-1,-1),
                    TABLA_L1["fuente_texto"]
                ),
    
                (
                    "GRID",
                    (0,0),
                    (-1,-1),
                    1,
                    colors.HexColor(
                        TABLA_L1["color_borde"]
                    )
                ),
    
                (
                    "ALIGN",
                    (0,0),
                    (-1,-1),
                    "CENTER"
                ),
    
                (
                    "VALIGN",
                    (0,0),
                    (-1,-1),
                    "MIDDLE"
                )
    
            ]
    
        )
    
    )
    
    ancho_tabla, alto_tabla = tabla_delitos.wrap(
        0,
        0
    )
    
    tabla_delitos.drawOn(
        pdf,
        TABLA_DELITOS_X,
        TABLA_DELITOS_Y - alto_tabla
    )
    
    # ==================================================
    # TABLA RIESGOS
    # ==================================================
    
    datos_riesgos = [
        ["Riesgos"]
    ]
    
    for fila in range(
        97,
        118
    ):
    
        valor = hoja[
            f"C{fila}"
        ].value
    
        if (
            valor is None
            or
            str(valor).strip() == ""
        ):
            continue
    
        datos_riesgos.append(
            [str(valor)]
        )
    
    cantidad_riesgos = len(
        datos_riesgos
    ) - 1
    
    if cantidad_riesgos <= 10:
    
        alto_fila_riesgos = 20
    
    elif cantidad_riesgos <= 15:
    
        alto_fila_riesgos = 15
    
    else:
    
        alto_fila_riesgos = 11
    
    tabla_riesgos = Table(
        datos_riesgos,
        colWidths=[
            TABLA_ANCHO
        ],
        rowHeights=alto_fila_riesgos
    )
    
    tabla_riesgos.setStyle(

        TableStyle(
    
            [
    
                (
                    "BACKGROUND",
                    (0,0),
                    (-1,0),
                    colors.HexColor(
                        TABLA_L1["color_header"]
                    )
                ),
    
                (
                    "TEXTCOLOR",
                    (0,0),
                    (-1,0),
                    colors.HexColor(
                        TABLA_L1["color_texto_header"]
                    )
                ),
    
                (
                    "FONTNAME",
                    (0,0),
                    (-1,0),
                    "Helvetica-Bold"
                ),
    
                (
                    "FONTSIZE",
                    (0,0),
                    (-1,0),
                    TABLA_L1["fuente_header"]
                ),
    
                (
                    "FONTSIZE",
                    (0,1),
                    (-1,-1),
                    TABLA_L1["fuente_texto"]
                ),
    
                (
                    "GRID",
                    (0,0),
                    (-1,-1),
                    1,
                    colors.HexColor(
                        TABLA_L1["color_borde"]
                    )
                ),
    
                (
                    "ALIGN",
                    (0,0),
                    (-1,-1),
                    "CENTER"
                ),
    
                (
                    "VALIGN",
                    (0,0),
                    (-1,-1),
                    "MIDDLE"
                )
    
            ]
    
        )
    
    )
    ancho_tabla, alto_tabla = tabla_riesgos.wrap(
        0,
        0
    )
    
    tabla_riesgos.drawOn(
        pdf,
        TABLA_RIESGOS_X,
        TABLA_RIESGOS_Y - alto_tabla
    )
    
    # ==================================================
    # PORCENTAJES
    # ==================================================
    
    porcentaje_delitos = hoja["B118"].value
    porcentaje_riesgos = hoja["C118"].value
    
    pdf.setFont(
        "Helvetica-Bold",
        24
    )
    
    pdf.drawCentredString(
        PORC_DELITOS_X,
        PORC_DELITOS_Y,
        str(porcentaje_delitos)
    )
    
    pdf.drawCentredString(
        PORC_RIESGOS_X,
        PORC_RIESGOS_Y,
        str(porcentaje_riesgos)
    )
    
    # ==================================================
    # TOTAL DATOS
    # ==================================================
    
    total_delitos = hoja["B119"].value
    total_riesgos = hoja["C119"].value
    
    pdf.setFont(
        "Helvetica",
        12
    )
    
    pdf.drawCentredString(
        TOTAL_DELITOS_X,
        TOTAL_DELITOS_Y,
        f"Total: {total_delitos}"
    )
    
    pdf.drawCentredString(
        TOTAL_RIESGOS_X,
        TOTAL_RIESGOS_Y,
        f"Total: {total_riesgos}"
    )
