import tempfile

import matplotlib.pyplot as plt


from styles.graficos import (
    GRAFICO_PASTEL_L,
    GRAFICO_PASTEL_M,
    GRAFICO_PASTEL_S
)


def _crear_pastel(
    pdf,
    etiquetas,
    valores,
    titulo,
    estilo,
    x,
    y
):

    fig, ax = plt.subplots(

        figsize=(

            estilo["ancho"] / 100,

            estilo["alto"] / 100

        )

    )

    ax.pie(

        valores,

        labels=etiquetas,

        autopct="%1.0f%%",

        colors=estilo[
            "colores"
        ]

    )

    ax.set_title(

        titulo,

        fontsize=estilo[
            "fuente_titulo"
        ]

    )

    temp = tempfile.NamedTemporaryFile(

        suffix=".png",

        delete=False

    )

    plt.tight_layout()

    plt.savefig(

        temp.name,

        dpi=300,

        bbox_inches="tight"

    )

    plt.close()

    pdf.drawImage(

        temp.name,

        x,

        y,

        width=estilo["ancho"],

        height=estilo["alto"]

    )


def insertar_grafico_pastel_l(
    pdf,
    etiquetas,
    valores,
    titulo,
    x,
    y
):

    _crear_pastel(
        pdf,
        etiquetas,
        valores,
        titulo,
        GRAFICO_PASTEL_L,
        x,
        y
    )


def insertar_grafico_pastel_m(
    pdf,
    etiquetas,
    valores,
    titulo,
    x,
    y
):

    _crear_pastel(
        pdf,
        etiquetas,
        valores,
        titulo,
        GRAFICO_PASTEL_M,
        x,
        y
    )


def insertar_grafico_pastel_s(
    pdf,
    etiquetas,
    valores,
    titulo,
    x,
    y
):

    _crear_pastel(
        pdf,
        etiquetas,
        valores,
        titulo,
        GRAFICO_PASTEL_S,
        x,
        y
    )
    
