def get_suppliers(invoices):
    return [inv["supplier"] for inv in invoices]


def count_by_currency(invoices):
    by_currency = {}
    for invoice in invoices:
        currency = invoice.get("currency", "UNKNOWN")
        by_currency[currency] = by_currency.get(currency, 0) + 1
    return by_currency


def filter_valid_invoices(invoices):
    return [inv for inv in invoices if inv.get("amount", 0) > 0]


def get_total_by_currency(invoices, currency):
    return sum(inv["amount"] for inv in invoices if inv.get("currency") == currency)


def find_max_invoice(invoices):
    if not invoices:
        return None
    return max(invoices, key=lambda x: x.get("amount", 0))


invoices = [
    {"supplier": "Max Mara", "amount": 1500, "currency": "EUR"},
    {"supplier": "Rinaldi", "amount": 0, "currency": "USD"},
    {"supplier": "DEDIMAX", "amount": 1800, "currency": "EUR"},
    {"supplier": "Coccinelle", "amount": 500, "currency": "GBP"},
    {"supplier": "IFD", "amount": 1200, "currency": "USD"},
]

print("=== Тест get_suppliers ===")
print(get_suppliers(invoices))

print("\n=== Тест count_by_currency ===")
print(count_by_currency(invoices))

print("\n=== Тест filter_valid_invoices ===")
print(filter_valid_invoices(invoices))

print("\n=== Тест get_total_by_currency ===")
print(f"EUR: {get_total_by_currency(invoices, 'EUR')}")
print(f"USD: {get_total_by_currency(invoices, 'USD')}")

print("\n=== Тест find_max_invoice ===")
print(find_max_invoice(invoices))