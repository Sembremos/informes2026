from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib import colors


def dibujar_tabla(
    pdf,
    datos,
    estilo,
    x,
    y
):

    if not datos:
        return

    cantidad_columnas = len(datos[0])

    ancho_columna = (
        estilo["ancho"] /
        cantidad_columnas
    )

    tabla = Table(
        datos,
        colWidths=[
            ancho_columna
        ] * cantidad_columnas,
        rowHeights=estilo["alto_fila"]
    )

    configuracion = [

        (
            "BACKGROUND",
            (0, 0),
            (-1, 0),
            colors.HexColor(
                estilo["color_header"]
            )
        ),

        (
            "TEXTCOLOR",
            (0, 0),
            (-1, 0),
            colors.HexColor(
                estilo["color_texto_header"]
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
            estilo["fuente_header"]
        ),

        (
            "FONTSIZE",
            (0, 1),
            (-1, -1),
            estilo["fuente_texto"]
        ),

        (
            "GRID",
            (0, 0),
            (-1, -1),
            1,
            colors.HexColor(
                estilo["color_borde"]
            )
        )
    ]

    if "color_primera_columna" in estilo:

        configuracion.append(

            (
                "BACKGROUND",
                (0, 1),
                (0, -1),
                colors.HexColor(
                    estilo["color_primera_columna"]
                )
            )

        )

    tabla.setStyle(
        TableStyle(
            configuracion
        )
    )

    ancho_tabla, alto_tabla = tabla.wrap(
        0,
        0
    )

    tabla.drawOn(
        pdf,
        x,
        y - alto_tabla
    )
