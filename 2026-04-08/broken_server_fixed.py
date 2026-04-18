import os
import pdfplumber
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("broken-invoice-server-fixed")

@mcp.tool()
def read_invoice(path: str) -> str:
    if not os.path.exists(path):
        return "Error: file not found"
    try:
        with pdfplumber.open(path) as pdf:
            if not pdf.pages:
                return "Error: no pages"
            return pdf.pages[0].extract_text() or ""
    except Exception as e:
        return f"Error: {e}"

@mcp.tool()
def count_pdfs(directory: str) -> int:
    if not os.path.isdir(directory):
        return 0
    files = os.listdir(directory)
    return len([f for f in files if f.lower().endswith(".pdf")])

@mcp.tool()
def get_supplier(filepath: str) -> str:
    name = os.path.splitext(os.path.basename(filepath))[0]
    if "_" in name:
        return name.split("_")[0].upper()
    return name.upper()

@mcp.tool()
def read_pdf_text(path: str) -> str:
    if not os.path.exists(path):
        return "Error: file not found"
    try:
        with pdfplumber.open(path) as pdf:
            if not pdf.pages:
                return "Error: no pages"
            return pdf.pages[0].extract_text() or ""
    except Exception as e:
        return f"Error: {e}"