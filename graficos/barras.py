import matplotlib.pyplot as plt

from styles.graficos import (
    GRAFICO_BARRAS_L
)


def crear_grafico_barras(
    categorias,
    valores,
    titulo,
    ruta_salida
):

    fig, ax = plt.subplots(
        figsize=(
            GRAFICO_BARRAS_L["ancho"] / 100,
            GRAFICO_BARRAS_L["alto"] / 100
        )
    )

    colores = GRAFICO_BARRAS_L["colores"]

    barras = ax.bar(
        categorias,
        valores,
        color=colores[:len(categorias)]
    )

    ax.set_title(
        titulo,
        fontsize=GRAFICO_BARRAS_L["fuente_titulo"]
    )

    ax.tick_params(
        axis="x",
        labelsize=GRAFICO_BARRAS_L["fuente_etiquetas"]
    )

    ax.tick_params(
        axis="y",
        labelsize=GRAFICO_BARRAS_L["fuente_texto"]
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

    plt.tight_layout()

    plt.savefig(
        ruta_salida,
        bbox_inches="tight",
        dpi=300
    )

    plt.close()
