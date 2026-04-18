import os
import pdfplumber
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("batch-processor")

@mcp.tool()
def process_all(directory: str) -> list[dict]:
    results = []
    for filename in os.listdir(directory):
        if not filename.lower().endswith(".pdf"):
            continue
        filepath = os.path.join(directory, filename)
        try:
            size_kb = round(os.path.getsize(filepath) / 1024, 2)
            with pdfplumber.open(filepath) as pdf:
                text = (pdf.pages[0].extract_text() or "").lower()
            words = len(text.split())

            name = filename.replace(".pdf", "").replace(".PDF", "")
            parts = name.split()
            supplier_parts = []
            for part in parts:
                if any(c.isdigit() for c in part):
                    break
                supplier_parts.append(part)
            supplier = " ".join(supplier_parts).lower()

            results.append({
                "file": filename,
                "supplier": supplier,
                "words": words,
                "size_kb": size_kb,
            })
        except Exception as e:
            results.append({"file": filename, "error": str(e)})
    return results

if __name__ == "__main__":
    folder = "test_invoices"
    for item in process_all(folder):
        if "error" in item:
            print(f"{item['file']} -> ERROR: {item['error']}")
        else:
            print(f"{item['file']}")
            print(f"  Supplier: {item['supplier']}")
            print(f"  Words: {item['words']}")
            print(f"  Size: {item['size_kb']} KB")
        print()