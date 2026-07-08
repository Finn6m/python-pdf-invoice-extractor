from app.services.extractor import extract_invoice
from app.services.exporter import export_to_excel


invoices = extract_invoice()

print(invoices)

export_to_excel(invoices)