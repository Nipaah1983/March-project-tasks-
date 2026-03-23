#A1
#Выводит умножение 0*2 1*2 и 2*2

#A2
#Выводит названия файлов в верхнем регистре

#A3
#Печатает сумму, 600

#A4
#Печатает значения 0, 1, 2, 3 по одному на каждой строке

#A5
#Печатает 0, 1, 2

#B6
invoice = {"supplier": "MaxMara", "amount": 1500}
for key in invoice:
    print(key)

#B7
invoices = [{"amount": 100}, {"amount": 200}, {"amount": 300}]
total = 0
for inv in invoices:
    total += inv["amount"]
print(total)

#B8
invoices = [{"amount": 100}, {"amount": 0}, {"amount": 200}]
for inv in invoices:
    if inv["amount"] == 0:
        continue
    print(inv["amount"])

#B9
invoice = {"supplier": "MaxMara", "amount": 1500}
for key in invoice:
    print(f"{key}: {invoice[key]}")

#B10
invoice = {"supplier": "MaxMara", "amount": 1500}
for key, value in invoice.items():
    print(f"{key}: {value}")

#C11
for i in range(1, 11):
    print(i)

#C12
for cur in ["EUR", "USD", "RUB"]:
    print(cur)

#C13
invoices = [
    {"currency": "EUR"},
    {"currency": "USD"},
    {"currency": "EUR"},
]
count = 0
for inv in invoices:
    if inv.get("currency") == "EUR":
        count += 1
print(count)

#C14
for i in range(0, 21):
    if i % 2 == 0:
        print(i)

#C15
def sum_amounts(invoices):
    total = 0
    for inv in invoices:
        total += inv.get("amount", 0)
    return total

#D16
i = 0
while i < 3:
    print(i)
    i += 1

#D17
items = ["a", "b", "c"]
for i in range(len(items)):
    if i == 1:
        break
    print(items[i])

#D18
invoices = [{"amount": 100}, {"amount": 0}, {"amount": 200}]
total = 0
for inv in invoices:
    if inv["amount"] == 0:
        continue
    total += inv["amount"]
print(total)

#D19
invoice = {"supplier": "MaxMara", "amount": 1500}
for key, value in invoice.items():
    print(f"{key}: {value}")

#E20
invoice = {"supplier": "MaxMara", "amount": 1500}
for key, value in invoice.items():
    print(f"{key}: {value}")

#E21
for i in range(5):
    print(i)

#E22
for i in range(10):
    if i % 2 != 0:
        print(i)

#F23
invoices = [
    {"supplier": "A", "amount": 1200, "currency": "EUR"},
    {"supplier": "B", "amount": 900, "currency": "EUR"},
    {"supplier": "C", "amount": 1500, "currency": "USD"},
]
for inv in invoices:
    if inv.get("amount", 0) > 1000 and inv.get("currency") == "EUR":
        print(inv)

#F24
invoices = [
    {"currency": "EUR"},
    {"currency": "USD"},
    {"currency": "EUR"},
    {"currency": "RUB"},
    {"currency": "EUR"},
]
counts = {"EUR": 0, "USD": 0, "RUB": 0}
for inv in invoices:
    cur = inv.get("currency")
    if cur in counts:
        counts[cur] += 1
print(f"EUR: {counts['EUR']}, USD: {counts['USD']}, RUB: {counts['RUB']}")

#F25
def validate_all(invoices):
    errors = []
    for idx, inv in enumerate(invoices):
        if not inv.get("supplier_name"):
            errors.append(f"Инвойс {idx}: нет поля supplier_name")
        if inv.get("amount") is None:
            errors.append(f"Инвойс {idx}: нет поля amount")
        if not inv.get("currency"):
            errors.append(f"Инвойс {idx}: нет поля currency")
    return errors
invoices = [
    {"supplier_name": "MaxMara", "amount": 1500, "currency": "EUR"},
    {"supplier_name": "", "amount": 200, "currency": "USD"},
    {"supplier_name": "Acme", "amount": None, "currency": "RUB"},
]
print(validate_all(invoices))