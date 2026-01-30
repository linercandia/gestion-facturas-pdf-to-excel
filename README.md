# Gestión de Facturas (PDF a Excel)

Esta aplicación automatiza la extracción de datos de facturas en formato PDF y las exporta a un archivo Excel organizado. Ideal para agilizar procesos contables y administrativos.

## 🚀 Características

*   **Extracción Automática:** Obtiene Número de Factura, Fecha, Razón Social, Subtotal, IVA y Total.
*   **Procesamiento por Lotes:** Procesa todas las facturas contenidas en una carpeta automáticamente.
*   **Exportación a Excel:** Genera un reporte consolidado `.xlsx`.
*   **Detección Inteligente:** Utiliza expresiones regulares para adaptarse a formatos comunes de facturas.

## 📋 Requisitos

*   Python 3.x
*   Librerías listadas en `requirements.txt`

## 🛠️ Instalación

1.  Clona este repositorio:
    ```bash
    git clone https://github.com/linercandia/gestion-facturas.git
    cd gestion-facturas
    ```

2.  Crea un entorno virtual (opcional pero recomendado):
    ```bash
    python -m venv env
    source env/bin/activate  # En Windows: env\Scripts\activate
    ```

3.  Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## 💻 Uso

1.  Coloca tus archivos PDF de facturas en la carpeta `input_invoices`.
2.  Ejecuta el script principal:
    ```bash
    python main.py
    ```
3.  El archivo Excel resultante aparecerá en la carpeta `output_data` con el nombre `resumen_facturas.xlsx`.

## 📂 Estructura del Proyecto

*   `main.py`: Código fuente principal.
*   `input_invoices/`: Carpeta de entrada para los PDFs (se ignora en git excepto el ejemplo).
*   `output_data/`: Carpeta de salida para el Excel.
*   `generate_dummy_invoice.py`: Utilidad para crear una factura de prueba.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.
