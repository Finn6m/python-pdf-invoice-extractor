schema = {
    "type": "OBJECT",
    "properties": {
        "invoice_number": {"type": "STRING"},
        "date": {"type": "STRING"},
        "total_amount": {"type": "NUMBER"},
        "items": {
            "type": "ARRAY",
            "items": {
                "type": "OBJECT",
                "properties": {
                    "description": {"type": "STRING"},
                    "price": {"type": "NUMBER"},
                },
            },
        },
    },
    "required": ["invoice_number", "date",
                 "total_amount", "items"],
}