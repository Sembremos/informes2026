from reportlab.lib.pagesizes import A4

def crear_subportada(pdf, delegacion, canton):

    ancho, alto = A4

    pdf.drawImage(
        "portadas/intro.png",
        0,
        0,
        width=ancho,
        height=alto
    )

    pdf.setFillColor("#FFFFFF")
    pdf.setFont("Helvetica-Bold", 34)

    pdf.drawCentredString(
        ancho / 2,
        200,
        "DELEGACIÓN POLICIAL"
    )

    pdf.setFont("Helvetica-Bold", 25)

    pdf.drawCentredString(
        ancho / 2,
        160,
        str(delegacion)
    )

    pdf.setFont("Helvetica-Bold", 20)

    pdf.drawCentredString(
        ancho / 2,
        125,
        str(canton)
    )

    pdf.showPage()
