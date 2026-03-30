from typing import Dict, List, Any
from .validators import validate_invoice


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
        curr = inv["currency"]
        by_currency[curr] = by_currency.get(curr, 0) + 1

    return {
        "total_count": total_count,
        "valid_count": len(valid_invoices),
        "invalid_count": total_count - len(valid_invoices),
        "total_amount": total_amount,
        "by_currency": by_currency,
        "errors": all_errors,
        "valid_invoices": valid_invoices,
    }