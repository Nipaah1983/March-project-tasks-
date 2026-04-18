import os
import pdfplumber
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("invoice-analyzer")

@mcp.tool()
def get_first_page_text(filepath: str) -> str:
    if not os.path.exists(filepath):
        return "Error: file not found"
    try:
        with pdfplumber.open(filepath) as pdf:
            return pdf.pages[0].extract_text() or ""
    except Exception as e:
        return f"Error: {e}"

@mcp.tool()
def get_word_count(filepath: str) -> int:
    text = get_first_page_text(filepath)
    if text.startswith("Error:"):
        return -1
    return len(text.split())

@mcp.tool()
def has_field(filepath: str, field: str) -> bool:
    text = get_first_page_text(filepath)
    if text.startswith("Error:"):
        return False
    return field.lower() in text.lower()

if __name__ == "__main__":
    folder = "test_invoices"

    for file in os.listdir(folder):
        if file.lower().endswith(".pdf"):
            path = os.path.join(folder, file)
            print(f"{file}")
            print(f"  Words: {get_word_count(path)}")
            print(f"  Has 'invoice': {has_field(path, 'invoice')}")
            print(f"  Has 'total': {has_field(path, 'total')}\n")