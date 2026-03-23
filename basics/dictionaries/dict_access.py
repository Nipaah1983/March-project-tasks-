invoice = {
"supplier_name": "Marina Rinaldi",
"amount": 1230.3,
"currency": "EUR",
"quantity": 6,
"date_issued": "02.10.2023",
"invoice_number": "FA 02736"
}
print(f"Поставщик: {invoice['supplier_name']}")
print(f"Сумма: {invoice['amount']} {invoice['currency']}")
vat_rate = 0.20
total_with_vat = round(invoice['amount'] * (1 + vat_rate), 2)
print(f"С НДС: {total_with_vat} {invoice['currency']}")