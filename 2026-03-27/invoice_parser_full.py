from typing import Dict, List, Any

def validate_invoice(invoice: Dict[str, Any], index: int) -> List[str]:
    errors = []

    if "supplier" not in invoice:
        errors.append(f"Invoice {index}: missing supplier field")
    elif not isinstance(invoice["supplier"], str):
        errors.append(f"Invoice {index}: supplier must be a string")

    if "amount" not in invoice:
        errors.append(f"Invoice {index}: missing amount field")
    elif not isinstance(invoice["amount"], (int, float)):
        errors.append(f"Invoice {index}: amount must be a number")
    elif invoice["amount"] <= 0:
        errors.append(f"Invoice {index}: amount <= 0")

    if "currency" not in invoice:
        errors.append(f"Invoice {index}: missing currency field")
    elif invoice["currency"] not in ["EUR", "USD", "RUB"]:
        errors.append(f"Invoice {index}: invalid currency")
        
    return errors

def process_invoices(invoices: List[Dict[str, Any]]) -> Dict[str, Any]:
    total_count = len(invoices)
    valid_invoices = []
    all_errors = []

    for idx, invoice in enumerate(invoices):
        invoice_errors = validate_invoice(invoice, idx)
        if invoice_errors:
            all_errors.extend(invoice_errors)
        else:
            valid_invoices.append(invoice)
    total_amount = sum(inv["amount"] for inv in valid_invoices)
    
    by_currency = {}
    for inv in valid_invoices:
        curr = inv.get("currency", "UNKNOWN")
        if curr not in by_currency:
            by_currency[curr] = {"count": 0, "total": 0}
        by_currency[curr]["count"] += 1
        by_currency[curr]["total"] += inv["amount"]

    return {
        "total_count": total_count,
        "valid_count": len(valid_invoices),
        "invalid_count": total_count - len(valid_invoices),
        "total_amount": total_amount,
        "by_currency": by_currency,
        "errors": all_errors,
        "valid_invoices": valid_invoices,
    }

invoices = [
    {"supplier": "Max Mara", "amount": 1500, "currency": "EUR"},
    {"supplier": "Rinaldi", "amount": 0, "currency": "USD"},
    {"supplier": "DEDIMAX", "amount": 1800, "currency": "EUR"},
    {"supplier": "Coccinelle", "amount": 500, "currency": "GBP"},
    {"supplier": "IFD", "amount": 1200, "currency": "USD"},
    {"supplier": "Slam Jam", "amount": 2500, "currency": "EUR"},
    {"supplier": "Brand X", "amount": -100, "currency": "EUR"},
    {"amount": 1000, "currency": "EUR"},
    {"supplier": 123, "amount": 500, "currency": "USD"},
]
result = process_invoices(invoices)

print("=== РЕЗУЛЬТАТЫ ОБРАБОТКИ ===\n")
print(f"Всего инвойсов: {result['total_count']}")
print(f"Валидных: {result['valid_count']}")
print(f"Невалидных: {result['invalid_count']}")
print(f"Общая сумма: {result['total_amount']}")
print(f"\nПо валютам (только валидные):")
if not result['by_currency']:
    print("  Нет данных")
else:
    for currency, data in result['by_currency'].items():
        print(f"  {currency}: {data['count']} инв., сумма {data['total']}")

print("\nОшибки:")
if not result['errors']:
    print("  Нет ошибок")
else:
    for error in result['errors']:
        print(f"  - {error}")

print("\nВалидные инвойсы:")
if not result['valid_invoices']:
    print("  Нет валидных инвойсов")
else:
    for inv in result['valid_invoices']:
        print(f"  ✓ {inv.get('supplier', 'N/A')}: {inv.get('amount', 'N/A')} {inv.get('currency', 'N/A')}")