def validate_invoice(invoice: dict) -> list:
    errors: list = []
    
    required = ["supplier_name", "amount", "currency", "date_issued", "invoice_number"]
    for key in required:
        if invoice.get(key) in (None, ""):
            errors.append(f"Отсутствует или пустое обязательное поле: {key}")

    amount = invoice.get("amount")
    if not isinstance(amount, (int, float)):
        errors.append("Поле 'amount' должно быть числом (int или float)")
    elif amount <= 0:
        errors.append("Поле 'amount' должно быть больше нуля")

    currency = invoice.get("currency")
    allowed_currencies = ("EUR", "USD", "RUB")
    if currency not in allowed_currencies:
        errors.append(f"Недопустимая валюта: '{currency}'. Допустимые: {', '.join(allowed_currencies)}")

    date_issued = invoice.get("date_issued")
    if date_issued is None or (isinstance(date_issued, str) and len(date_issued) < 8):
        errors.append(f"Некорректный формат даты: '{date_issued}'. Ожидается формат DD.MM.YYYY.")

    invoice_number = invoice.get("invoice_number")
    if isinstance(invoice_number, str) and len(invoice_number) < 3:
        errors.append(f"Некорректный номер инвойса: '{invoice_number}'. Номер должен быть не короче 3 символов.")

    return errors

invoice_ok = {
    "supplier_name": "Marina Rinaldi",
    "amount": 1230.3,
    "currency": "EUR",
    "date_issued": "02.10.2023",
    "invoice_number": "FA 02736",
}
invoice_bad = {
    "supplier_name": "",
    "amount": -5,
    "currency": "ABC",
    "date_issued": None,
    "invoice_number": None,
}
print(validate_invoice(invoice_ok))
print(validate_invoice(invoice_bad))