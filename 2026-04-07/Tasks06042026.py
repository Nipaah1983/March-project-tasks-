#A1
#ошибка типа
#конец

#A2
#делим на ноль
#cleanup
#ZeroDivisionError: division by zero

#A3
#KeyError: 'date'

#A4
#except будет ловить любую ошибку, но делать ничего с ней не будет

#A5
# 0

#B6
def read_invoice(path):
    try:
        with open(path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return None
    
#B7
def parse_amount(text):
    try:
        return float(text.replace(",", "").replace(" ", ""))
    except ValueError:
        return 0.0
    
#B8
REQUIRED_FIELDS = ["supplier", "amount", "date", "currency"]

def validate_invoice(data):
    missing = [field for field in REQUIRED_FIELDS if field not in data]
    if missing:
        raise CustomInvoiceError(missing)
    else:
        return True

class CustomInvoiceError(Exception):
    def __init__(self, missing):
        self.missing = missing
        super().__init__(f"Отсутствуют поля: {', '.join(missing)}")

#B9
def batch_process(paths):
    results = []
    errors = []
    for path in paths:
        try:
            if path.endswith(".nonexistent"):
                raise FileNotFoundError(f"Ошибка: {path}")
            content = f"Content of {path}" 
            results.append({"path": path, "content": content})
        except Exception as e:
            errors.append((path, str(e)))
    return results, errors

#C10
import pdfplumber
import traceback

def safe_extract_pdf(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            if not pdf.pages:
                print(f"Внимание: PDF '{pdf_path}' пустой.")
                return None
            first_page = pdf.pages[0]
            return first_page.extract_text()
    except FileNotFoundError:
        print(f"Внимание: Файл не найден в {pdf_path}")
        return None
    except pdfplumber.pdferrors.PDFSyntaxError:
        print(f"Внимание: Нерабочий PDF в {pdf_path}")
        return None
    except Exception as e:
        print(f"Внимание: Неожиданная ошибка в {pdf_path}. Тип ошибки: {type(e).__name__}")
        return None
    
#C11
def safe_run(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Внимание: Ошибка в функции '{func.__name__}': {e}")
            return None
    return wrapper

@safe_run
def risky_function(x):
    return 1 / x
print(risky_function(2))
print(risky_function(0))

#C12
def parse_invoice(path):
    if "error" in path:
        raise ValueError(f"Не удалось прочитать {path}")
    return {"sender": "Company A", "amount": 1500.00, "currency": "USD"}

class InvoiceProcessor:
    def __init__(self, paths):
        self.paths = paths
        self.results = []
        self.errors = []

    def process_all(self):
        self.results = []
        self.errors = []
        for path in self.paths:
            try:
                data = parse_invoice(path)
                self.results.append({"path": path, "data": data})
            except Exception as e:
                self.errors.append({"path": path, "error": str(e)})
        return self.results, self.errors

    def report(self):
        print(f"\nОбработано: {len(self.results)}")
        print(f"Ошибок: {len(self.errors)}")
        for r in self.results:
            print(f"  Ок: {r['path']} -> {r['data']}")
        for e in self.errors:
            print(f"  Ошибка: {e['path']} -> {e['error']}")

#C13
def manual_parse(path):
    return {"sender": "Company A", "amount": 1500.00, "currency": "USD"}

def ai_parse(text):
    return {"sender": "Company A", "amount": 1620.00, "currency": "USD"}

def compare_with_ai(invoice_path):
    manual = manual_parse(invoice_path)
    ai = ai_parse("текст инвойса")

    match = manual == ai
    status = "ok"

    if not match:
        diff = abs(manual["amount"] - ai["amount"])
        percent = diff / manual["amount"] * 100
        if percent > 10:
            status = "requires_review"

    return {
        "manual": manual,
        "ai": ai,
        "match": match,
        "status": status
    }

#D14
def process_invoice_file(path):
    try:
        with open(path, 'r') as f:
            content = f.read()
            data = parse_invoice(content) 
            validate(data)
            save(data)
        print(f"Успех {path}")
    except FileNotFoundError:
        print(f"Ошибка: Файл не найден в '{path}'.")
    except ValueError as ve:
        print(f"Ошибка парсинга в '{path}'.")
    except Exception as e:
        print(f"Неожиданная ошибка в '{path}'.")

#D15
def handle_errors():
    try:
        risky_operation()
    except Exception as e:
        print(f"Первая ошибка: {e}")
        try:
            fallback_operation()
        except Exception as fe:
            print(f"Ошибка в резервной операции: {fe}")

#D16
def get_invoice_value(data, key):
    try:
        return data[key]
    except KeyError:
        return "default"
    finally:
        pass
print(get_invoice_value({"a": 1}, "b"))

#F19
#try-except используется когда ошибка является исключительной ситуацией, а не частью хода программы.
#1. При попытке чтения файла, файл может не существовать
#2. При парсинге в PDF файле может не быть данных
#if используется для контроля ожидаемых данных.
#1. Можно использовать для проверки списка инвойсов в папке
#2. Также можно использовать для проверки наличия определённого типа данных в файле