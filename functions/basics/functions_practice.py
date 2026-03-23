#A1
#Выводит результат x * 2

#A2
#Выводит Hello, Max

#A3
#Выводит True

#A4
#Возвращает 30 и присваивает это значение result

#A5
#Всегда возвращает EUR, присваивает это значение curr

#B6
def add(a, b):
    return a + b

#B7
def is_eur(currency):
    return currency == "EUR"

#B8
def calculate_vat(amount):
    return amount * 0.20

#B9
def count_items(items):
    return len(items)

#B10
def get_first(items):
    return items[0]

#C11
def multiply(a, b):
    return a * b

#C12
def is_positive(x):
    return x > 0

#C13
def get_supplier_name(invoice):
    return invoice["supplier"]

#C14
def format_currency(amount, currency):
    return f"{amount} {currency}"

#C15
def count_eur_invoices(invoices):
    count = 0
    for invoice in invoices:
        if invoice.get("currency") == "EUR":
            count += 1
    return count

#D16
def add(a, b):
    return a + b
result = add(5, 5)

#D17
def get_supplier(invoice):
    return invoice["supplier"]

#D18
def is_valid(amount):
    if amount > 0:
        return True
    
#D19
def calculate_total(amount):
    vat = amount * 0.20
    total = amount + vat
    return total
    
#E20
result = 5 * 2

#E21
def calculate_total_with_vat(amount):
    vat = amount * 0.20
    total = amount + vat
    return total
amount = 1000
total = calculate_total_with_vat(amount)

#E22
def calculate_vat(amount):
    return amount * 0.20
def calculate_total(amount, vat_amount):
    return amount + vat_amount
amount = 1000
vat = calculate_vat(amount)
total = calculate_total(amount, vat)

#F23
def validate_invoice(invoice):
    errors = []
    required_fields = ["supplier", "amount", "currency"]
    for field in required_fields:
        if field not in invoice:
            errors.append(f"Missing field: {field}")
    if "amount" in invoice and invoice["amount"] <= 0:
        errors.append("Amount must be greater than 0")
    return errors

#F24
def extract_supplier(text):
    if ":" in text:
        return text.split(":", 1)[1].strip()
    return ""

#F25
# . . . .

#G26
#print выводит значение но никуда его не передаёт, return возвращает значение после чего его можно присвоить переменной

#G27
#Документация которая описывает что делает функция

#G28
#Это значение параметра, которое используется, если аргумент не передан при вызове
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"

#G29
#Это зона где доступна переменная, локальные переменные создаются при вызове функции и удаляются после завершения

#G30
#Чтобы не копировать один и тот же код, также упращает этап тестирования