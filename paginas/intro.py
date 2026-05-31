from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle

from styles.textos import TITULO_1, PARRAFO


def crear_intro(pdf):

    ancho_pagina, alto_pagina = A4

    # ==========================
    # PARÁMETROS MODIFICABLES
    # ==========================

    TITULO_X = 40
    TITULO_Y = 700

    PARRAFO_X = 40
    PARRAFO_Y = 430
    PARRAFO_ANCHO = 515
    PARRAFO_ALTO = 220

    IMAGEN_X = 0
    IMAGEN_Y = 60

    # ==========================
    # HEADER
    # ==========================

    header = ImageReader("portadas/header.png")

    hw, hh = header.getSize()

    header_alto = (hh / hw) * ancho_pagina

    pdf.drawImage(
        "portadas/header.png",
        0,
        alto_pagina - header_alto,
        width=ancho_pagina,
        height=header_alto
    )

    # ==========================
    # FOOTER
    # ==========================

    footer = ImageReader("portadas/footer.png")

    fw, fh = footer.getSize()

    footer_alto = (fh / fw) * ancho_pagina

    pdf.drawImage(
        "portadas/footer.png",
        0,
        0,
        width=ancho_pagina,
        height=footer_alto
    )

    # ==========================
    # TÍTULO
    # ==========================

    pdf.setFillColor(colors.HexColor(TITULO_1["color"]))
    pdf.setFont("Helvetica-Bold", TITULO_1["tamano"])

    pdf.drawString(
        TITULO_X,
        TITULO_Y,
        "Introducción"
    )

    # ==========================
    # PÁRRAFO
    # ==========================

    estilo_parrafo = ParagraphStyle(
        "Introduccion",
        fontName="Helvetica",
        fontSize=PARRAFO["tamano"],
        textColor=colors.HexColor(PARRAFO["color"]),
        alignment=4,  # Justificado
        leading=16
    )

    texto = """
    Desde el año 2022, el Ministerio de Seguridad Pública ha implementado en todo el territorio nacional el Modelo Preventivo de Gestión Policial, una iniciativa estratégica destinada a fortalecer la seguridad pública a través de un enfoque proactivo y colaborativo. Una parte integral de este modelo es la Estrategia Integral de Prevención para la Seguridad Pública, conocida como Sembremos Seguridad, que se centra en la contextualización de las dinámicas delincuenciales y sociales que afectan a nuestras comunidades.<br/><br/>

    El presente informe, elaborado para el territorio que comprende la Delegación Policial de San Ramón, surge como una herramienta esencial para la toma efectiva de decisiones. Este informe se concibe como un instrumento dinámico y orientado hacia el futuro, diseñado para proporcionar información clave y un plan de trabajo estructurado que permita abordar las problemáticas prioritarias identificadas en el ámbito de la seguridad pública.
    """

    parrafo = Paragraph(
        texto,
        estilo_parrafo
    )

    parrafo.wrap(
        PARRAFO_ANCHO,
        PARRAFO_ALTO
    )

    parrafo.drawOn(
        pdf,
        PARRAFO_X,
        PARRAFO_Y
    )

    # ==========================
    # IMAGEN INFERIOR
    # ==========================

    imagen = ImageReader(
        "portadas/conformacion.png"
    )

    iw, ih = imagen.getSize()

    imagen_alto = (ih / iw) * ancho_pagina

    pdf.drawImage(
        "portadas/conformacion.png",
        IMAGEN_X,
        IMAGEN_Y,
        width=ancho_pagina,
        height=imagen_alto
    )

    pdf.showPage()
