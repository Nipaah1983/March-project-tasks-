import os
import pdfplumber
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("invoice-validator")

REQUIRED_FIELDS = {
    "supplier": ["supplier", "vendor", "company", "To:", "Поставщик"],
    "amount": ["amount", "total", "sum", "price"],
    "date": ["date", "invoice date", "issued"],
    "number": ["invoice number", "ref", "no."],
}

@mcp.tool()
def validate_invoice(filepath: str) -> dict:
    if not os.path.exists(filepath):
        return {"valid": False, "fields": {}, "errors": ["File not found"]}

    try:
        with pdfplumber.open(filepath) as pdf:
            text = (pdf.pages[0].extract_text() or "").lower()
    except Exception as e:
        return {"valid": False, "fields": {}, "errors": [str(e)]}

    fields = {}
    errors = []

    for field, keywords in REQUIRED_FIELDS.items():
        found = any(kw in text for kw in keywords)
        fields[field] = found
        if not found:
            errors.append(f"Missing: {field}")

    return {"valid": len(errors) == 0, "fields": fields, "errors": errors}

if __name__ == "__main__":
    folder = "test_invoices"

    for file in os.listdir(folder):
        if file.lower().endswith(".pdf"):
            path = os.path.join(folder, file)
            result = validate_invoice(path)
            print(f"{file}")
            print(f"  Valid: {result['valid']}")
            print(f"  Fields: {result['fields']}")
            if result["errors"]:
                print(f"  Errors: {result['errors']}")
            print()