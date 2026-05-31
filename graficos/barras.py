import tempfile

import matplotlib.pyplot as plt

from styles.graficos import (
    GRAFICO_BARRAS_L
)


def insertar_grafico_barras_l(
    pdf,
    categorias,
    valores,
    titulo,
    x,
    y
):

    fig, ax = plt.subplots(

        figsize=(

            GRAFICO_BARRAS_L["ancho"] / 100,

            GRAFICO_BARRAS_L["alto"] / 100

        )

    )

    barras = ax.bar(

        categorias,

        valores,

        color=GRAFICO_BARRAS_L["colores"][
            :len(categorias)
        ]

    )

    ax.set_title(

        titulo,

        fontsize=GRAFICO_BARRAS_L[
            "fuente_titulo"
        ]

    )

    for barra, valor in zip(

        barras,

        valores

    ):

        ax.text(

            barra.get_x()
            + barra.get_width() / 2,

            barra.get_height(),

            f"{valor:.2f}%",

            ha="center"

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

        width=GRAFICO_BARRAS_L["ancho"],

        height=GRAFICO_BARRAS_L["alto"]

    )
