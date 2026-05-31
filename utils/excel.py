from openpyxl import load_workbook


def cargar_excel(archivo_excel):

    workbook = load_workbook(
        archivo_excel,
        data_only=True
    )

    return workbook
