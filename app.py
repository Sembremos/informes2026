import streamlit as st
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generar_pdf():
buffer = BytesIO()

```
pdf = canvas.Canvas(buffer, pagesize=A4)

ancho, alto = A4

# Página 1 - Portada de prueba
pdf.setTitle("Informe Comunitario")

pdf.setFont("Helvetica-Bold", 28)
pdf.drawCentredString(
    ancho / 2,
    alto - 180,
    "INFORME COMUNITARIO"
)

pdf.setFont("Helvetica", 14)
pdf.drawCentredString(
    ancho / 2,
    alto - 220,
    "Versión de prueba"
)

pdf.showPage()

# Página 2 - Contenido de prueba
pdf.setFont("Helvetica-Bold", 20)
pdf.drawString(
    50,
    alto - 80,
    "Página de prueba"
)

pdf.setFont("Helvetica", 12)
pdf.drawString(
    50,
    alto - 120,
    "Si estás viendo esta página,"
)

pdf.drawString(
    50,
    alto - 140,
    "la estructura base funciona correctamente."
)

pdf.showPage()

pdf.save()

buffer.seek(0)

return buffer
```

st.set_page_config(
page_title="Generador de Informes",
layout="wide"
)

st.title("Generador de Informes")

st.write(
"Versión inicial del sistema."
)

if st.button("Generar PDF"):

```
pdf_file = generar_pdf()

st.success("PDF generado correctamente.")

st.download_button(
    label="Descargar PDF",
    data=pdf_file,
    file_name="informe.pdf",
    mime="application/pdf"
)
```

