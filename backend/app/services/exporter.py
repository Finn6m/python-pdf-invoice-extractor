import pandas as pd

def export_to_excel(invoices, filename="invoices_db.xlsx"):
    df = pd.DataFrame(invoices)

    df.to_excel(
        filename,
        index=False
    )

    print(f"Excel file created: {filename}")