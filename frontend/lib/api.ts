import { InvoiceData } from "@/types/invoice";

const BASE_URL = "http://localhost:8000";

export async function extractInvoice(file: File): Promise<InvoiceData> {
    const formData = new FormData();
    formData.append("file", file)

    const response = await fetch(`${BASE_URL}/extract`, {
        method: "POST",
        body: formData,
    });

    if (!response.ok) {
        throw new Error("Failed to extract the uploaded PDF");
    }

    return response.json();
}
