with open("invoice_sample.txt", "r") as f:
    for line in f:
        if "Amount:" in line:
            parts = line.split(": ")
            value_part = parts[1]
            amount = value_part.split(" ")[0]
            print(amount)