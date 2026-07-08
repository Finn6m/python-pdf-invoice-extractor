export type InvoiceItems = {
    description: string,
    price: number
}

export type InvoiceData = {
    invoice_number: string,
    date: string,
    total_amount: number,
    items: InvoiceItems[],
}
