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
    pdf.setFont("Helvetica-Bold", 24)

    pdf.drawCentredString(
        ancho / 2,
        300,
        "DELEGACIÓN POLICIAL"
    )

    pdf.setFont("Helvetica-Bold", 20)

    pdf.drawCentredString(
        ancho / 2,
        260,
        str(delegacion)
    )

    pdf.setFont("Helvetica", 16)

    pdf.drawCentredString(
        ancho / 2,
        225,
        str(canton)
    )

    pdf.showPage()
