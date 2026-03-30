from invoice_parser import process_invoices

invoices = [
    {"supplier": "Max Mara", "amount": 1500, "currency": "EUR"},
    {"supplier": "Rinaldi", "amount": 0, "currency": "USD"},
    {"supplier": "DEDIMAX", "amount": 1800, "currency": "EUR"},
    {"supplier": "Coccinelle", "amount": 500, "currency": "GBP"},
    {"supplier": "IFD", "amount": 1200, "currency": "USD"},
    {"supplier": "Slam Jam", "amount": 2500, "currency": "EUR"},
    {"amount": 1000, "currency": "EUR"},
    {"supplier": "Brand X", "amount": -100, "currency": "EUR"},
]
result = process_invoices(invoices)

print("=== РЕЗУЛЬТАТЫ ОБРАБОТКИ ===\n")
print(f"Всего инвойсов: {result['total_count']}")
print(f"Валидных: {result['valid_count']}")
print(f"Невалидных: {result['invalid_count']}")
print(f"Общая сумма: {result['total_amount']}")
print(f"\nПо валютам: {result['by_currency']}")
print(f"\nОшибки ({len(result['errors'])}):")
for error in result["errors"]:
    print(f"  ❌ {error}")
print(f"\nВалидные инвойсы ({len(result['valid_invoices'])}):")
for inv in result["valid_invoices"]:
    print(f"  ✅ {inv['supplier']}: {inv['amount']} {inv['currency']}")