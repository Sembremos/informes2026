from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader


def dibujar_header_footer(pdf):

    ancho_pagina, alto_pagina = A4

    header = ImageReader(
        "portadas/header.png"
    )

    hw, hh = header.getSize()

    header_alto = (
        hh / hw
    ) * ancho_pagina

    pdf.drawImage(
        "portadas/header.png",
        0,
        alto_pagina - header_alto,
        width=ancho_pagina,
        height=header_alto
    )

    footer = ImageReader(
        "portadas/footer.png"
    )

    fw, fh = footer.getSize()

    footer_alto = (
        fh / fw
    ) * ancho_pagina

    pdf.drawImage(
        "portadas/footer.png",
        0,
        0,
        width=ancho_pagina,
        height=footer_alto
    )
