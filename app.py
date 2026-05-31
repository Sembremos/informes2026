import streamlit as st
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


def generar_pdf():
    buffer = BytesIO()

    pdf = canvas.Canvas(buffer, pagesize=A4)

    ancho, alto = A4

    pdf.drawImage(
        "Portadas/portada.png",
        0,
        0,
        width=ancho,
        height=alto
    )

    pdf.showPage()

    pdf.save()

    buffer.seek(0)

    return buffer


st.set_page_config(
    page_title="Informes 2026",
    layout="wide"
)

st.title("Informes 2026")

if st.button("Generar PDF"):
    pdf_file = generar_pdf()

    st.download_button(
        label="Descargar PDF",
        data=pdf_file,
        file_name="informe.pdf",
        mime="application/pdf"
    )
