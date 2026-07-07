import pandas as pd


def export_to_excel(invoices, filename="invoices_db.xlsx"):

    invoice_rows = []
    item_rows = []


    for invoice in invoices:

        invoice_rows.append({
            "invoice_number": invoice["invoice_number"],
            "date": invoice["date"],
            "total_amount": invoice["total_amount"]
        })


        for item in invoice["items"]:

            item_rows.append({
                "invoice_number": invoice["invoice_number"],
                "description": item["description"],
                "price": item["price"]
            })


    invoices_df = pd.DataFrame(invoice_rows)
    items_df = pd.DataFrame(item_rows)


    with pd.ExcelWriter(filename) as writer:

        invoices_df.to_excel(
            writer,
            sheet_name="Invoices",
            index=False
        )

        items_df.to_excel(
            writer,
            sheet_name="Items",
            index=False
        )


    print(f"Created {filename}")