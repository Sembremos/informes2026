from openpyxl import load_workbook

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

from styles.textos import TITULO_2
from styles.textos import Subti

from styles.tablas import TABLA_L3

from utils.header_footer import (
    dibujar_header_footer
)

from utils.tablas import (
    dibujar_tabla
)


def crear_indice(
    pdf,
    archivo_excel
):

    workbook = load_workbook(
        archivo_excel,
        data_only=True
    )

    hoja = workbook["Hoja1"]

    ancho_pagina, alto_pagina = A4

    # ==========================
    # PORTADA PARTICIPACIÓN
    # ==========================

    pdf.drawImage(
        "portadas/participacion.png",
        0,
        0,
        width=ancho_pagina,
        height=alto_pagina
    )

    pdf.showPage()

    # ==========================
    # PÁGINA DISTRITO
    # ==========================

    dibujar_header_footer(pdf)

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
        40,
        750,
        "Datos de Participación"
    )

    pdf.setFillColor(
        colors.HexColor(
            Subti["color"]
        )
    )

    pdf.setFont(
        "Helvetica-Bold",
        Subti["tamano"]
    )

    pdf.drawString(
        40,
        700,
        "Participación por Distrito"
    )

    # ==========================
    # TABLA DISTRITO
    # ==========================

    datos_tabla = [
        [
            "Distrito",
            "%",
            "Frecuencia"
        ]
    ]

    for fila in range(
        7,
        12
    ):

        distrito = hoja[
            f"A{fila}"
        ].value

        porcentaje = hoja[
            f"B{fila}"
        ].value

        frecuencia = hoja[
            f"C{fila}"
        ].value

        if distrito is None:

            continue
        
        if str(distrito).strip() == "":
        
            continue

        datos_tabla.append(
            [
                str(distrito),
                str(porcentaje),
                str(frecuencia)
            ]
        )

    dibujar_tabla(
        pdf,
        datos_tabla,
        TABLA_L3,
        40,
        650
    )

    # ==========================
    # RELACIÓN POR DISTRITO
    # ==========================

    pdf.setFillColor(
        colors.HexColor(
            Subti["color"]
        )
    )

    pdf.setFont(
        "Helvetica-Bold",
        Subti["tamano"]
    )

    pdf.drawString(
        40,
        310,
        "Relación por Distrito"
    )

    categorias = []
    valores = []

    for fila in range(
        8,
        12
    ):

        categoria = hoja[
            f"G{fila}"
        ].value

        porcentaje = hoja[
            f"H{fila}"
        ].value

        if categoria is None:
        
            continue
        
        if str(categoria).strip() == "":
        
            continue

        categorias.append(
            str(categoria)
        )

        if porcentaje is None:
            continue
        
        print(
            "FILA:", fila,
            "CATEGORIA:", categoria,
            "PORCENTAJE:", porcentaje,
            "TIPO:", type(porcentaje)
        )
        
        
        try:
        
            valores.append(
                float(porcentaje)
            )
        
        except:
        
            if porcentaje is None:
                continue
            
            valores.append(
                float(porcentaje)
            )

    from graficos.barras import (
        insertar_grafico_barras_l
    )

    insertar_grafico_barras_l(
        pdf,
        categorias,
        valores,
        "Participación por Distrito",
        40,
        20
    )

    pdf.showPage()

    # ==========================
    # PAGINA 3
    # ==========================

    dibujar_header_footer(pdf)

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
        40,
        750,
        "Datos de Participación"
    )

    from styles.tablas import TABLA_M

    from graficos.pastel import (
        insertar_grafico_pastel_s
    )

    # =====================================
    # EDAD
    # =====================================

    pdf.line(
        20,
        520,
        575,
        520
    )

    etiquetas_edad = []
    valores_edad = []

    tabla_edad = [
        [
            "Edad",
            "Frecuencia"
        ]
    ]

    for fila in range(
        29,
        34
    ):

        categoria = hoja[
            f"A{fila}"
        ].value

        porcentaje = hoja[
            f"B{fila}"
        ].value

        frecuencia = hoja[
            f"C{fila}"
        ].value

        if categoria is None:
            continue

        etiquetas_edad.append(
            str(categoria)
        )

        if porcentaje is None:
            continue

        valores_edad.append(
            float(porcentaje) * 100
        )

        tabla_edad.append(
            [
                str(categoria),
                str(frecuencia)
            ]
        )

    insertar_grafico_pastel_s(
        pdf,
        etiquetas_edad,
        valores_edad,
        "Participación por Edad",
        30,
        545
    )

    dibujar_tabla(
        pdf,
        tabla_edad,
        TABLA_M,
        300,
        700
    )

    # =====================================
    # ESCOLARIDAD
    # =====================================

    pdf.line(
        20,
        350,
        575,
        350
    )

    etiquetas_escolaridad = []
    valores_escolaridad = []

    tabla_escolaridad = [
        [
            "Escolaridad",
            "Frecuencia"
        ]
    ]

    for fila in range(
        39,
        47
    ):

        categoria = hoja[
            f"A{fila}"
        ].value

        porcentaje = hoja[
            f"B{fila}"
        ].value

        frecuencia = hoja[
            f"C{fila}"
        ].value

        if categoria is None:
            continue

        etiquetas_escolaridad.append(
            str(categoria)
        )

        if porcentaje is None:
            continue

        valores_escolaridad.append(
            float(porcentaje) * 100
        )

        tabla_escolaridad.append(
            [
                str(categoria),
                str(frecuencia)
            ]
        )

    insertar_grafico_pastel_s(
        pdf,
        etiquetas_escolaridad,
        valores_escolaridad,
        "Participación por Escolaridad",
        30,
        375
    )

    dibujar_tabla(
        pdf,
        tabla_escolaridad,
        TABLA_M,
        300,
        535
    )
    
     # =====================================
    # GENERO
    # =====================================

    pdf.line(
        20,
        180,
        575,
        180
    )

    etiquetas_genero = []
    valores_genero = []

    tabla_genero = [
        [
            "Genero",
            "Frecuencia"
        ]
    ]

    for fila in range(
        52,
        55
    ):

        categoria = hoja[
            f"A{fila}"
        ].value

        porcentaje = hoja[
            f"B{fila}"
        ].value

        frecuencia = hoja[
            f"C{fila}"
        ].value

        if categoria is None:
            continue

        etiquetas_genero.append(
            str(categoria)
        )

        if porcentaje is None:
            continue

        valores_genero.append(
            float(porcentaje) * 100
        )

        tabla_genero.append(
            [
                str(categoria),
                str(frecuencia)
            ]
        )

    insertar_grafico_pastel_s(
        pdf,
        etiquetas_genero,
        valores_genero,
        "Participación por Genero",
        30,
        200
    )

    dibujar_tabla(
        pdf,
        tabla_genero,
        TABLA_M,
        300,
        350
    )
