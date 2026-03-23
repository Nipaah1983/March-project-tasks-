invoice = {
"supplier_name": "ABC Fashion GmbH",
"amount": 1250.50
}
currency = invoice.get("currency", "EUR")
print(f"Валюта: {currency}")
payment_terms = invoice.get("payment_terms")
print(f"Условия оплаты: {payment_terms}")