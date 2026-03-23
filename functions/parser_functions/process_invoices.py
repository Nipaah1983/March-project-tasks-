def process_invoices(invoices):
    total_count = len(invoices)
    total_amount = 0.0
    by_currency = {}
    errors = []

    for idx, inv in enumerate(invoices):
        supplier = inv.get("supplier") or inv.get("supplier_name") or f"Инвойс {idx}"
        amount = inv.get("amount")
        currency = inv.get("currency")

        if currency:
            by_currency[currency] = by_currency.get(currency, 0) + 1
        if amount is None or amount <= 0:
            errors.append(f"Инвойс {idx} ({supplier}): amount <= 0")
            continue
        if currency not in ("EUR", "USD", "RUB"):
            errors.append(f"Инвойс {idx} ({supplier}): неожиданная валюта {currency}")
            continue
        total_amount += amount

    return {
        "total_count": total_count,
        "total_amount": total_amount,
        "by_currency": by_currency,
        "errors": errors,
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