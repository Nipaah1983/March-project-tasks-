#A1
#3

#A2
#DEDIMAX

#A3
#[2, 3, 4]

#A4
#4

#A5
#1

#B6
suppliers = ["Max Mara", "Rinaldi"]
suppliers.append("IFD")

#B7
suppliers = ["Max Mara", "Rinaldi", "DEDIMAX"]
last = suppliers[-1]

#B8
amounts = [500, 1500, 2000, 800]
filtered = [a for a in amounts if a > 1000]

#B9
amounts = [1000, 1500, 2000]
total = sum(amounts)

#B10
list1 = [1, 2, 3]
list2 = list1[:]

#C11
invoices = [
    {"supplier_name": "Supplier A", "amount": 100.50, "currency": "EUR"},
    {"supplier_name": "Supplier B", "amount": 250.00, "currency": "USD"},
    {"supplier_name": "Supplier A", "amount": 150.20, "currency": "EUR"},
]
def get_suppliers(invoices):
    return [invoice["supplier_name"] for invoice in invoices]

#C12
def count_currency(invoices):
    currency_counts = {}
    for invoice in invoices:
        currency = invoice["currency"]
        currency_counts[currency] = currency_counts.get(currency, 0) + 1
    return currency_counts

#C13
def filter_by_amount(invoices, min_amount):
    return [invoice for invoice in invoices if invoice["amount"] >= min_amount]

#C14
def get_total_by_currency(invoices, currency):
    total = 0
    for invoice in invoices:
        if invoice["currency"] == currency:
            total += invoice["amount"]
    return total

#C15
def find_max_invoice(invoices):
    if not invoices:
        return None
    max_invoice = invoices[0]
    for invoice in invoices:
        if invoice["amount"] > max_invoice["amount"]:
            max_invoice = invoice
    return max_invoice

#D16
def get_suppliers(invoices):
    result = []
    for invoice in invoices:
        result.append(invoice["supplier_name"])
    return result

#D17
def calculate_total(invoices):
    total = 0
    for invoice in invoices:
        total += invoice["amount"]
    return total

#D18
def filter_eur(invoices):
    result = []
    for invoice in invoices:
        if invoice["currency"] == "EUR":
            result.append(invoice)
    return result

#E19
result = [invoice["amount"] for invoice in invoices]

#E20
result = [invoice for invoice in invoices if invoice["amount"] > 0]

#F21
def analyze_invoices(invoices):
    total_count = len(invoices)
    valid_count = 0
    total_amount = 0
    by_currency = {}
    max_amount = 0
    min_amount = float('inf')
    valid_amounts = []

    for invoice in invoices:
        if invoice["amount"] > 0:
            valid_count += 1
            total_amount += invoice["amount"]
            valid_amounts.append(invoice["amount"])

            currency = invoice["currency"]
            by_currency[currency] = by_currency.get(currency, 0) + 1

            if invoice["amount"] > max_amount:
                max_amount = invoice["amount"]

            if invoice["amount"] < min_amount:
                min_amount = invoice["amount"]

    if valid_count == 0:
        avg_amount = 0
        min_amount = 0
    else:
        avg_amount = total_amount / valid_count

    return {
        "total_count": total_count,
        "valid_count": valid_count,
        "total_amount": round(total_amount, 2),
        "by_currency": by_currency,
        "max_amount": max_amount,
        "min_amount": min_amount,
        "avg_amount": round(avg_amount, 2)
    }

#F22
def group_by_currency(invoices):
    grouped = {}
    for invoice in invoices:
        currency = invoice["currency"]
        if currency not in grouped:
            grouped[currency] = []
        grouped[currency].append(invoice)
    return grouped

#G23
#append() добавляет один элемент в конец списка. extend() добавляет все элементы объекта поэлементно.

#G24
#pop удаляет по индексу, remove по значению

#G25
#list2 = list1.copy()

#G26
#slice это типо подсписок какой-то ээээ 
#my_list[::2]

#G27
#При удалении/добавлении элементов индексы сдвигаются, из-за этого они могут быть обработаны дважды