import os
import json
import base64
from pathlib import Path

from anthropic import Anthropic
from dotenv import load_dotenv

from app.models.schemas import schema


load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    raise ValueError("ANTHROPIC_API_KEY not found")

client = Anthropic(
    api_key=api_key
)



#TODO: when FastAPI post route is set up, add pdf_path as a param
def extract_invoice(pdf_path: Path):
     
    print(f"Processing {pdf_path.name}...")

    pdf_data = base64.b64encode(
        pdf_path.read_bytes()
    ).decode("utf-8")


    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=4096,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "document",
                        "source": {
                            "type": "base64",
                            "media_type": "application/pdf",
                            "data": pdf_data
                        }
                    },
                    {
                        "type": "text",
                        "text": f"""
                                Extract the invoice information.

                                Return ONLY valid JSON.

                                Use this schema:

                                {json.dumps(schema)}
                                """
                        }
                    ]
                }
            ]
        )
    

    invoice_json = response.content[0].text

    #get rid of code fences from claudes response so that json.loads() doesnt fail
    invoice_json = invoice_json.replace("```json", "")
    invoice_json = invoice_json.replace("```", "")
    invoice_json = invoice_json.strip()

    try:
        invoice_data = json.loads(invoice_json)
        return invoice_data

    except json.JSONDecodeError:
        print(f"Could not parse {pdf_path.name}")
        return None
