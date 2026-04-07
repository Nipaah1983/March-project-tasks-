import os
import json
import logging

logging.basicConfig(filename='errors.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_text_from_txt(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def parse_invoice_data(text):
    if "good_invoice" in text:
        return {
            "supplier": "Example Supplier",
            "amount": 123.45,
            "date": "2024-04-07"
        }
    elif "broken_invoice" in text:
        raise ValueError("Ошибка в структуре данных")
    else:
        raise ValueError("Неизвестный формат текста")

def robust_invoice_parser():
    invoices_dir = "invoices"
    output_json_file = "invoices.json"
    
    os.makedirs(invoices_dir, exist_ok=True)
    
    with open(os.path.join(invoices_dir, "good_invoice_1.txt"), "w") as f:
        f.write("header\ngood_invoice\nsupplier: A\namount: 100\ndate: 2023-01-01\nfooter")
    with open(os.path.join(invoices_dir, "good_invoice_2.txt"), "w") as f:
        f.write("another good_invoice file\nsupplier: B\namount: 200\ndate: 2023-02-15")
    with open(os.path.join(invoices_dir, "good_invoice_3.txt"), "w") as f:
        f.write("just a good_invoice\nsupplier: C\namount: 150.50\ndate: 2023-03-10")
    with open(os.path.join(invoices_dir, "broken_invoice_1.txt"), "w") as f:
        f.write("broken_invoice\nsupplier: D\namount: 300\ndate: 2023-04-20")
    with open(os.path.join(invoices_dir, "broken_invoice_2.txt"), "w") as f:
        f.write("another broken_invoice\nsupplier: E\namount: 400")

    all_parsed_data = []
    
    for filename in os.listdir(invoices_dir):
        if filename.endswith(".txt"):
            filepath = os.path.join(invoices_dir, filename)
            try:
                text = extract_text_from_txt(filepath)
                parsed_data = parse_invoice_data(text)
                all_parsed_data.append(parsed_data)
            except Exception as e:
                log_message = f"Error processing {filename}: {e}"
                print(log_message)
                logging.error(log_message)
    with open(output_json_file, 'w', encoding='utf-8') as f:
        json.dump(all_parsed_data, f, ensure_ascii=False, indent=4)
    print(f"Обработка завершена. Результаты сохранены в {output_json_file}. Ошибки записаны в errors.log.")

robust_invoice_parser()