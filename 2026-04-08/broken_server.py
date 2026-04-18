from mcp.server.fastmcp import FastMCP
import pdfplumber
import os

mcp = FastMCP("broken-invoice-server")

@mcp.tool()
def read_invoice(path):
    with open(path) as f:
        content = f.read()
        return content

@mcp.tool()
def count_pdfs(directory: str) -> int:
    files = os.listdir(directory)
    pdfs = [f for f in files if f.endswith('.pdf')]
    return len(pdfs)

@mcp.tool()
def get_supplier(filepath: str) -> str:
    name = os.path.basename(filepath)
    parts = name.split('_')
    return parts[0].upper()

@mcp.tool()
def read_pdf_text(path: str) -> str:
    pdf = pdfplumber.open(path)
    return pdf.pages[0].text