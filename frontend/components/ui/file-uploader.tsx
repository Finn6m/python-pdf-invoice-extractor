"use client";

import { useRef, useState } from "react"
import { Button } from "./button"
import { extractInvoice } from "@/lib/api";
import { InvoiceData } from "@/types/invoice";

export const FileUploader = () => {
    const [selectedFile, setSelectedFile] = useState<File | null>(null);
    const [isLoading, setIsLoading] = useState<boolean | null>(null);
    const [extractedData, setExtractedData] = useState<InvoiceData | null>(null);

    const fileInputRef = useRef<HTMLInputElement>(null);
    const handleOnClick = () => {
        fileInputRef.current?.click()

    }
    async function handleFileChange(event: React.ChangeEvent<HTMLInputElement>) {
        const file = event.target.files?.[0];

        if (file) {
            const data = await extractInvoice(file)
            setExtractedData(data);
            setSelectedFile(file);
            console.log(file);
        }
    };
    return (
        <div className="flex flex-col p-5">
            <div className="flex flex-col items-center justify-center gap-4 w-full h-64 border border-dashed border-muted-foreground rounded-lg p-20">
                <h1 className="text-lg font-semibold">Upload a file</h1>
                <p className="text-muted-foreground text-sm">Any invoice submitted in PDF format</p>
                <input 
                    ref={fileInputRef}
                    type="file"
                    accept="application/pdf"
                    hidden
                    onChange={handleFileChange}
                />
                <Button variant="outline" onClick={handleOnClick}>Browse files</Button>
            </div>
            <div className="flex flex-col items-center justify-center p-20">
                <h1>Extracted data:</h1>
                <p>{extractedData?.invoice_number}</p>
                <p>{extractedData?.date}</p>
                <p>{extractedData?.total_amount}</p>
                <p>Items</p>
                {extractedData?.items.map((r, i) => (
                    <div key={i} className="flex gap-2">
                        <p>{r.description}</p>
                        <p>{r.price}</p>
                    </div>
                ))}
            </div>
        </div> 
    )
}