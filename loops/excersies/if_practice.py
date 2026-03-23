#A1
#A

#A2
#доллар

#A3
#Нет

#A4
#{"currency": "EUR", "amount": 0}

#A5
#не оплачен

#B6
amount = 10
if amount > 0:
    print("OK")

#B7
currency = "USD"
if currency == "EUR":
    print("EUR")
elif currency == "USD":
    print("USD")
else:
    print("OTHER")

#B8
invoice = {"supplier_name": "ABC"}
if "invoice_number" in invoice:
    print(invoice["invoice_number"])
else:
    print("Нет номера инвойса")

#B9
invoice = {"amount": 100}
currency = invoice.get("currency", "EUR")
print(currency)

#B10
amount = 100
currency = "EUR"
if amount > 0 and currency == "EUR":
    print("OK")

#B11
x = 5
if x == 5:
    print("равно")

#C12
invoice = {"supplier_name": "ABC", "delivery_address": ""}
if not invoice.get("delivery_address"):
    print("нет адреса доставки")

#C13
invoice = {"amount": 100}
if "currency" not in invoice or not invoice["currency"]:
    invoice["currency"] = "EUR"
print(invoice)

#C14
amount = 750
if amount < 1000:
    print("маленький инвойс")
else:
    print("крупный инвойс")

#C15
def is_invoice_complete(invoice):
    required = ["supplier_name", "amount", "currency"]
    return all(key in invoice and invoice[key] is not None for key in required)
print(is_invoice_complete({"supplier_name": "ABC", "amount": 100, "currency": "EUR"}))
print(is_invoice_complete({"supplier_name": "ABC", "amount": 100}))

#C16
def normalize_currency(currency):
    if currency == "€":
        return "EUR"
    if currency == "$":
        return "USD"
    return currency
print(normalize_currency("€"))
print(normalize_currency("$"))
print(normalize_currency("GBP"))

#C17
def vat_amount(amount, vat_rate):
    if amount is None:
        return None
    return round(amount * vat_rate, 2)
print(vat_amount(100, 0.2))
print(vat_amount(None, 0.2))

#D18
amount = 10
if amount > 0:
    print("OK")

#D19
invoice = {"amount": 100}
print(invoice.get("currency", "нет"))

#D20
currency = "EUR"
if currency == "EUR":
    print("OK")
elif currency == "USD":
    print("USD")
elif currency == "RUB":
    print("RUB")
else:
    print("OTHER")

#D21
invoice = {"amount": 0}
if invoice.get("amount") is None:
    print("amount отсутствует")
else:
    print("amount есть")

#D22
invoice = {"amount": "123"}
amount = invoice.get("amount")
if isinstance(amount, (int, float)):
    print("число")
else:
    print("не число")

#D23
invoice = {"amount": 100, "currency": "EUR"}
amt = invoice.get("amount")
cur = invoice.get("currency")
if isinstance(amt, (int, float)) and amt > 0 and cur == "EUR":
    print("OK")
else:
    print("BAD")

#D24
currency = None
if currency is None:
    print("нет")
else:
    print("есть")