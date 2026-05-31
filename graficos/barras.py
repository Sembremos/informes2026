import tempfile

import matplotlib.pyplot as plt


from styles.graficos import (
    GRAFICO_BARRAS_L,
    GRAFICO_BARRAS_M,
    GRAFICO_BARRAS_S
)


def _crear_grafico(
    pdf,
    categorias,
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

    barras = ax.bar(

        categorias,

        valores,

        color=estilo["colores"][
            :len(categorias)
        ]

    )

    ax.set_title(

        titulo,

        fontsize=estilo[
            "fuente_titulo"
        ]

    )

    ax.tick_params(

        axis="x",

        labelsize=estilo[
            "fuente_etiquetas"
        ]

    )

    ax.tick_params(

        axis="y",

        labelsize=estilo[
            "fuente_texto"
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
    
            ha="center",
    
            fontsize=estilo[
                "fuente_etiquetas"
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


def insertar_grafico_barras_l(
    pdf,
    categorias,
    valores,
    titulo,
    x,
    y
):

    _crear_grafico(
        pdf,
        categorias,
        valores,
        titulo,
        GRAFICO_BARRAS_L,
        x,
        y
    )


def insertar_grafico_barras_m(
    pdf,
    categorias,
    valores,
    titulo,
    x,
    y
):

    _crear_grafico(
        pdf,
        categorias,
        valores,
        titulo,
        GRAFICO_BARRAS_M,
        x,
        y
    )


def insertar_grafico_barras_s(
    pdf,
    categorias,
    valores,
    titulo,
    x,
    y
):

    _crear_grafico(
        pdf,
        categorias,
        valores,
        titulo,
        GRAFICO_BARRAS_S,
        x,
        y
    )
