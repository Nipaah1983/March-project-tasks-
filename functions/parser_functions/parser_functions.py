def extract_field(text, field_name):
    field_to_find = f"{field_name}:"
    start_index = text.find(field_to_find)
    if start_index == -1:
        return None
    
    value_start_index = start_index + len(field_to_find)
    end_index_newline = text.find('\n', value_start_index)

    if end_index_newline != -1:
        value = text[value_start_index:end_index_newline]
    else:
        value = text[value_start_index:]
    return value.strip()

def parse_amount(amount_string):
    try:
        cleaned_string = amount_string.replace(',', '')
        return float(cleaned_string)
    except ValueError:
        return None
    
def create_invoice_dict(supplier, amount, currency, date):
    return {
        "supplier": supplier,
        "amount": amount,
        "currency": currency,
        "date": date
    }

print("=== Тест extract_field ===")
text = "Supplier: Max Mara\nAmount: 1500"
print(extract_field(text, "Supplier"))
print(extract_field(text, "Amount"))
print("\n=== Тест parse_amount ===")
print(parse_amount("1500.50"))
print(parse_amount("1,500.50"))
print(parse_amount("abc"))
print("\n=== Тест create_invoice_dict ===")
invoice = create_invoice_dict("Max Mara", 1500.0, "EUR", "15.03.2024")
print(invoice)