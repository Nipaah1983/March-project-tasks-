def analyze_invoices(invoices):
    valid = [inv for inv in invoices if inv.get("amount", 0) > 0]

    total_count = len(invoices)
    valid_count = len(valid)
    total_amount = sum(inv["amount"] for inv in valid)
    avg_amount = total_amount / valid_count if valid_count > 0 else 0
    max_invoice = max(valid, key=lambda x: x["amount"]) if valid else None
    min_invoice = min(valid, key=lambda x: x["amount"]) if valid else None
    by_currency = {}
    for inv in valid:
        curr = inv.get("currency", "UNKNOWN")
        if curr not in by_currency:
            by_currency[curr] = {"count": 0, "total": 0}
        by_currency[curr]["count"] += 1
        by_currency[curr]["total"] += inv["amount"]

    return {
        "total_count": total_count,
        "valid_count": valid_count,
        "invalid_count": total_count - valid_count,
        "total_amount": total_amount,
        "avg_amount": avg_amount,
        "max_invoice": max_invoice,
        "min_invoice": min_invoice,
        "by_currency": by_currency,
    }

invoices = [
    {"supplier": "Max Mara", "amount": 1500, "currency": "EUR"},
    {"supplier": "Rinaldi", "amount": 0, "currency": "USD"},
    {"supplier": "DEDIMAX", "amount": 1800, "currency": "EUR"},
    {"supplier": "Coccinelle", "amount": 500, "currency": "GBP"},
    {"supplier": "IFD", "amount": 1200, "currency": "USD"},
    {"supplier": "Slam Jam", "amount": 2500, "currency": "EUR"},
]
stats = analyze_invoices(invoices)

print("=== СТАТИСТИКА ПО ИНВОЙСАМ ===\n")
print(f"Всего инвойсов: {stats['total_count']}")
print(f"Валидных: {stats['valid_count']}")
print(f"Невалидных: {stats['invalid_count']}")
print(f"Общая сумма: {stats['total_amount']}")
print(f"Средняя сумма: {stats['avg_amount']:.2f}")
print(f"Максимальный: {stats['max_invoice']}")
print(f"Минимальный: {stats['min_invoice']}")
print("\n=== ПО ВАЛЮТАМ ===")

for currency, data in stats["by_currency"].items():
    print(f"{currency}: {data['count']} инв., сумма {data['total']}")