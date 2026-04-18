import os
from datetime import datetime
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("invoice-counter")

@mcp.tool()
def count_invoices(directory: str) -> int:
    if not os.path.exists(directory):
        raise ValueError(f"Directory not found: {directory}")

    count = 0
    for filename in os.listdir(directory):
        if filename.lower().endswith(".pdf"):
            count += 1
    return count

if __name__ == "__main__":
    test_directory = "test_invoices"
    try:
        result = count_invoices(test_directory)
        print(f"\nFound {result} PDF file(s) in '{test_directory}'")
    except ValueError as e:
        print(f"Error: {e}")

@mcp.tool()
def get_supplier_name(filepath: str) -> str:
    filename = os.path.basename(filepath)
    name = filename.lower().replace(".pdf", "")
    parts = name.split()

    supplier_parts = []
    for part in parts:
        if any(char.isdigit() for char in part):
            break
        supplier_parts.append(part)

    return " ".join(supplier_parts)

@mcp.tool()
def get_file_info(filepath: str) -> dict:
    """Returns file size and modification date."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    size_bytes = os.path.getsize(filepath)
    mod_time = os.path.getmtime(filepath)
    modified = datetime.fromtimestamp(mod_time).strftime("%Y-%m-%d %H:%M:%S")

    return {
        "size_bytes": size_bytes,
        "size_kb": round(size_bytes / 1024, 2),
        "modified": modified
    }

if __name__ == "__main__":
    folder = "test_invoices"

    print(f"PDF count: {count_invoices(folder)}\n")

    for file in os.listdir(folder):
        if file.lower().endswith(".pdf"):
            filepath = os.path.join(folder, file)
            supplier = get_supplier_name(file)
            info = get_file_info(filepath)
            print(f"{file}")
            print(f"  Supplier: {supplier}")
            print(f"  Size: {info['size_kb']} KB")
            print(f"  Modified: {info['modified']}\n")