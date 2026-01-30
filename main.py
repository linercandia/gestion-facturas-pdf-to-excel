import os
import pdfplumber
import pandas as pd
import re
from datetime import datetime

# Configuración
INPUT_FOLDER = 'input_invoices'
OUTPUT_FOLDER = 'output_data'
OUTPUT_FILE = os.path.join(OUTPUT_FOLDER, 'resumen_facturas.xlsx')

def extract_invoice_data(pdf_path):
    """
    Extrae datos de una única factura en PDF.
    Esta función necesita ser personalizada basándose en el diseño específico de las facturas.
    Por ahora, utiliza expresiones regulares para encontrar patrones comunes.
    """
    data = {
        'Archivo': os.path.basename(pdf_path),
        'Numero Factura': None,
        'Fecha': None,
        'Razon Social': None,
        'Subtotal': None,
        'IVA': None,
        'Total': None
    }
    
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    
    # Encontrando fechas (ej., 20/01/2023, 20-01-2023, 2026-01-30)
    date_match = re.search(r'(\d{2}[/-]\d{2}[/-]\d{4}|\d{4}[/-]\d{2}[/-]\d{2})', text)
    if date_match:
        data['Fecha'] = date_match.group(0)

    # Encontrando Número de Factura
    # Busca "Factura No:", "Folio:", etc. dentro de la misma línea o bloque
    # Usamos [:] para asegurar que encontramos dos puntos, lo que ayuda a anclar el valor
    invoice_no_match = re.search(r'(?:Factura|Folio)(?:\s+(?:No\.?|Num\.?))?\s*[:]\s*([A-Za-z0-9-]+)', text, re.IGNORECASE)
    if invoice_no_match:
        data['Numero Factura'] = invoice_no_match.group(1)

    # Encontrando Importes (busca formato de moneda)
    def get_amount(label):
        # \b asegura que coincidamos con "Total" no "Subtotal"
        # \d+ permite números como 4000 sin comas. (?:,\d{3})* maneja 1,000,000
        pattern = r'\b{}.*?\$?\s?(\d+(?:,\d{{3}})*[\.,]\d{{2}})'.format(label)
        match = re.search(pattern, text, re.IGNORECASE)
        return match.group(1) if match else None

    data['Subtotal'] = get_amount('Subtotal')
    data['IVA'] = get_amount('IVA')
    data['Total'] = get_amount('Total')

    # Encontrando Razón Social (Heurística: La primera línea del PDF a menudo contiene el nombre de la empresa)
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    if lines:
        data['Razon Social'] = lines[0]  # Tomando la primera línea no vacía como suposición
    
    return data

def main():
    if not os.path.exists(INPUT_FOLDER):
        print(f"Error: La carpeta '{INPUT_FOLDER}' no existe.")
        return

    invoices_data = []
    
    files = [f for f in os.listdir(INPUT_FOLDER) if f.lower().endswith('.pdf')]
    if not files:
        print(f"No se encontraron archivos PDF en '{INPUT_FOLDER}'.")
        return

    print(f"Procesando {len(files)} facturas...")

    for filename in files:
        filepath = os.path.join(INPUT_FOLDER, filename)
        try:
            print(f"Leyendo: {filename}")
            invoice_info = extract_invoice_data(filepath)
            invoices_data.append(invoice_info)
        except Exception as e:
            print(f"Error procesando {filename}: {e}")

    if invoices_data:
        df = pd.DataFrame(invoices_data)
        
        # Asegurar que el directorio de salida existe (debería, pero seguridad primero)
        if not os.path.exists(OUTPUT_FOLDER):
            os.makedirs(OUTPUT_FOLDER)
            
        df.to_excel(OUTPUT_FILE, index=False)
        print(f"\n¡Éxito! Datos exportados a: {OUTPUT_FILE}")
        print(df)
    else:
        print("No se extrajeron datos.")

if __name__ == "__main__":
    main()
