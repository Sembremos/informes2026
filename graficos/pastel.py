import tempfile

import matplotlib.pyplot as plt

from styles.graficos import (
    GRAFICO_PASTEL_S
)


def insertar_grafico_pastel_s(
    pdf,
    etiquetas,
    valores,
    titulo,
    x,
    y
):

    fig, ax = plt.subplots(

        figsize=(

            GRAFICO_PASTEL_S["ancho"] / 100,

            GRAFICO_PASTEL_S["alto"] / 100

        )

    )

    ax.pie(

        valores,

        labels=etiquetas,

        autopct="%1.0f%%",

        colors=GRAFICO_PASTEL_S[
            "colores"
        ]

    )

    ax.set_title(

        titulo,

        fontsize=GRAFICO_PASTEL_S[
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

        width=GRAFICO_PASTEL_S["ancho"],

        height=GRAFICO_PASTEL_S["alto"]

    )
