def is_valid_amount(amount):
    return amount > 0

def is_valid_currency(currency):
    allowed = ["EUR", "USD", "RUB"]
    return currency in allowed

def validate_invoice(invoice, index):
    errors = []
    supplier = invoice.get("supplier") or invoice.get("supplier_name") or f"Инвойс {index}"
    amount = invoice.get("amount")
    if not is_valid_amount(amount):
        errors.append(f"Инвойс {index} ({supplier}): amount <= 0")
    currency = invoice.get("currency")
    if not is_valid_currency(currency):
        errors.append(f"Инвойс {index} ({supplier}): неожиданная валюта {currency}")
    return errors

def count_by_currency(invoices):
    by_currency = {}
    for invoice in invoices:
        currency = invoice.get("currency")
    if currency:
        by_currency[currency] = by_currency.get(currency, 0) + 1
    return by_currency

def calculate_total_amount(invoices):
    total = 0.0
    for invoice in invoices:
        amount = invoice.get("amount")
    if is_valid_amount(amount):
        total += amount
    return total

def process_invoices(invoices):
    total_count = len(invoices)
    total_amount = calculate_total_amount(invoices)
    by_currency = count_by_currency(invoices)
    errors = []
    for idx, invoice in enumerate(invoices):
        invoice_errors = validate_invoice(invoice, idx)
        errors.extend(invoice_errors)
    return {
    "total_count": total_count,
    "total_amount": total_amount,
    "by_currency": by_currency,
    "errors": errors
    }

invoices = [
    {"supplier": "MaxMara", "amount": 1500.0, "currency": "EUR"},
    {"supplier": "Rinaldi", "amount": 0, "currency": "USD"},
    {"supplier": "DEDIMAX", "amount": 2000.0, "currency": "EUR"},
    {"supplier": "Coccinelle", "amount": 500.0, "currency": "GBP"},
    {"supplier": "IFD", "amount": 1200.0, "currency": "USD"},
]
result = process_invoices(invoices)
print(result)