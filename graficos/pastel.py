import tempfile

import matplotlib.pyplot as plt

from reportlab.lib import colors

from styles.graficos import (
    GRAFICO_PASTEL_L,
    GRAFICO_PASTEL_M,
    GRAFICO_PASTEL_S
)


def _crear_pastel(
    pdf,
    etiquetas,
    valores,
    frecuencias,
    titulo,
    estilo,
    grafico_x,
    grafico_y,
    leyenda_x=None,
    leyenda_y=None
):

    lado = max(
        estilo["ancho"],
        estilo["alto"]
    )

    fig, ax = plt.subplots(
        figsize=(
            lado / 100,
            lado / 100
        )
    )

    wedges, texts, autotexts = ax.pie(
        valores,
        labels=None,
        autopct="%1.0f%%",
        colors=estilo["colores"],
        radius=1
    )

    for texto in autotexts:

        texto.set_color("black")
    
        texto.set_fontweight(
            "bold"
        )
    
        texto.set_fontsize(
            estilo["fuente_etiquetas"]
        )
    
        texto.set_bbox(
            dict(
                facecolor="white",
                edgecolor="none",
                alpha=0.75,
                boxstyle="round,pad=0.25"
            )
        )

    ax.axis("equal")

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
        dpi=300
    )

    plt.close()

    pdf.drawImage(
        temp.name,
        grafico_x,
        grafico_y,
        width=estilo["ancho"],
        height=estilo["alto"]
    )

    # ==========================
    # LEYENDA
    # ==========================

    if (
        leyenda_x is not None
        and
        leyenda_y is not None
    ):

        pdf.setFont(
            "Helvetica",
            8
        )

        y_actual = leyenda_y

        colores_grafico = estilo[
            "colores"
        ]

        for i in range(
            len(etiquetas)
        ):

            color = colores_grafico[
                i % len(colores_grafico)
            ]

            pdf.setFillColor(
                colors.HexColor(color)
            )

            pdf.rect(
                leyenda_x,
                y_actual - 7,
                8,
                8,
                fill=1,
                stroke=0
            )

            pdf.setFillColor(
                colors.black
            )

            pdf.drawString(
                leyenda_x + 14,
                y_actual - 2,
                f"{etiquetas[i]} ({frecuencias[i]})"
            )

            y_actual -= 14


def insertar_grafico_pastel_l(
    pdf,
    etiquetas,
    valores,
    frecuencias,
    titulo,
    grafico_x,
    grafico_y,
    leyenda_x=None,
    leyenda_y=None
):

    _crear_pastel(
        pdf,
        etiquetas,
        valores,
        frecuencias,
        titulo,
        GRAFICO_PASTEL_L,
        grafico_x,
        grafico_y,
        leyenda_x,
        leyenda_y
    )


def insertar_grafico_pastel_m(
    pdf,
    etiquetas,
    valores,
    frecuencias,
    titulo,
    grafico_x,
    grafico_y,
    leyenda_x=None,
    leyenda_y=None
):

    _crear_pastel(
        pdf,
        etiquetas,
        valores,
        frecuencias,
        titulo,
        GRAFICO_PASTEL_M,
        grafico_x,
        grafico_y,
        leyenda_x,
        leyenda_y
    )


def insertar_grafico_pastel_s(
    pdf,
    etiquetas,
    valores,
    frecuencias,
    titulo,
    grafico_x,
    grafico_y,
    leyenda_x=None,
    leyenda_y=None
):

    _crear_pastel(
        pdf,
        etiquetas,
        valores,
        frecuencias,
        titulo,
        GRAFICO_PASTEL_S,
        grafico_x,
        grafico_y,
        leyenda_x,
        leyenda_y
    )
