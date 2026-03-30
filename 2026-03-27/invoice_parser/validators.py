from typing import Dict, List, Any


def validate_invoice(invoice: Dict[str, Any], index: int) -> List[str]:
    errors = []

    if "supplier" not in invoice:
        errors.append(f"Инвойс {index}: нет поля supplier")
    elif not isinstance(invoice["supplier"], str):
        errors.append(f"Инвойс {index}: supplier должен быть строкой")

    if "amount" not in invoice:
        errors.append(f"Инвойс {index}: нет поля amount")
    elif not isinstance(invoice["amount"], (int, float)):
        errors.append(f"Инвойс {index}: amount должен быть числом")
    elif invoice["amount"] <= 0:
        errors.append(f"Инвойс {index}: amount <= 0")

    if "currency" not in invoice:
        errors.append(f"Инвойс {index}: нет поля currency")
    elif invoice["currency"] not in ["EUR", "USD", "RUB"]:
        errors.append(f"Инвойс {index}: недопустимая валюта {invoice['currency']}")

    return errors