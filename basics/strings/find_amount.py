with open("invoice_sample.txt", "r") as f:
    for line in f:
        if "Amount:" in line:
            print(line.strip())