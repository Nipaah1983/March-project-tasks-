date = "13-09-2023"
number = "3A00003107"

code = 23640723
name = "DATABILE"
description = "SWEATER"
currency = "EUR"
custom_tariff = 61101190
net_weight = 0.925
total_pieces = 4
unit_price = 74.40
amount = 297.60
discount = None
net_amount = 297.60

print(type(date))
print(type(net_weight))
print(type(net_amount))
print(type(discount))

vat_rate = 0.20
total = round(amount * (1 + vat_rate), 2)
print(f"Итого с НДС: {total:.2f} {currency}")