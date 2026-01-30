from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def create_invoice(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    # Header
    c.setFont("Helvetica-Bold", 20)
    c.drawString(50, 750, "EMPRESA EJEMPLO S.A.")
    
    # Invoice Details
    c.setFont("Helvetica", 12)
    c.drawString(50, 720, "R.F.C.: ABC123456T1A")
    c.drawString(50, 705, "Dirección: Calle Falsa 123, Ciudad")
    
    c.setFont("Helvetica-Bold", 14)
    c.drawString(400, 750, "FACTURA")
    c.setFont("Helvetica", 12)
    c.drawString(400, 730, "Factura No: A-1001")
    c.drawString(400, 715, "Fecha: 30/01/2026")
    
    # Table Header
    y = 650
    c.line(50, y+5, 550, y+5)
    c.drawString(50, y+10, "Descripción")
    c.drawString(450, y+10, "Importe")
    c.line(50, y+25, 550, y+25)
    
    # Items
    items = [
        ("Servicio de Consultoría", "1000.00"),
        ("Desarrollo de Software", "2500.50"),
        ("Mantenimiento", "500.00")
    ]
    
    for desc, amount in items:
        c.drawString(50, y, desc)
        c.drawString(450, y, f"${amount}")
        y -= 20
        
    y -= 20
    c.line(50, y, 550, y)
    y -= 20
    
    # Totals
    c.drawString(350, y, "Subtotal:")
    c.drawString(450, y, "$4000.50")
    y -= 20
    c.drawString(350, y, "IVA (16%):")
    c.drawString(450, y, "$640.08")
    y -= 20
    c.setFont("Helvetica-Bold", 14)
    c.drawString(350, y, "Total:")
    c.drawString(450, y, "$4640.58")
    
    c.save()

if __name__ == "__main__":
    if not os.path.exists('input_invoices'):
        os.makedirs('input_invoices')
    create_invoice('input_invoices/factura_prueba.pdf')
    print("Factura de prueba creada.")
