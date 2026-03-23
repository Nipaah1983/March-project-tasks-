files = [
    "MaxMara_001.pdf",
    "Rinaldi_002.pdf",
    "readme.txt",
    "DEDIMAX_003.pdf",
    "Coccinelle_004.pdf",
    "backup.zip",
    "IFD_005.pdf"
]

processed = 0
for name in files:
    if not name.lower().endswith(".pdf"):
        continue
    print(f"Обрабатываю: {name}")
    processed += 1
print(f"Обработано PDF-файлов: {processed}")