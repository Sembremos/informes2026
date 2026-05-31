import matplotlib.pyplot as plt

from styles.graficos import (
    GRAFICO_PASTEL_S
)


def crear_grafico_pastel(
    etiquetas,
    valores,
    titulo,
    ruta_salida
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
        colors=GRAFICO_PASTEL_S["colores"]
    )

    ax.set_title(
        titulo,
        fontsize=GRAFICO_PASTEL_S["fuente_titulo"]
    )

    plt.tight_layout()

    plt.savefig(
        ruta_salida,
        bbox_inches="tight",
        dpi=300
    )

    plt.close()
