import streamlit as st
from io import BytesIO

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from datos.lector_excel import leer_datos_generales
from paginas.subportada import crear_subportada


def generar_pdf(archivo_excel):

    datos = leer_datos_generales(
        archivo_excel
    )

    buffer = BytesIO()

    pdf = canvas.Canvas(
        buffer,
        pagesize=A4
    )

    ancho, alto = A4

    # PORTADA PRINCIPAL

    pdf.drawImage(
        "portadas/portada.png",
        0,
        0,
        width=ancho,
        height=alto
    )

    pdf.showPage()

    # SUBPORTADA

    crear_subportada(
        pdf,
        datos["delegacion"],
        datos["canton"]
    )

    pdf.save()

    buffer.seek(0)

    return buffer


st.set_page_config(
    page_title="Informes 2026",
    layout="wide"
)

st.title("Informes 2026")

archivo_excel = st.file_uploader(
    "Seleccione el archivo Excel",
    type=["xlsx"]
)

if archivo_excel is not None:

    if st.button("Generar PDF"):

        pdf_file = generar_pdf(
            archivo_excel
        )

        st.download_button(
            label="Descargar PDF",
            data=pdf_file,
            file_name="informe.pdf",
            mime="application/pdf"
        )
