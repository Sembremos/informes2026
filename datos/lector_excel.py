from openpyxl import load_workbook


def leer_datos_generales(archivo_excel):

    workbook = load_workbook(
        archivo_excel,
        data_only=True
    )

    hoja = workbook["Hoja1"]

    delegacion = hoja["B2"].value
    canton = hoja["B3"].value

    return {
        "delegacion": delegacion,
        "canton": canton
    }
